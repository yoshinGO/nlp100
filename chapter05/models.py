class Morph:
    '''
    形態素クラス
    表層系(surface), 基本形(base), 品詞(pos), 品詞細分類(pos1)を
    メンバ変数に持つ
    '''
    def __init__(self, surface, base, pos, pos1):
        '''初期化'''
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def __str__(self):
        '''オブジェクトの文字列表現'''
        return 'surface[{}]\tbase[{}]\tpos[{}]pos1[{}]'\
            .format(self.surface, self.base, self.pos, self.pos1)


class Chunk:
    '''
    文節クラス
    Morphオブジェクトのリスト(morphs), 係り先文節インデックス番号(dst),
    係り元文節番号(srcs)をメンバ変数にもつ
    '''
    def __init__(self):
        '''初期化'''
        self.morphs = []
        self.srcs = []
        self.dst = -1

    def __str__(self):
        '''オブジェクトの文字列表現'''
        surface = ''
        for morph in self.morphs:
            surface += morph.surface
        return '{}\tsrcs{}\tdst[{}]'.format(surface, self.srcs, self.dst)
