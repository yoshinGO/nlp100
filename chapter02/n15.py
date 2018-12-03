"""
自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．
確認にはtailコマンドを用いよ
"""
from sys import argv


n = int(argv[1])  # 表示する行数

with open(argv[2], 'r') as f:
    lines = f.readlines()
    for line in lines[-n:]:  # スライシングで後ろの要素を取り出す
        print(line.strip())  # エスケープ文字を処理して表示

# tail -3 hoge.txt
