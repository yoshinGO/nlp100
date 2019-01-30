"""
文中のすべての名詞を含む文節に対し，その文節から構文木の根に至るパスを抽出せよ． ただし，構文木上のパスは以下の仕様を満たすものとする．

各文節は（表層形の）形態素列で表現する
パスの開始文節から終了文節に至るまで，各文節の表現を"->"で連結する
「吾輩はここで始めて人間というものを見た」という文（neko.txt.cabochaの8文目）から，次のような出力が得られるはずである．

吾輩は -> 見た
ここで -> 始めて -> 人間という -> ものを -> 見た
人間という -> ものを -> 見た
ものを -> 見た
"""

# 名詞を含む文節を探して、その係り先(dst)の文節をextractして、extractした文節の係り先(dst)が-1になるまで続ける(再帰関数を定義しよう)
# 名詞を見つけるたびに書き込みをout_fileに書き込みを行う

from utils import make_chunks
from constants import FNAME_PARSED

with open('result_n48.txt', mode='w') as out_file:
    if __name__ == '__main__':
        for chunks in make_chunks(FNAME_PARSED):  # １文ごとの係り受け解析結果のジュネレータ
            for chunk in chunks:
                # 名詞を含む文節を探す
                noun_info = chunk.get_morphlist_by_pos('名詞')
                if len(noun_info) < 1 or chunk.dst == -1:  # 名詞が存在しない場合もしくは係り先の文節が存在しない場合は次の文節へ
                    continue

                out_file.write('{}\n'.format(' -> '.join(chunk.chunk_dst_relation(chunks))))
