"""
今回用いている文章をコーパスと見なし，日本語の述語が取りうる格を調査したい．
動詞を述語，動詞に係っている文節の助詞を格と考え，述語と格をタブ区切り形式で出力せよ．
ただし，出力は以下の仕様を満たすようにせよ．

動詞を含む文節において，最左の動詞の基本形を述語とする
述語に係る助詞を格とする
述語に係る助詞（文節）が複数あるときは，すべての助詞をスペース区切りで辞書順に並べる
「吾輩はここで始めて人間というものを見た」という例文（neko.txt.cabochaの8文目）を考える．
この文は「始める」と「見る」の２つの動詞を含み，「始める」に係る文節は「ここで」，
「見る」に係る文節は「吾輩は」と「ものを」と解析された場合は，次のような出力になるはずである．

始める  で
見る    は を
このプログラムの出力をファイルに保存し，以下の事項をUNIXコマンドを用いて確認せよ．

コーパス中で頻出する述語と格パターンの組み合わせ
「する」「見る」「与える」という動詞の格パターン（コーパス中で出現頻度の高い順に並べよ）
"""
from utils import make_chunks
from constants import FNAME_PARSED

if __name__ == '__main__':
    with open('result_n45.txt', mode='w') as out_file:
        for chunks in make_chunks(FNAME_PARSED):
            for chunk in chunks:
                verbs = chunk.get_by_pos('動詞')
                if len(verbs) < 1:
                    continue
                # 文節内(chunk)に動詞がある状態
                prts = []
                for src_number in chunk.srcs:
                    prt = chunks[src_number].get_by_pos('助詞')
                    if len(prt) > 0:
                        prts.append(prt[0].surface)
                    else:
                        continue

                if len(prts) < 1:
                    continue

                out_file.write('{}\t{}\n'.format(
                    verbs[0].base,
                    ' '.join(prts)
                ))
