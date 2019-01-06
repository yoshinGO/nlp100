"""
名詞を含む文節が，動詞を含む文節に係るとき，これらをタブ区切り形式で抽出せよ．
ただし，句読点などの記号は出力しないようにせよ．
"""
from constants import FNAME_PARSED
from n41 import neko_chunk
from models import Morph, Chunk

if __name__ == '__main__':
    for chunks in neko_chunk(FNAME_PARSED):

        # 係り先があるものを列挙
        for chunk in chunks:
            if chunk.dst != -1:  # chunk.dstが-1であるとは, その文節はどの文節にも係っていない状態(係り先がない)

                # この文節に名詞があるか, この文節の係り先に動詞があるかチェック
                if chunk.chk_pos('名詞') and chunks[chunk.dst].chk_pos('動詞'):  # chunks[chunk.dst]でこの文節の係り先の文節が取得できる.

                    # 記号を除いた表層系をチェック, 空なら除外
                    src_surface = chunk.normalized_surface()
                    dst_surface = chunks[chunk.dst].normalized_surface()
                    if src_surface != '' and dst_surface != '':
                        print(f'{src_surface}\t{dst_surface}')
