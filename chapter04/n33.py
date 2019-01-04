"""
サ変接続の名詞をすべて抽出せよ.
"""
from constants import FNAME_PARSED
from n30 import neko_lines

if __name__ == '__main__':
    for morphemes in neko_lines(FNAME_PARSED):
        for morpheme in morphemes:
            if morpheme['pos'] == '名詞' and morpheme['pos1'] == 'サ変接続':
                print(morpheme['surface'])
