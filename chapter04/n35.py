"""
名詞の連接（連続して出現する名詞）を最長一致で抽出せよ．
"""

from constants import FNAME_PARSED
from n30 import neko_lines

list_series_noun = []
if __name__ == '__main__':
    for morphemes in neko_lines(FNAME_PARSED):
        nouns = []  # 名詞のリスト
        for morpheme in morphemes:
            if morpheme['pos'] == '名詞':
                nouns.append(morpheme['surface'])
            else:
                if len(nouns) > 1:
                    list_series_noun.append(''.join(nouns))
                nouns = []
        # 名詞で終わる行の場合, 最後の連続する名詞を追加する必要がある
        if len(nouns) > 1:
            list_series_noun.append("".join(nouns))

    # 重複除去して表示
    print(set(list_series_noun))
