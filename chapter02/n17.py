"""
1列目の文字列の種類（異なる文字列の集合）を求めよ．確認にはsort, uniqコマンドを用いよ．
"""

with open('../data/hightemp.txt', 'r') as data_file:
    unique_col1_elements = set([line.strip().split()[0] for line in data_file])
    print(unique_col1_elements)

"""
linux : cut -f ../data/hightemp.txt | sort | uniq
"""
