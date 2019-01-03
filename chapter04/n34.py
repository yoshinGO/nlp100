"""
2つの名詞が「の」で連結されている名詞句を抽出せよ.
"""
from constants import FNAME_PARSED
from n30 import neko_lines

for line in neko_lines(FNAME_PARSED):
    if len(line) > 2:
        for i in range(1, len(line) - 1):
            if line[i]['surface'] == 'の' and line[i - 1]['pos'] == '名詞' and line[i + 1]['pos'] == '名詞':
                print(f'{line[i-1]["surface"]}の{line[i+1]["surface"]}')
