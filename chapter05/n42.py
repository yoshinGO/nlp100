"""
係り元の文節と係り先の文節のテキストをタブ区切り形式ですべて抽出せよ．
ただし，句読点などの記号は出力しないようにせよ.
"""
from constants import FNAME_PARSED
from models import Morph, Chunk
from n41 import neko_chunk

if __name__ == '__main__':
    for chunks in neko_chunk(FNAME_PARSED):

        # 係り先がるものを列挙
        for chunk in chunks:
            if chunk.dst != -1:

                # 記号を除いた表層系をチェック, 空なら除外
                src_chunk = chunk.normalized_surface()
                dst_chunk = chunks[chunk.dst].normalized_surface()
                if src_chunk != '' and dst_chunk != '':
                    print(f'{src_chunk}\t{dst_chunk}')
