"""
45のプログラムを改変し，述語と格パターンに続けて項（述語に係っている文節そのもの）を
タブ区切り形式で出力せよ．
45の仕様に加えて，以下の仕様を満たすようにせよ．

項は述語に係っている文節の単語列とする（末尾の助詞を取り除く必要はない）
述語に係る文節が複数あるときは，助詞と同一の基準・順序でスペース区切りで並べる
「吾輩はここで始めて人間というものを見た」という例文（neko.txt.cabochaの8文目）を考える．
 この文は「始める」と「見る」の２つの動詞を含み，「始める」に係る文節は「ここで」，
 「見る」に係る文節は「吾輩は」と「ものを」と解析された場合は，次のような出力になるはずである．

始める  で      ここで
見る    は を   吾輩は ものを
"""
from constants import FNAME_PARSED, FNAME_RESULT
from models import Morph, Chunk
from n41 import neko_chunk


if __name__ == '__main__':
    with open(FNAME_RESULT, 'w') as out_file:
        for chunks in neko_chunk(FNAME_PARSED):
            for chunk in chunks:
                # 動詞を含むかチェック
                verbs = chunk.get_morphs_by_pos('動詞')
                if len(verbs) < 1:
                    continue

                # 係り元に助詞を含むchunkを列挙
                chunks_include_prt = []
                for src_number in chunk.srcs:
                    if len(chunks[src_number].get_kaku_prt()) > 0:
                        chunks_include_prt.append(chunks[src_number])
                if len(chunks_include_prt) < 1:
                    continue

                # chunkを助詞の辞書順でソート
                chunks_include_prt.sort(key=lambda x: x.get_kaku_prt())

                # 出力
                out_file.write('{}\t{}\t{}\n'.format(
                    verbs[0].base,  # 最左の動詞の基本形
                    ' '.join([chunk.get_kaku_prt() for chunk in chunks_include_prt]),  # 助詞
                    ' '.join([chunk.normalized_surface() for chunk in chunks_include_prt])  # 項
                ))
