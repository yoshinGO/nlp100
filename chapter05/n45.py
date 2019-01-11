"""
今回用いている文章をコーパスと見なし，日本語の述語が取りうる格を調査したい.
動詞を述語，動詞に係っている文節の助詞を格と考え，述語と格をタブ区切り形式で出力せよ.
ただし，出力は以下の仕様を満たすようにせよ．

動詞を含む文節において，最左の動詞の基本形を述語とする
述語に係る助詞を格とする
述語に係る助詞（文節）が複数あるときは，すべての助詞をスペース区切りで辞書順に並べる
「吾輩はここで始めて人間というものを見た」という例文（neko.txt.cabochaの8文目）を考える.
この文は「始める」と「見る」の２つの動詞を含み，「始める」に係る文節は「ここで」，
「見る」に係る文節は「吾輩は」と「ものを」と解析された場合は，次のような出力になるはずである．

始める  で
見る    は を
このプログラムの出力をファイルに保存し，以下の事項をUNIXコマンドを用いて確認せよ．

コーパス中で頻出する述語と格パターンの組み合わせ
「する」「見る」「与える」という動詞の格パターン（コーパス中で出現頻度の高い順に並べよ）
"""
from constants import FNAME_PARSED, FNAME_RESULT
from models import Morph, Chunk
from n41 import neko_chunk

if __name__ == '__main__':
    with open(FNAME_RESULT, mode='w') as out_file:
        for chunks in neko_chunk(FNAME_PARSED):

            for chunk in chunks:

                # 動詞を含むかチェック
                verbs = chunk.get_morphs_by_pos('動詞')
                if len(verbs) < 1:
                    continue

                # 係り元の列挙
                prts = []
                for src_number in chunk.srcs:

                    # 助詞を検索
                    prts_in_chunk = chunks[src_number].get_morphs_by_pos('助詞')
                    if len(prts_in_chunk) > 1:

                        # Chunk内に2つ以上助詞がある場合は, 格助詞を優先
                        kaku_prts = chunks[src_number].get_morphs_by_pos('助詞', '格助詞')
                        if len(kaku_prts) > 0:
                            prts_in_chunk = kaku_prts

                    if len(prts_in_chunk) > 0:
                        prts.append(prts_in_chunk[-1])  # 抽出する助詞はChunk当たり最後の1つ

                if len(prts) < 1:
                    continue

                # 出力
                out_file.write('{}\t{}\n'.format(verbs[0].base, ' '.join(sorted(prt.surface for prt in prts))))
                # 最左の動詞の基本形, 助詞は辞書順
