"""
名詞を含む文節が，動詞を含む文節に係るとき，これらをタブ区切り形式で抽出せよ．
ただし，句読点などの記号は出力しないようにせよ．
"""
from utils import make_chunks
from constants import FNAME_PARSED

# 12文目まで表示
if __name__ == '__main__':
    for i, chunks in enumerate(make_chunks(FNAME_PARSED)):
        for chunk in chunks:
            if chunk.dst != -1 and chunk.chk_pos('名詞') and chunks[chunk.dst].chk_pos('動詞'):
                print('{}\t{}'.format(chunk.normalized_surface(), chunks[chunk.dst].normalized_surface()))
        if i == 12:
            break
