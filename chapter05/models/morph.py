class Morph:
    '''
    形態素クラス
    表層系(surface), 基本形(base), 品詞(pos), 品詞細分類(pos1)を
    メンバー変数に持つ
    '''
    def __init__(self, surface, base, pos, pos1):
        '''初期化'''
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def __str__(self):
        '''オブジェクトの文字列表現'''
        return f'surface[{self.surface}]\tbase[{self.base}]\tpos[{self.pos}]\tpos1[{self.pos1}]'
