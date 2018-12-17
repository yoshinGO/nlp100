
"""
25の処理時に，テンプレートの値からMediaWikiの強調マークアップ（弱い強調，強調，
強い強調のすべて）を除去してテキストに変換せよ
"""
# coding: utf-8
import gzip
import json
import re
fname = '../data/jawiki-country.json.gz'


def extract_UK():
    '''イギリスに関する記事本文を取得

    戻り値：
    イギリスの記事本文
    '''

    with gzip.open(fname, 'rt') as data_file:
        for line in data_file:
            data_json = json.loads(line)
            if data_json['title'] == 'イギリス':
                return data_json['text']

    raise ValueError('イギリスの記事が見つからない')


def remove_markup(target):
    '''マークアップの除去
    強調マークアップを除去する

    引数：
    target -- 対象の文字列
    戻り値：
    マークアップを除去した文字列
    '''

    # 除去対象の正規表現のコンパイル
    pattern = re.compile(r'''
    \'{2,5} # 2~5個の'(シングルクォーテーション)
    ''', re.MULTILINE + re.VERBOSE)

    # 空文字に置換
    return pattern.sub('', target)


# 基礎情報テンプレートの抽出条件のコンパイル
pattern = re.compile(r'''
    ^\{\{基礎情報.*?$  # '{{基礎情報'で始まる行
    (.*?)  # キャプチャ対象, 任意の0文字以上, 非貪欲
    ^\}\}$  # '}}'の行
    ''', re.MULTILINE + re.VERBOSE + re.DOTALL)

# 基礎情報テンプレートの抽出
contents = pattern.findall(extract_UK())

# 抽出結果からのフィールド名と値の抽出条件のコンパイル
pattern = re.compile(r'''
    ^\|  # '|'で始まる行
    (.+?)  # キャプチャ対象（フィールド名）, 任意の1文字以上, 非貪欲
    \s*  # 空白文字0文字以上
    =
    \s*  # 空白文字0文字以上
    (.+?)  # キャプチャ対象（値）, 任意の1文字以上, 非貪欲
    (?:  # キャプチャ対象外のグループ開始
        (?=\n\|)  # 改行+'|'の手前（肯定の先読み）
        | (?=\n$)  # または, 改行+終端の手前（肯定の先読み）
    )  # グループ終了
    ''', re.MULTILINE + re.VERBOSE + re.DOTALL)

# フィールド名と値の抽出
fields = pattern.findall(contents[0])

# 辞書にセット
result = {}
keys_test = []  # 確認用の出現順フィールド名リスト
for field in fields:
    result[field[0]] = remove_markup(field[1])
    keys_test.append(field[0])

# 確認のため表示
for item in sorted(result.items(), key=lambda field: keys_test.index(field[0])):
    print(item)
