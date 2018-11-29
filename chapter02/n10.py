"""
行数をカウントせよ．確認にはwcコマンドを用いよ
"""
from sys import argv


def count_len():
    with open(argv[1]) as f:
        return sum(1 for line in f)


if __name__ == '__main__':
    print(count_len())
