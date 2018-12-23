"""
記事中に含まれるセクション名とそのレベル（例えば"== セクション名 =="なら1）を表示せよ．
"""
import gzip
import json
import re

pattern = re.compile(r'^(={2,})\s*(.+?)\s*\1.*$', re.MULTILINE)

with open('britain.txt', 'r') as britain_file:
    # findallは正規表現にマッチする部分文字列を全て探し出しリストとして返す（インデックスは0ベース）
    result = pattern.findall(britain_file.read())
    # 結果表示
    for line in result:
        level = len(line[0]) - 1  # '='の数-1
        print('{indent}{sect}({level})'.format(indent='\t'*(level-1), sect=line[1], level=level))
