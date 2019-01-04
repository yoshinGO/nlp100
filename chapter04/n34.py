"""
2つの名詞が「の」で連結されている名詞句を抽出せよ.
"""
from constants import FNAME_PARSED
from n30 import neko_lines

for morphemes in neko_lines(FNAME_PARSED):
    number_of_morpheme = len(morphemes)
    if number_of_morpheme > 2:
        for i in range(1, number_of_morpheme - 1):
            if morphemes[i]['surface'] == 'の' and morphemes[i-1]['pos'] == '名詞' and morphemes[i+1]['pos'] == '名詞':
                print(f'{morphemes[i-1]["surface"]}の{morphemes[i+1]["surface"]}')
