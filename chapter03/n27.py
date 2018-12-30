"""
26の処理に加えて，テンプレートの値からMediaWikiの内部リンクマークアップを除去し，テキストに変換せよ
"""
import re
from n26 import remove_markup, show_extracted_sentence


def remove_internallinks(target):
    '''内部リンクの除去
    内部リンクを除去する

    引数：
    target -- 対象の文字列
    戻り値：
    内部リンクを除去した文字列
    '''
    # 内部リンクの削除
    internallinks_pattern = re.compile(r'''
        \[\[      # '[['（マークアップの開始）
        (?:      # キャプチャ対象外のグループ開始
            [^|]*?  # '|'以外の文字が0文字以上, 非貪欲
            \|      # '|'
        )?      # グループ終了, このグループが0または1回出現
        ([^|]*?)  # キャプチャ対象, '|'以外が0文字以上, 非貪欲（表示対象の文字列）
        \]\]
        ''', re.MULTILINE + re.VERBOSE)

    return internallinks_pattern.sub(r'\1', target)


if __name__ == '__main__':
    show_extracted_sentence(remove_markup, remove_internallinks)
