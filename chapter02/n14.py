"""
自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．
確認にはheadコマンドを用いよ
"""
from sys import argv


if __name__ == '__main__':
    n = int(argv[1])
    with open(argv[2], 'r') as f:
        while n > 0:  # n回繰り返す
            print(f.readline(), end='')  # readline関数で１行ずつ取り出す
            n -= 1

# head -n 5 ../tmp/merge_text.txt
