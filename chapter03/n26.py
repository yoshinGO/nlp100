"""
25の処理時に，テンプレートの値からMediaWikiの
強調マークアップ（弱い強調，強調，強い強調のすべて）を除去してテキストに変換せよ
"""
import re


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


# 基礎情報テンプレートの抽出条件のコンパイル
extract_pattern = re.compile(r'''
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
    contents = extract_pattern.findall(britain_file.read())  # findallは正規表現にマッチする部分文字列を全て探し出しリストとして返す（インデックスは0ベース）
    # フィールド名と値の抽出
    fiels_values = field_value_pattern.findall(contents[0])  # キャプチャの機能により ('フィールド名', 'キャプチャ名')の形式で複数のデータがリストに格納される

    # 辞書にセット
    result = {}
    keys_test = []  # 確認用の出現フィールド名リスト
    for field_value in fiels_values:
        """
        field_valueには ('略名', 'イギリス') や ('確立形態4', "現在の国号「'''グレートブリテン及び北アイルランド連合王国'''」に変更")の形で値が代入される
        """
        result[field_value[0]] = remove_markup(field_value[1])
        keys_test.append(field_value[0])

    # 確認のため表示（確認しやすいようにkeys_testを使ってフィールド名の出現順にソート）
    for item in sorted(result.items(), key=lambda field_value: keys_test.index(field_value[0])):
        print(item)
