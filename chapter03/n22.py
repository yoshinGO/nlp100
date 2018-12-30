"""
記事のカテゴリ名を（行単位ではなく名前で）抽出せよ
"""
import re

pattern = re.compile(r'^\[\[Category:(.+?)(?:\|.+)?\]\]$')

with open('britain.txt', 'r') as britain_file:
    for line in britain_file:
        match = pattern.search(line)
        if match:
            print(match.group(1))
