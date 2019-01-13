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
from constants import FNAME_PARSED, FNAME_RESULT
from models import Morph, Chunk
from n41 import neko_chunk

if __name__ == '__main__':
    with open(FNAME_RESULT, mode='w') as out_file:
        for chunks in neko_chunk(FNAME_PARSED):
            for chunk in chunks:
                # 動詞を含むかチェック
                verbs = chunk.get_morphs_by_pos('動詞')  # 返り値は動詞の形態素のリスト
                if len(verbs) < 1:
                    continue

                # 係り元に動詞を含むchunkを列挙
                chunks_include_prt = []  # 係り元の文節たちが格納されるリスト
                for src_number in chunk.srcs:
                    if len(chunks[src_number].get_kaku_prt()) > 0:
                        chunks_include_prt.append(chunks[src_number])
                if len(chunks_include_prt) < 1:
                    continue

                # 係り元に「サ変接続名詞+助詞の[を]」があるかチェック
                sahen_wo = ''
                for chunk_src in chunks_include_prt:
                    sahen_wo = chunk_src.get_sahen_wo()
                    if len(sahen_wo) > 0:
                        chunk_remove = chunk_src
                        break
                if len(sahen_wo) < 1:
                    continue

                # 「サ変接続名詞*助詞の[を]」は述語として動詞と一緒に出力するので係り元からは除外
                chunks_include_prt.remove(chunk_remove)

                # chunkを助詞の辞書順でソート
                chunks_include_prt.sort(key=lambda x: x.get_kaku_prt())

                # 出力
                out_file.write('{}\t{}\t{}\n'.format(
                    sahen_wo + verbs[0].base,  # サ変接続名詞+を+最左の動詞の基本形
                    ' '.join([chunk.get_kaku_prt() for chunk in chunks_include_prt]),  # 助詞
                    ' '.join([chunk.normalized_surface() for chunk in chunks_include_prt])  # 項
                    ))
