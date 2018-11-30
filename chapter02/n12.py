"""
各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ
"""
from sys import argv


if __name__ == '__main__':
    with open(argv[1], 'w') as f, open(argv[2], 'w') as g:
        for line in open(argv[3]):
            element = line.split()
            f.write(element[0] + '\n')
            g.write(element[1] + '\n')
"""
cut -f 1 ../data/highttemp.txt > col1_cut.txt
cut -f 2 ../data/highttemp.txt > col2_cut.txt
"""
