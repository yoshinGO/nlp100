"""
行数をカウントせよ．確認にはwcコマンドを用いよ
"""
from sys import argv


def count_len():
    with open(argv[1]) as f:
        counts = sum(1 for line in f)
    return counts


if __name__ == '__main__':
    line_counts = count_len()
    print(line_counts)
