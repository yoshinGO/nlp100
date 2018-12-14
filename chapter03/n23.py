"""
記事中に含まれるセクション名とそのレベル（例えば"== セクション名 =="なら1）を表示せよ
"""
# condig: utf-8
import gzip
import json
import re
fname = '../data/jawiki-country.json.gz'


def extract_UK():
    '''イギリスに関する記事本文を取得

    戻り値：
    イギリスの記事本文
    '''
    # gzipを使うときはmode引数に明示的にtを指定しないとバイナリーモードになる
    with gzip.open(fname, 'rt') as data_file:
        for line in data_file:
            # json形式の文字列を辞書型に変換するためにjsonモジュールのloads関数を使う
            data_json = json.loads(line)
            if data_json['title'] == 'イギリス':
                return data_json['text']

    raise ValueError('イギリスの記事が見つからない')


# 正規表現のコンパイル
pattern = re.compile(r'''
    ^        # 行頭
    (={2,})  # キャプチャ対象
    \s*      # 余分な0個以上の空白（'哲学'や'婚姻'の前後に余分な空白があるので撤去）
    (.+?)    # キャプチャ対象、任意の文字が１文字以上、一番短い文字列にマッチ
    \s*      # 余分な0子以上の空白
    \1       # 後方参照、１番目のキャプチャ対象と同じ内容
    .*       # 任意の文字が0文字以上
    $        # 行末
    ''', re.MULTILINE + re.VERBOSE)

# 抽出
result = pattern.findall(extract_UK())

# 結果表示
for line in result:
    level = len(line[0]) - 1  # '='の数-1
    print('{indent}{sect}({level})'.format(
        indent='\t' * (level - 1), sect=line[1], level=level))
