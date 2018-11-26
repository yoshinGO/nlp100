"""
スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，
それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．
ただし，長さが４以下の単語は並び替えないこととする．
適当な英語の文（例えば"I couldn't believe that I could actually understand
what I was reading : the phenomenal power of the human mind ."）を与え，
その実行結果を確認せよ．
"""

import random

"""
# 文字の順番をバラバラにする
def element_shuffle(ele):
    ele_list = list(ele)  # 渡された単語が一文字ずつリストに格納する
    tmp = list(ele)  # shuffle後に元のリストの情報が必要になるため
    random.shuffle(ele_list)  # ele_listは要素がバラバラになった
    orign_head_index = ele_list.index(tmp[0])  # 元のele_listの先頭の文字がshuffle後にどこにいるか
    orign_end_index = ele_list.index(tmp[len(ele_list)-1])  # 元のele_listの末尾の文字がshuffle後にどこにいるか
    ele_list[0], ele_list[orign_head_index] = ele_list[orign_head_index], ele_list[0]
    ele_list[len(ele_list)-1], ele_list[orign_end_index] = ele_list[orign_end_index], ele_list[len(ele_list)-1]
    shuffle_ele = "".join(ele_list)
    return shuffle_ele
"""


def element_shuffle(ele):
    # 0番目と最後だけ抜く
    middle_characters = list(ele[1:-1])
    random.shuffle(middle_characters)
    middle_string = "".join(middle_characters)
    return ele[0] + middle_string + ele[-1]


if __name__ == "__main__":

    seq = "I couldn't believe that I could actually understandwhat I was reading : the phenomenal power of the human mind ."

    words = seq.split()
    shufflewords_list = []  # バラバラになった単語を格納s流
    # 5字以上の単語の語順をバラバラにする
    for i, word in enumerate(words):
        if len(word) > 4:
            shufflewords_list.append(element_shuffle(word))
        else:
            shufflewords_list.append(word)

    print(seq)
    new_seq = " ".join(shufflewords_list)
    print("文字の順番をバラバラにしました。")
    print(new_seq)
