"""
12で作ったcol1.txtとcol2.txtを結合し，
元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．
確認にはpasteコマンドを用いよ．
"""

with open('../tmp/col1.txt', 'r') as col1_file, open('../tmp/col2.txt', 'r') as col2_file, open('../tmp/merge.txt', 'w') as merge_file:
    col1_elements = col1_file.read().strip().split()  # 要素をリストに格納
    col2_elements = col2_file.read().strip().split()  # 要素をリストに格納
    # ファイルへの書き込み
    for col1, col2 in zip(col1_elements, col2_elements):
        merge_file.write(f'{col1}\t{col2}\n')

"""
linux : paste ../tmp/col1.txt ../tmp/col2.txt
"""
