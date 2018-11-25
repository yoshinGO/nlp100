# "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
# という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，それ以外の単語は先頭に2文字を取り出し，
# 取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．

# 与えられた英文
seq = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

# ピリオドを削除
seq = seq.replace('.', '')

# split関数を使って与えられた英文を単語毎に分割し, リストに格納する
words = seq.split(' ')

periodic_table_list = []
for i in range(len(words)):
    if((i + 1) == 1 or (i + 1) == 5 or (i + 1) == 6 or (i + 1) == 7 \
    or (i + 1) == 8 or (i + 1) == 9 or (i + 1) == 15 or (i + 1) == 16 \
    or (i + 1) == 19):
        periodic_table_list.append(words[i][0])
    else:
        periodic_table_list.append(words[i][:2])

# リストが完成したので連想配列を辞書型で作成する
periodic_table_dict = {}
for i, word in enumerate(periodic_table_list):
    periodic_table_dict[word] = i+1

print(periodic_table_dict)
print(periodic_table_dict['Ne'])  # 10
print(periodic_table_dict['O'])  # 8
