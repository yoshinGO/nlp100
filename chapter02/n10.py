"""
行数をカウントせよ．確認にはwcコマンドを用いよ
"""

with open('../data/hightemp.txt', 'r') as data_file:
    print(sum(1 for line in data_file))

"""
linux : wc -l ../data/hightemp
"""
