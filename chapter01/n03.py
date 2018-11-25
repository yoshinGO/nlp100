# "Now I need a drink, alcoholic of course, after the heavy lectures
# involving quantum mechanics."という文を単語に分解し，
# 各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．

# 与えられた英文
seq = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

# カンマを削除
seq = seq.replace(',', '')
# ピリオドを削除
seq = seq.replace('.', '')

# # split関数を使って, 与えられた英文を単語毎に分割し, 配列に格納する
words = seq.split(' ')

word_cnt_list = []

for i in range(len(words)):
    word = words[i]
    word_cnt = len(word)
    word_cnt_list.append(word_cnt)

print(word_cnt_list)
