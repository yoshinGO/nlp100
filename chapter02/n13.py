"""
12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目を
タブ区切りで並べたテキストファイルを作成せよ．確認にはpasteコマンドを用いよ
"""

from sys import argv


with open(argv[1], 'r') as f, open(argv[2], 'r') as g, open(argv[3], 'w') as h:
    elements1 = f.read().strip().split()  # 要素をリストで管理
    elements2 = g.read().strip().split()  # 要素をリストで管理
    # ファイルへの書き込み
    for ele1, ele2 in zip(elements1, elements2):
        h.write(f'{ele1}\t{ele2}\n')

#  paste col1.txt col2.txt
