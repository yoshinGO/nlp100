"""
'paraparaparadise'と'paragraph'に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，
XとYの和集合，積集合，差集合を求めよ．
さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ
"""


#  n-gramをセット型で生成
def make_n_gram(seq, n, unit):
    if unit == 'word':
        seq = seq.split()
    return set((seq[i:(i+n)]) for i in range(len(seq) - n + 1))


# 和集合を求める
def union_two_set(x, y):
    return x | y


# 積集合を求める
def intersection_two_set(x, y):
    return x & y


# 差集合を求める
def difference_two_set(x, y):
    return x - y


if __name__ == '__main__':
    seq1 = 'paraparaparadise'
    seq2 = 'paragraph'
    # seq1, seq2のそれぞれの文字bi-gramを生成
    X = make_n_gram(seq1, 2, 'char')
    Y = make_n_gram(seq2, 2, 'char')
    print(f'X：{X}')
    print(f'Y：{Y}')
    print(f'XとYの和集合：{union_two_set(X, Y)}')
    print(f'XとYの積集合：{intersection_two_set(X, Y)}')
    print(f'XとYの差集合：{difference_two_set(X, Y)}')
    print('Xにseは含まれているか：', 'se' in X)
    print('Yにseは含まれているか：', 'se' in Y)
