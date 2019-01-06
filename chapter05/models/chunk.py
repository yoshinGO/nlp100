class Chunk:
    '''
    文節クラス
    形態素(Morphオブジェクト)のリスト(morphs), 係り先文節インデックス番号(dst),
    係り元文節インデックス番号のリスト(srcs)をメンバー変数に持つ
    '''

    def __init__(self):
        '''初期化'''
        self.morphs = []  # 1文節の形態素解析結果が格納されているリスト
        self.srcs = []
        self.dst = -1

    def __str__(self):
        '''オブジェクトの文字列表現'''
        surface = ''
        '''
        morphsには一文節『吾輩は』の形態素解析結果の
        『吾輩	名詞,代名詞,一般,*,*,*,吾輩,ワガハイ,ワガハイ,,』と
        『は	助詞,係助詞,*,*,*,*,は,ハ,ワ,,』が入っている
        '''
        for morph in self.morphs:
            surface += morph.surface  # 『吾輩』と『は』を足し合わせて『吾輩は』という一文節が完成する.
        return f'{surface}\tsrcs{self.srcs}\tdst[{self.dst}]'  # [0]吾輩は	srcs[]	dst[5]

    def normalized_surface(self):
        '''句読点などの記号をのぞいた表層系

        * 2 -1D 0/2 0.000000
        猫	名詞,一般,*,*,*,*,猫,ネコ,ネコ,,
        で	助動詞,*,*,*,特殊・ダ,連用形,だ,デ,デ,,
        ある	助動詞,*,*,*,五段・ラ行アル,基本形,ある,アル,アル,,
        。	記号,句点,*,*,*,*,。,。,。,,
        上記のような文節が存在しており, 句読点を無視する関数
        '''
        result = ''
        for morph in self.morphs:
            if morph.pos != '記号':
                result += morph.surface
        return result
