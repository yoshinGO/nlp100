"""
各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．
確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）．
"""
from operator import itemgetter

with open('../data/hightemp.txt', 'r') as data_file:
    print(sorted([line.strip().split() for line in data_file], key=itemgetter(2)))
