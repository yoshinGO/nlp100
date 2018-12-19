"""
自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．
同様の処理をsplitコマンドで実現せよ
"""
from sys import argv
import math

split_size = int(argv[1])  # 分割ファイルの個数

with open(argv[2], 'r') as f:
    # １行ごとにリストに格納
    lines = f.readlines()
    # リストの要素数 (行数)
    lines_length = len(lines)
    # 均等に分割するために分割ファイル一つあたりの行数を求める
    lines_length_per_file = math.ceil(lines_length/split_size)  # 切り上げ

    line_index = 0
    for i in range(split_size):
        with open(argv[3]+str(i)+'.txt', 'w') as g:
            file = lines[line_index:line_index+lines_length_per_file]
            g.writelines(file)
            line_index += lines_length_per_file
