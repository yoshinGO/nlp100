"""
文章中に出現する単語とその出現頻度を求め，出現頻度の高い順に並べよ.
"""
from constants import FNAME_PARSED
from collections import defaultdict
from n30 import neko_lines

if __name__ == '__main__':
    word_count = defaultdict(lambda: 0)
    for morphemes in neko_lines(FNAME_PARSED):
        for morpheme in morphemes:
            if morpheme['pos'] == '名詞':
                word_count[morpheme['surface']] += 1

    for k, v in sorted(word_count.items(), key=lambda x: -x[1]):
        print(f'{str(k)}: {str(v)}')
