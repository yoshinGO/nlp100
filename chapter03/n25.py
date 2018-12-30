"""
記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，
辞書オブジェクトとして格納せよ
"""
import re
from collections import OrderedDict

basic_info_pattern = re.compile(r'^\{\{基礎情報.*?$(.*?)^\}\}$', re.MULTILINE + re.DOTALL)

with open('britain.txt', 'r') as britain_file:
    contents = basic_info_pattern.findall(britain_file.read())

    # フィールド名と値の抽出
    field_value_pattern = re.compile(r'^\|(.+?)\s*=\s*(.+?)(?:(?=\n\|)|(?=\n$))', re.MULTILINE + re.DOTALL)  # ?:で肯定の先読みを行う
    fields_values = field_value_pattern.findall(contents[0])  # contensはエスケープ文字が残ってるが, contents[0]とすることでそれらが全て処理された状態で取得できる

    # 辞書にセット
    result = OrderedDict()
    for field_value in fields_values:
        # field_valueにはキャプチャした二つの値がタプル型で格納されている
        result[field_value[0]] = field_value[1]  # field_valueの形式 : ('フィールド名', 'バリュー')

    for item in result.items():  # resultはdict型, itemはtuple型
        print(item)
