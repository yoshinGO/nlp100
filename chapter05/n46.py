"""
45のプログラムを改変し，述語と格パターンに続けて項（述語に係っている文節そのもの）をタブ区切り形式で出力せよ．
45の仕様に加えて，以下の仕様を満たすようにせよ．

項は述語に係っている文節の単語列とする（末尾の助詞を取り除く必要はない）
述語に係る文節が複数あるときは，助詞と同一の基準・順序でスペース区切りで並べる
「吾輩はここで始めて人間というものを見た」という例文（neko.txt.cabochaの8文目）を考える．
この文は「始める」と「見る」の２つの動詞を含み，「始める」に係る文節は「ここで」，
「見る」に係る文節は「吾輩は」と「ものを」と解析された場合は，次のような出力になるはずである．

始める  で      ここで
見る    は を   吾輩は ものを
"""
from utils import make_chunks
from constants import FNAME_PARSED

with open('result_n46.py', mode='w') as out_file:
    if __name__ == '__main__':
        for chunks in make_chunks(FNAME_PARSED):
            for chunk in chunks:
                verb_info = chunk.get_morphlist_by_pos('動詞')
                if len(verb_info) < 1:
                    continue  # 文節内に動詞がない場合は次の文節へ

                particles = []
                chunks_attached_by_particle = []
                for src_number in chunk.srcs:
                    particle_info = chunks[src_number].get_morphlist_by_pos('助詞')
                    if len(particle_info) > 0:
                        particles.append(particle_info[0].base)
                        chunks_attached_by_particle.append(chunks[src_number].normalized_surface())

                if len(particles) < 1:
                    continue  # 係り受けの文節内に助詞がなかった場合は何も表示しない

                out_file.write('{}\t{}\t{}\n'.format(
                    verb_info[0].base,
                    ' '.join(particles),
                    ' '.join(chunks_attached_by_particle)
                ))
