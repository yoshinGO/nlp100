"""
40に加えて，文節を表すクラスChunkを実装せよ.
このクラスは形態素（Morphオブジェクト）のリスト（morphs），係り先文節インデックス番号（dst），
係り元文節インデックス番号のリスト（srcs）をメンバ変数に持つこととする．
さらに，入力テキストのCaboChaの解析結果を読み込み，１文をChunkオブジェクトのリストとして表現し，
8文目の文節の文字列と係り先を表示せよ．
第5章の残りの問題では，ここで作ったプログラムを活用せよ
"""
import re
from constants import FNAME_PARSED
from models import Morph, Chunk


def neko_chunk(fname_parsed):
    '''「吾輩は猫である」の係り受け解析結果のジェネレータ
    「吾輩は猫である」の係り受け解析結果を順次読み込んで,
    1文ずつChunkクラスのリストを返す

    戻り値：
    1文のChunkクラスのリスト
    '''
    with open(fname_parsed) as file_parsed:

        chunks = dict()  # idxをkeyにChunkを格納
        idx = -1

        for line in file_parsed:

            # 1文の終了判定
            if line == 'EOS\n':

                # Chunkのリストを返す
                if len(chunks) > 0:

                    # chunksをkeyでソートし, valueのみ取り出し
                    # xを与えるとx[0]を返すためkey(idxの番号順)でのソートとなる
                    sorted_tuple = sorted(chunks.items(), key=lambda x: x[0])  # sorted関数の返り値はリスト
                    yield list(zip(*sorted_tuple))[1]  # 文が終わり次第, valueのみを取り出しyieldする.
                    chunks.clear()

                else:
                    yield []
            # 先頭が*の行は係り受け解析結果なので, Chunkを作成. 文節ごとに*が存在する
            elif line[0] == '*':

                # Chunkのインデックス番号と係り先のインデックス番号取得
                cols = line.split(' ')  # 『* 0 2D 0/0 -0.764522』 この形式の行をスペース区切りでリスト化する
                idx = int(cols[1])  # 何番目の文節かの情報が格納されている
                dst = int(re.search(r'(.*?)D', cols[2]).group(1))  # 係り先の文節の番号

                # Chunkを生成(なければ)し, 係り先のインデックス番号セット
                if idx not in chunks:
                    chunks[idx] = Chunk()
                chunks[idx].dst = dst

                # 係り先のChunkを生成し, 係り元インデックス番号追加
                if dst != -1:  # dst = -1 というのは係り先の文節が存在しない状態
                    if dst not in chunks:
                        chunks[dst] = Chunk()
                    chunks[dst].srcs.append(idx)  # chunksオブジェクトのsrcsの型はリスト
                    # 『この文節』の【係り先の文節の係り元の番号】に『係り元であるこの文節のidx』を入れる

            # それ以外の行は形態素解析結果なので, Morphを作りChunkに追加
            else:

                # 表層系はtab区切り, それ以外は','区切りでバラす
                # 『吾輩	名詞,代名詞,一般,*,*,*,吾輩,ワガハイ,ワガハイ,,』
                cols = line.split('\t')  # [吾輩,その他の情報がカンマ区切りで格納されたもの]という形式になる
                res_cols = cols[1].split(',')

                # Morph作成, リストに追加
                # idxはelifの処理の段階で獲得しており, 冒頭のidx=-1は更新済みである.
                chunks[idx].morphs.append(
                    Morph(
                        cols[0],  # surface
                        res_cols[6],  # base
                        res_cols[0],  # pos
                        res_cols[1],  # pos1
                    )
                )
        raise StopIteration


if __name__ == '__main__':
    # 1文ずつリスト作成
    for i, chunks in enumerate(neko_chunk(FNAME_PARSED), 1):

        # 8文目を表示
        if i == 8:
            for j, chunk in enumerate(chunks):
                print(f'[{j}]{chunk}')
            break
