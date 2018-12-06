"""
各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．
確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）
"""
from sys import argv
from operator import itemgetter

if __name__ == '__main__':
    with open(argv[1], 'r') as f, open(argv[2], 'w') as g:
        # 整列したいデータをリストに格納する
        elements_list = f.readlines()
        # 3コラム目の数値でsortedするために二次元のリストにする
        list_elements = [ele.split() for ele in elements_list]
        ascending_elements = sorted(list_elements, key=itemgetter(2))
        for line in ascending_elements:
            add_elements = '\t'.join(line)
            g.write(add_elements + '\n')  # 数値の逆順で整列したものをファイルに書き出す

# sort -k 3 -t ' ' ../data/highttemp.txt
