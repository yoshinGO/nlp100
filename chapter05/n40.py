"""
形態素を表すクラスMorphを実装せよ
このクラスは表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をメンバ変数に持つこととする．
さらに，CaboChaの解析結果（neko.txt.cabocha）を読み込み，各文をMorphオブジェクトのリストとして表現し，3文目の形態素列を表示せよ．
"""
from constants import FNAME_PARSED
from models import Morph


def neko_morphs(fname_parsed):
    with open(fname_parsed, 'r') as file_parsed:
        morphs = []
        for line in file_parsed:

            # 1文の終了判定
            if line == 'EOS\n':
                yield morphs  # 1文の形態素解析結果が集まり次第yieldする。
                morphs = []

            else:
                # 先頭が*の行は係り受け解析結果なのでスキップ
                if line[0] == '*':
                    continue

                # 表層系はtab区切り, それ以外は','で区切りバラす
                cols = line.split('\t')  # cols[0]は表層系, cols[1]は解析結果
                res_cols = cols[1].split(',')

                # Morph作成, リストに追加
                morphs.append(Morph(
                    cols[0],  # surface
                    res_cols[6],  # base
                    res_cols[0],  # pos
                    res_cols[1],  # pos1
                ))

        raise StopIteration


if __name__ == '__main__':
    for i, morphs in enumerate(neko_morphs(FNAME_PARSED), 1):  # neko_lines(FNAME_PARSED)はgenerator
        # 3文目を表示
        if i == 3:  # 1ベースのi, 最初2回分のEOSは意味のないものであるから挙動を確認するためにi==3の時を確認
            for morph in morphs:
                print(morph)
            break
