"""
文中のすべての名詞を含む文節に対し，その文節から構文木の根に至るパスを抽出せよ.
ただし，構文木上のパスは以下の仕様を満たすものとする.

各文節は（表層形の）形態素列で表現する
パスの開始文節から終了文節に至るまで，各文節の表現を"->"で連結する
「吾輩はここで始めて人間というものを見た」という文（neko.txt.cabochaの8文目）から，次のような出力が得られるはずである.

吾輩は -> 見た
ここで -> 始めて -> 人間という -> ものを -> 見た
人間という -> ものを -> 見た
ものを -> 見た
"""
from constants import FNAME_PARSED, FNAME_RESULT
from models import Morph, Chunk
from n41 import neko_chunk

if __name__ == '__main__':
    with open(FNAME_RESULT, mode='w') as out_file:
        for chunks in neko_chunk(FNAME_PARSED):
            for chunk in chunks:
                # 名詞を含むかチェック
                if(len(chunk.get_morphs_by_pos('名詞')) > 0):
                    # 名詞のchunkを出力
                    out_file.write(chunk.normalized_surface())

                    # 根へのパスを出力
                    dst = chunk.dst
                    while dst != -1:
                        out_file.write(' -> ' + chunks[dst].normalized_surface())
                        dst = chunks[dst].dst
                    out_file.write('\n')
