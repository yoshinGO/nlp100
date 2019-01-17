"""
40に加えて，文節を表すクラスChunkを実装せよ．
このクラスは形態素（Morphオブジェクト）のリスト（morphs），係り先文節インデックス番号（dst），
係り元文節インデックス番号のリスト（srcs）をメンバ変数に持つこととする．
さらに，入力テキストのCaboChaの解析結果を読み込み，
１文をChunkオブジェクトのリストとして表現し，8文目の文節の文字列と係り先を表示せよ．
第5章の残りの問題では，ここで作ったプログラムを活用せよ
"""
from utils import make_chunks
from constants import FNAME_PARSED

if __name__ == '__main__':
    for i, chunks in enumerate(make_chunks(FNAME_PARSED), 1):

        # 8文目を表示
        if i == 8:
            for j, chunk in enumerate(chunks):
                print('[{}]{}'.format(j, chunk))
