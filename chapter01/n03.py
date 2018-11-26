
"""
"Now I need a drink, alcoholic of course, after the heavy lectures
involving quantum mechanics."という文を単語に分解し，
各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．
"""


def del_symbols(text, symbol):
    return text.replace(symbol, '')


# 与えられた英文
seq = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

# カンマを削除
seq = del_symbols(seq, ',')
# ピリオドを削除
seq = del_symbols(seq, '.')

# split関数を使って, 与えられた英文を単語毎に分割し, 配列に格納する
words = seq.split(' ')

# 単語それぞれの文字数を格納する
word_len_list = [len(word) for word in words]  # リストの宣言と同時に中身を定義

print(word_len_list)
