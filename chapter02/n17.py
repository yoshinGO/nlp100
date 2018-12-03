"""
1列目の文字列の種類（異なる文字列の集合）を求めよ．確認にはsort, uniqコマンドを用いよ
"""
from sys import argv

if __name__ == '__main__':
    with open(argv[1], 'r') as f:
        elements = f.readlines()
        unique_ele = set(elements)
        print(unique_ele)

# cat ../tmpcol1.txt | sort | uniq
