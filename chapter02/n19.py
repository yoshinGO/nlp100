"""
各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．
確認にはcut, uniq, sortコマンドを用いよ
"""
from collections import defaultdict

with open('../data/hightemp.txt', 'r') as data_file:
    col1_elements = [line.strip().split()[0] for line in data_file]

    count_col1 = defaultdict(lambda: 0)
    for ele in col1_elements:
        count_col1[ele] += 1

    for k, v in sorted(count_col1.items(), key=lambda x: -x[1]):
        print(f'{str(k)} : {str(v)}')

"""
linux : cut -f 1 ../data/highttemp.txt | sort | uniq -c | sort -k1 -r
"""
