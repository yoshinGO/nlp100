"""
タブ1文字につきスペース1文字に置換せよ．
確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ
"""

with open('../data/hightemp.txt', 'r') as data_file:
    for line in data_file:
        print(line.strip().replace('\t', ' '))

"""
linux : cat ../data/hightemp.txt | tr '\t' ' '
"""
