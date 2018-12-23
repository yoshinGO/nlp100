"""
記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，
辞書オブジェクトとして格納せよ
"""
import re

pattern = re.compile(r'^\{\{基礎情報.*?$(.*?)^\}\}$', re.MULTILINE + re.DOTALL)

with open('britain.txt', 'r') as britain_file:
    contents = pattern.findall(britain_file.read())
    field_value_pattern = re.compile(r'^\|(.+?)\s*=\s*(.+?)(?:(?=\n\|)|(?=\n$))', re.MULTILINE + re.DOTALL)

    # フィールド名と値の抽出
    fiels_values = field_value_pattern.findall(contents[0])

    # 辞書にセット
    result = {}
    keys_test = []
    for field_value in fiels_values:
        result[field_value[0]] = field_value[1]
        keys_test.append(field_value[0])

    # 確認のため表示（確認しやすいようにkeys_testを使ってフィールド名の出現順にソート）
    for item in sorted(result.items(), key=lambda field: keys_test.index(field[0])):
        print(item)
