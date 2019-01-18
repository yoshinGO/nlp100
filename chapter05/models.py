class Morph:
    '''
    形態素クラス
    表層系(surface), 基本形(base), 品詞(pos), 品詞細分類(pos1)を
    メンバ変数に持つ
    '''
    def __init__(self, surface, base, pos, pos1):
        '''初期化'''
        self._surface = surface
        self._base = base
        self._pos = pos
        self._pos1 = pos1

    def __str__(self):
        '''オブジェクトの文字列表現'''
        return 'surface[{}]\tbase[{}]\tpos[{}]pos1[{}]'\
            .format(self._surface, self._base, self._pos, self._pos1)

    @property
    def surface(self):
        return self._surface

    @property
    def base(self):
        return self._base

    @property
    def pos(self):
        return self._pos

    @property
    def pos1(self):
        return self._pos1


class Chunk:
    '''
    文節クラス
    Morphオブジェクトのリスト(morphs), 係り先文節インデックス番号(dst),
    係り元文節番号(srcs)をメンバ変数にもつ
    '''
    def __init__(self):
        '''初期化'''
        self._morphs = []
        self._srcs = []
        self._dst = -1

    @property
    def morphs(self):
        return self._morphs

    @property
    def srcs(self):
        return self._srcs

    @property
    def dst(self):
        return self._dst

    @dst.setter
    def dst(self, v):
        self._dst = v

    def add_morph(self, v):
        self._morphs.append(v)

    def add_src(self, v):
        self._srcs.append(v)

    def __str__(self):
        '''オブジェクトの文字列表現'''
        surface = ''
        for morph in self._morphs:
            surface += morph._surface
        return '{}\tsrcs{}\tdst[{}]'.format(surface, self._srcs, self._dst)

    def normalized_surface(self):
        '''句読点を除去した表現'''
        result = ''
        for morph in self._morphs:
            if morph._pos != '記号':
                result += morph._surface
        return result

    def chk_pos(self, pos):
        '''対象の品詞が入っているかチェック
        戻り値はブーリアン型
        '''
        for morph in self._morphs:
            if morph._pos == pos:
                return True
        return False
