"""
テンプレートの内容を利用し，国旗画像のURLを取得せよ．
"""
# TODO: いつかやり直す, 2018/12/30
import re
import json
import urllib.parse
import urllib.request
from n26 import remove_markup
from n27 import remove_internallinks
from n28 import remove_media

if __name__ == '__main__':
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
        contents = basic_info_pattern.findall(britain_file.read())  # findallは正規表現にマッチする部分文字列を全て探し出しリストとして返す（インデックスは0ベース）
        # フィールド名と値の抽出
        fields_values = field_value_pattern.findall(contents[0])  # キャプチャの機能により ('フィールド名', 'キャプチャ名')の形式で複数のデータがリストに格納される

        # 辞書にセット
        result = {}
        for field_value in fields_values:
            """
            field_valueには ('略名', 'イギリス') や ('確立形態4', "現在の国号「'''グレートブリテン及び北アイルランド連合王国'''」に変更")の形で値が代入される
            """
            result[field_value[0]] = remove_markup(remove_internallinks(remove_media(field_value[1])))

        # 国旗画像の値を取得
        fname_flag = result['国旗画像']

        # リクエスト生成
        url = 'https://www.mediawiki.org/w/api.php?' \
        + 'action=query' \
        + '&titles=File:' + urllib.parse.quote(fname_flag) \
        + '&format=json' \
        + '&prop=imageinfo' \
        + '&iiprop=url'

        # MediaWikiのサービスへリクエスト送信
        request = urllib.request.Request(url, headers={'User-Agent': 'NLP100_Python(@segavvy)'})
        connection = urllib.request.urlopen(request)

        # jsonとして受信
        data = json.loads(connection.read().decode())

        # URL取り出し
        url = data['query']['pages'].popitem()[1]['imageinfo'][0]['url']
        print(url)
