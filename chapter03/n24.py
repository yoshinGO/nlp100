"""
記事から参照されているメディアファイルをすべて抜き出せ
"""
import re

pattern = re.compile(r'\[\[(?:File|ファイル):(.+?)\|')

with open('britain.txt', 'r') as britain_file:
    result = pattern.findall(britain_file.read())
    # 結果表示
    for line in result:
        print(line)
