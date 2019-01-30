"""
動詞のヲ格にサ変接続名詞が入っている場合のみに着目したい．46のプログラムを以下の仕様を満たすように改変せよ．

「サ変接続名詞+を（助詞）」で構成される文節が動詞に係る場合のみを対象とする
述語は「サ変接続名詞+を+動詞の基本形」とし，文節中に複数の動詞があるときは，最左の動詞を用いる
述語に係る助詞（文節）が複数あるときは，すべての助詞をスペース区切りで辞書順に並べる
述語に係る文節が複数ある場合は，すべての項をスペース区切りで並べる（助詞の並び順と揃えよ）
例えば「別段くるにも及ばんさと、主人は手紙に返事をする。」という文から，以下の出力が得られるはずである．

返事をする      と に は        及ばんさと 手紙に 主人は
このプログラムの出力をファイルに保存し，以下の事項をUNIXコマンドを用いて確認せよ．

コーパス中で頻出する述語（サ変接続名詞+を+動詞）
コーパス中で頻出する述語と助詞パターン
"""
from utils import make_chunks
from constants import FNAME_PARSED

'''「する」に係っている'''

if __name__ == '__main__':
    with open('result_n47.txt', mode='w') as out_file:
        for chunks in make_chunks(FNAME_PARSED):
            for chunk in chunks:
                verbs_info = chunk.get_morphs_by_pos('動詞')
                if len(verbs_info) < 1 or (verbs_info[0].surface) != 'する':
                    continue
                particles = []
                chunks_attached_by_particle = []
                for src_number in chunk.srcs:
                    particles_info = chunks[src_number].get_morphs_by_pos('助詞')
                    if len(particles_info) > 0:
                        particles.append(particles_info[0].surface)
                        chunks_attached_by_particle.append(chunks[src_number].normalized_surface())

                for src_number in chunk.srcs:
                    sahen_noun_info = chunks[src_number].get_morphs_by_pos('名詞', 'サ変接続')
                    if len(sahen_noun_info) > 0 and chunks[src_number].target_word('を'):
                        out_file.write('{}{}{}\t{}\t{}\n'.format(
                            sahen_noun_info[0].surface,
                            'を',
                            verbs_info[0].base,
                            ' '.join(particles[:-1]),
                            ' '.join(chunks_attached_by_particle[:-1])
                        ))
