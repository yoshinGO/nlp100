"""
各行の1列目だけを抜き出したものをcol1.txtに，
2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．
確認にはcutコマンドを用いよ
"""

with open('../tmp/col1.txt', 'w') as f, open('../tmp/col2.txt', 'w') as g, open('../data/hightemp.txt', 'r') as data_file:
    for line in data_file:
        element = line.strip().split()
        f.write(element[0] + '\n')
        g.write(element[1] + '\n')

"""
linux :
    cut -f 1 ../data/hightemp.txt > ../tmp/col1_cut.txt
    cut -f 2 ../data/hightemp.txt > ../tmp/col2_cut.txt
"""
