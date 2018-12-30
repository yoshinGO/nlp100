"""
27の処理に加えて，テンプレートの値からMediaWikiマークアップを可能な限り除去し，
国の基本情報を整形せよ
"""
import re
from n26 import remove_markup, show_extracted_sentence
from n27 import remove_internallinks


def remove_media(target):
    # Template:Langの除去        {{lang|言語タグ|文字列}}
    lang_pattern = re.compile(r'''
        \{\{lang    # '{{lang'（マークアップの開始）
        (?:         # キャプチャ対象外のグループ開始
            [^|]*?  # '|'以外の文字が0文字以上、非貪欲
            \|      # '|'
        )*?         # グループ終了、このグループが0以上出現、非貪欲
        ([^|]*?)    # キャプチャ対象、'|'以外が0文字以上、非貪欲（表示対象の文字列）
        \}\}        # '}}'（マークアップの終了）
        ''', re.MULTILINE + re.VERBOSE)
    target = lang_pattern.sub(r'\1', target)

    # 外部リンクの除去  [http://xxxx] 、[http://xxx xxx]
    externallink_pattern = re.compile(r'''
        \[http:\/\/ # '[http://'（マークアップの開始）
        (?:         # キャプチャ対象外のグループ開始
            [^\s]*? # 空白以外の文字が0文字以上、非貪欲
            \s      # 空白
        )?          # グループ終了、このグループが0か1出現
        ([^]]*?)    # キャプチャ対象、']'以外が0文字以上、非貪欲（表示対象の文字列）
        \]          # ']'（マークアップの終了）
        ''', re.MULTILINE + re.VERBOSE)
    target = externallink_pattern.sub(r'\1', target)

    # <br>、<ref>の除去
    br_ref_pattern = re.compile(r'''
        <           # '<'（マークアップの開始）
        \/?         # '/'が0か1出現（終了タグの場合は/がある）
        [br|ref]    # 'br'か'ref'
        [^>]*?      # '>'以外が0文字以上、非貪欲
        >           # '>'（マークアップの終了）
        ''', re.MULTILINE + re.VERBOSE)
    return br_ref_pattern.sub('', target)


if __name__ == '__main__':
    show_extracted_sentence(remove_markup, remove_internallinks, remove_media)
