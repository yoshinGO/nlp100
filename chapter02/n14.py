"""
自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．
確認にはheadコマンドを用いよ．
"""
from sys import argv


denote_number = int(argv[1])
with open('../data/hightemp.txt', 'r') as data_file:
    for _ in range(denote_number):
        print(data_file.readline(), end='')  # readline関数で１行ずつ取り出す

"""
linux : head -n ../data/hightemp.txt
"""
