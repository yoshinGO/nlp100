"""
各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．
確認にはcut, uniq, sortコマンドを用いよ．
"""
from sys import argv
from collections import defaultdict


with open(argv[1]) as f:
    # 取り出した行をリスト化し, その1コラム目が必要であるから[0]で取得する
    data_list = [line.strip().split()[0] for line in f]

    count_col1 = defaultdict(lambda: 0)  # lキーが存在していない時は0を返す
    for ele in data_list:
        count_col1[ele] += 1

    for k, v in sorted(count_col1.items(), key=lambda x: -x[1]):
        print(f'{str(k)} : {str(v)}')

# cut -f 1 ../data/highttemp.txt | sort | uniq -c | sort -k1 -r
