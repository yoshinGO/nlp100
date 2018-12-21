"""
自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．
同様の処理をsplitコマンドで実現せよ
"""
from sys import argv
import math

split_size = int(argv[1])  # 分割ファイルの個数

with open('../data/hightemp.txt', 'r') as data_file:
    lines = data_file.readlines()  # １行毎にリストに格納
    lines_length_per_file = math.ceil(len(lines)/split_size)  # 切り上げ

    line_index = 0
    for i in range(split_size):
        with open(f'../tmp/splited_file{i}.txt', 'w') as output_file:
            output_file.writelines(lines[line_index:line_index+lines_length_per_file])
            line_index += lines_length_per_file

"""
linux : split -l 3 ../data/hightemp
上記のlinuxコマンドは-lで指定した行数ずつに分割する処理を行う。（上記の例では３行ずつ）
当スクリプト（n16.py）はコマンドライン引数で指定した個数に分割する処理を行う。
"""
