"""
係り元の文節と係り先の文節のテキストをタブ区切り形式ですべて抽出せよ．
ただし，句読点などの記号は出力しないようにせよ．
"""

from utils import make_chunks
from constants import FNAME_PARSED

# 8文目まで実行する
if __name__ == '__main__':
    for i, chunks in enumerate(make_chunks(FNAME_PARSED), 1):
        for chunk in chunks:
            if chunk.dst != -1:
                src = chunk.normalized_surface()
                dst = chunks[chunk.dst].normalized_surface()
                if src != '' and dst != '':
                    print('{}\t{}'.format(src, dst))
        if i == 8:
            break
