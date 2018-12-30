"""
25の処理時に，テンプレートの値からMediaWikiの
強調マークアップ（弱い強調，強調，強い強調のすべて）を除去してテキストに変換せよ
"""
import re
from collections import OrderedDict


def remove_markup(target):
    '''マークアップの除去
    強調マークアップを除去する

    引数：
    target -- 対象の文字列
    戻り値：
    マークアップを除去した文字列
    '''
    # 除去対象の正規表現のコンパイル
    remove_pattern = re.compile(r'\'{2,5}', re.MULTILINE)

    # 空文字に置換
    return remove_pattern.sub('', target)


def show_extracted_sentence(*regexes):
    # 基礎情報テンプレートの抽出条件のコンパイル
    basic_info_pattern = re.compile(r'''
        ^\{\{基礎情報.*?$  # '{{基礎情報'で始まる行
        (.*?)  # キャプチャ対象, 任意の0文字以上, 非貪欲
        ^\}\}$  # '}}'の行
        ''', re.MULTILINE + re.VERBOSE + re.DOTALL)

    # 抽出結果からのフィールド名と値の抽出条件のコンパイル
    field_value_pattern = re.compile(r'''
        ^\|         # '|'で始まる行
        (.+?)       # キャプチャ対象（フィールド名）、任意の1文字以上、非貪欲
        \s*         # 空白文字0文字以上
        =
        \s*         # 空白文字0文字以上
        (.+?)       # キャプチャ対象（値）、任意の1文字以上、非貪欲
        (?:         # キャプチャ対象外のグループ開始
            (?=\n\|)    # 改行+'|'の手前（肯定の先読み）
            | (?=\n$)   # または、改行+終端の手前（肯定の先読み）
        )           # グループ終了
        ''', re.MULTILINE + re.VERBOSE + re.DOTALL)
    with open('britain.txt', 'r') as britain_file:
        # 基礎情報テンプレートの抽出
        # findallは正規表現にマッチする部分文字列を全て探し出しリストとして返す
        contents = basic_info_pattern.findall(britain_file.read())
        # フィールド名と値の抽出
        # キャプチャの機能により ('フィールド名', 'キャプチャ名')の形式で複数のデータがリストに格納される
        fields_values = field_value_pattern.findall(contents[0])

        # 辞書にセット
        result = OrderedDict()
        for field_value in fields_values:
            """
            field_valueには ('略名', 'イギリス') や
            ('確立形態4', "現在の国号「'''グレートブリテン及び北アイルランド連合王国'''」に変更")
            の形で値が代入される
            """
            value = field_value[1]
            for regex in regexes:  # 任意の個数の関数を受け取って, 順々に噛ませる
                value = regex(value)
            result[field_value[0]] = value

        for item in result.items():  # resultはdict型, itemはtuple型
            print(item)


if __name__ == '__main__':
    show_extracted_sentence(remove_markup)
