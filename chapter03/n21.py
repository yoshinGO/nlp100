"""
記事中でカテゴリ名を宣言している行を抽出せよ
"""
import re

pattern = re.compile(r'^\[\[Category:.*\]\]$')

with open('britain.txt', 'r') as britain_file:
    for line in britain_file:
        match = pattern.search(line)
        if match:
            print(match.group())
