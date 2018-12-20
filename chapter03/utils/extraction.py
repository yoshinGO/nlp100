import gzip
import json


def extract_UK(fname):
    '''イギリスの関する記事本文を取得

    戻り値：
    イギリスの記事本文
    '''

    with gzip.open(fname, mode='rt', encoding='utf-8') as data_file:
        for line in data_file:
            # json形式の文字列を辞書型に変関するためにjsonモジュールのloads関数を使う
            data_json = json.loads(line)
            if data_json['title'] == 'イギリス':
                return data_json['text']

    raise ValueError('イギリスの記事が見つからない')
