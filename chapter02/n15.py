"""
自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．
確認にはtailコマンドを用いよ.
"""
from sys import argv


denote_number = int(argv[1])
with open('../data/hightemp.txt', 'r') as data_file:
    lines = data_file.readlines()  # list型に格納
    for line in lines[-denote_number:]:
        print(line.strip())

"""
linux : tail -3 ../data/hightemp.txt
