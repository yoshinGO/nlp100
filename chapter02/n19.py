"""
各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．
確認にはcut, uniq, sortコマンドを用いよ．
"""
from sys import argv


with open(argv[1]) as f:
    data_of_list = [line.strip().split() for line in f]
    col_1_elemtents = [col[0] for col in data_of_list]
    count_col1 = {}
    for ele in col_1_elemtents:
        if ele in count_col1:
            count_col1[ele] += 1
        else:
            count_col1[ele] = 1

    for k, v in sorted(count_col1.items(), key=lambda x: -x[1]):
        print(str(k) + ": " + str(v))

# cut -f 1 ../data/highttemp.txt | sort | uniq -c | sort -k1 -r
