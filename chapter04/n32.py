'''
動詞の原形をすべて抽出せよ.
'''
from constants import FNAME_PARSED
from n30 import neko_lines

if __name__ == '__main__':
    # lineには一文の形態素のリストが格納されている.
    for line in neko_lines(FNAME_PARSED):
        # morphemeには1つの形態素の解析結果が格納されている.
        for morpheme in line:
            if morpheme['pos'] == '動詞':
                print(morpheme['base'])
