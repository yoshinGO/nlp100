# "paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，
# XとYの和集合，積集合，差集合を求めよ．さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ.


# n-gramを生成する関数, 単語にも文字にも対応
def make_n_gram(seq, n, unit):
    if unit == "word":
        seq = seq.split()
    elif unit == "char":
        seq = seq
    return [list(seq[i:i + n]) for i in range(len(seq) - n + 1)]


# # 重複が存在するかを確認できる関数
# def is_unique(seq):
#     return len(seq) == len(set(seq))


# 引数として与えられたリストを, 順序を保持したまま重複を取り除く関数
def get_unique_list(list):
    result = []
    for ele in list:
        if ele not in result:
            result.append(ele)
    return result


# 引く数として与えられた２つのリストの和集合を求める
def union_two_list(list1, list2):
    result = list1
    for ele in list2:
        if ele not in result:
            result.append(ele)
    return result


# 引く数として与えられた２つのリストの積集合を求める
def intersection_two_list(list1, list2):
    result = []
    for ele in list1:
        if ele in list2:
            result.append(ele)
    for ele in list2:
        if ele not in result:
            result.append(ele)
    return result


# 引く数として与えられた２つのリストの差集合を求める
# 和集合から積集合の要素を排除する
def difference_set_two_list(list1, list2):
    result = []
    union = union_two_list(list1, list2)
    intersection = intersection_two_list(list1, list2)
    for ele in union:
        if ele not in intersection:
            result.append(ele)
    return result


# main関数
if __name__ == "__main__":
    seq1 = "paraparaparadise"
    seq2 = "paragraph"
    # s1, s2それぞれの文字bi-gramを生成
    seq1_bi_gram = make_n_gram(seq1, 2, "char")
    seq1_unique_bi_gram = get_unique_list(seq1_bi_gram)
    X = seq1_unique_bi_gram

    seq2_bi_gram = make_n_gram(seq2, 2, "char")
    seq2_unique_bi_gram = get_unique_list(seq2_bi_gram)
    Y = seq2_unique_bi_gram

    print("X : ", X)
    print("Y : ", Y)
    print("XとYの和集合 : ", union_two_list(X, Y))
    print("XとYの積集合 : ", intersection_two_list(X, Y))
    print("XとYの差集合 : ", difference_set_two_list(X, Y))
