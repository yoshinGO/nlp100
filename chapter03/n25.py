"""
記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，
辞書オブジェクトとして格納せよ．
"""
# coding: utf-8
import gzip
import json
import re
fname = '../data/jawiki-country.json.gz'


def extrant_UK():
    '''イギリスに関する記事本文を取得

    戻り値：
    イギリスの記事本文
    '''
    # gzipを使うときはmode引数に明示的にtを指定しないとバイナリーモードになる
    with gzip.open(fname, 'rt') as data_file:
        for line in data_file:
            # json形式の文字列を辞書型に辞書型にするためにjsonモジュールのloads関数を使う
            data_json = json.loads(line)
            if data_json['title'] == 'イギリス':
                return data_json['text']

    raise ValueError('イギリスの記事が見つからない')


# 基礎情報テンプレートの抽出条件のコンパイル
pattern = re.compile(r'''
    ^\{\{基礎情報.*?$  # '{{基礎情報'で始まる行
    (.*?)  # キャプチャ対象, 任意の0文字以上, 非貪欲
    ^\}\}$  # '}}'の行
    ''', re.MULTILINE + re.VERBOSE + re.DOTALL)

# 基礎情報テンプレートの抽出
contents = pattern.findall(extrant_UK())

# 抽出結果からのフィールドメイトあたいの抽出条件コンパイル
patten = re.compile(r'''
    ^\|  # '|'で始まる行
    (.+?)  # キャプチャ対象（フィールド名）, 任意の1文字以上, 非貪欲
    \s*  # 空白文字0文字以上
    =
    \s*  # 空白文字0文字以上
    (.+?)  # キャプチャ対象（値）, 任意の1文字以上, 非貪欲
    (?:  # キャプチャ対象外のグループ開始
        (?=\n\|)  # 改行+'|'の手前（肯定の先読み）
        | (?=\n$)  # または, 改行+終端の手前（肯定の先読み）
        # 肯定の先読みを使って、直後に|または改行+終端があるものに一致するようにする
    )  # グループ終了
    ''', re.MULTILINE + re.VERBOSE + re.DOTALL)

# フィールドメイトあたいの抽出
fields = patten.findall(contents[0])

# 辞書にセット
result = {}
keys_test = []  # 確認用の出現順フィールド名リスト
for field in fields:
    result[field[0]] = field[1]  # fieldはjson形式であり、そのキーとバリューを辞書型で管理
    keys_test.append(field[0])

# 確認のため表示（確認しやすいようにkeys_testを使ってフィールド名の出現順にソート）
for item in sorted(result.items(), key=lambda field: keys_test.index(field[0])):
    print(item)
