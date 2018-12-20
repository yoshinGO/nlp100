"""
記事のカテゴリ名を（行単位ではなく名前で）抽出せよ
"""
import re
from utils import extraction

# 例：[[Category:G8加盟国]]
# 例：[[Category:島国|くれいとふりてん]]
pattern = re.compile(r'^\[\[Category:(.+?)(?:\|.+)?\]\]$')

britain_file = extraction.extract_UK('../data/jawiki-country.json.gz')
for line in britain_file:
    match = pattern.search(line)
    if match:
        print(match.group(1))
