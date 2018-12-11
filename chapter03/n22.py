"""
記事のカテゴリ名を（行単位ではなく名前で）抽出せよ
"""
import re

# 例：[[Category:G8加盟国]]
# 例：[[Category:島国|くれいとふりてん]]
pattern = re.compile(r'^\[\[Category:(.+?)(?:\|.+)?\]\]$')

with open('../tmp/Britain.txt', 'r', encoding='utf-8') as britain_file:
    for line in britain_file:
        match = pattern.search(line)
        if match:
            print(match.group(1))
