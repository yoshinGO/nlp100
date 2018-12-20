"""
スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，
それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．
ただし，長さが４以下の単語は並び替えないこととする．
適当な英語の文（例えば'I couldn't believe that I could actually understand
what I was reading : the phenomenal power of the human mind .'）を与え，
その実行結果を確認せよ
"""

import random


def del_symbols(seq, symbols):
    for symbol in symbols:
        seq = seq.replace(symbol, '')
    return seq


# 先頭と末尾を除いた文字列の順序をランダムに入れ替える
def shuffle_word(word):
    random_center_sentence = ''.join(random.sample(word[1:len(word)-1], len(word)-2))
    return f'{word[0]}{random_center_sentence}{word[-1]} '


if __name__ == '__main__':
    example_sentence = 'I couldn\'t believe that I could actually understand \
    what I was reading : the phenomenal power of the human mind .'

    shuffle_word_list = []
    for word in example_sentence.split():
        if len(word) > 4:
            shuffle_word_list.append(shuffle_word(word))
        else:
            shuffle_word_list.append(word)

    shuffle_centence = ' '.join(shuffle_word_list)
    print(shuffle_centence)
