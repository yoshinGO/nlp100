# 与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．
# この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．


def make_n_gram(seq, n, unit):
    if unit == 'word':
        seq = seq.split()
    return [list(seq[i:i + n]) for i in range(len(seq) - n + 1)]


if __name__ == "__main__":
    example_sentence = 'I am an NLPer'
    print('word bi-gram: ', make_n_gram(example_sentence, 2, 'word'))
    print('character bi-gram:', make_n_gram(example_sentence, 2, 'char'))
