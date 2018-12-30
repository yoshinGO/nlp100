"""
Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．
問題21-29では，ここで抽出した記事本文に対して実行せよ
"""
import gzip
import json


with gzip.open('../data/jawiki-country.json.gz', 'rt') as data_file:
    for country_info in data_file:
        # json形式の文字列を辞書型に変換して, if文でイギリスの記事を探す
        country_dict = json.loads(country_info)
        if country_dict['title'] == 'イギリス':
            with open('britain.txt', 'w') as britain_file:
                britain_file.write(country_dict['text'])
            break
