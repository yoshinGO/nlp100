"""
タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ
"""
from sys import argv


if __name__ == '__main__':
    with open(argv[1]) as f:
        for line in f:
            print(line.replace('\t', ' '))

# cat ../data/highttemp.txt | tr '\t' ' '
