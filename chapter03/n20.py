"""
Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．
問題21-29では，ここで抽出した記事本文に対して実行せよ．
"""
# coding: utf-8
import gzip
import json


# gzipを使うときはmode引数に明示的にtを指定しないとバイナリーモードになる
with gzip.open('../data/jawiki-country.json.gz', 'rt', encoding='utf-8') as data_file:
    for line in data_file:
        # json形式の文字列を辞書型に変換するためにjsonモジュールのloads関数を使う
        country_info = json.loads(line)
        if country_info['title'] == 'イギリス':
            print(country_info['text'])
            with open('Britain.txt', 'w', encoding='utf-8') as result:
                result.write(country_info['text'])
            break
