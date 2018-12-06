"""
各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．
確認にはcut, uniq, sortコマンドを用いよ．
"""
from sys import argv
from collections import defaultdict


with open(argv[1]) as f:
    # 二次元のリストが生成する
    data_list = [line.strip().split() for line in f]
    # data_listは複数のリストを保持するリストであり、for文を使って一つのリストを取り出す。
    # 取り出したリストの1コラム目が必要であるからdata[0]で取得する
    col_1_elements = [data[0] for data in data_list]
    count_col1 = defaultdict(lambda: 0)  # lキーが存在していない時は0を返す
    for ele in col_1_elements:
        count_col1[ele] += 1

    for k, v in sorted(count_col1.items(), key=lambda x: -x[1]):
        print(f'{str(k)} : {str(v)}')

# cut -f 1 ../data/highttemp.txt | sort | uniq -c | sort -k1 -r
