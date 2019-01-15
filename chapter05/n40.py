"""
形態素を表すクラスMorphを実装せよ．
このクラスは表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をメンバ変数に持つこととする．
さらに，CaboChaの解析結果（neko.txt.cabocha）を読み込み，各文をMorphオブジェクトのリストとして表現し，3文目の形態素列を表示せよ
"""
from utils import make_morphs
from constants import FNAME_PARSED


if __name__ == '__main__':
    for i, morphs in enumerate(make_morphs(FNAME_PARSED), 1):
        # 3文目を表示
        if i == 3:
            for morph in morphs:
                print(morph)
            break
