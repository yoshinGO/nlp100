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
        return f'{surface}\tsrcs{self.srcs}\tdst[{self.dst}]'  # 吾輩は  srcs[]  dst[5]

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

    def chk_pos(self, pos):
        '''指定した品詞(pos)を含むかチェックする

        戻り値：
        品詞(pos)を含む場合はTrue
        '''
        for morph in self.morphs:
            if morph.pos == pos:
                return True
        return False

    def get_morphs_by_pos(self, pos, pos1=''):
        '''指定した品詞(pos), 品詞細分類1(pos1)の形態素のリストを返す
        pos1の指定がない場合はposのみで判定する

        戻り値：
        形態素(morph)のリスト, 該当形態素がない場合は空のリスト
        '''
        if len(pos1) > 0:
            return [res for res in self.morphs if (res.pos == res) and (res.pos1 == pos1)]
        else:
            return [res for res in self.morphs if res.pos == pos]

    # 助詞は英語でpostpositional particle
    def get_kaku_prt(self):
        '''助詞を1つ返す
        複数ある場合は格助詞を優先し, 最後の助詞を返す.

        戻り値：
        助詞, ない場合は空文字列
        '''
        prts = self.get_morphs_by_pos('助詞')
        if len(prts) > 1:

            # 2つ以上ある場合は, 格助詞を優先
            kaku_prts = self.get_morphs_by_pos('助詞', '格助詞')
            if len(kaku_prts) > 0:
                prts = kaku_prts

        if len(prts) > 0:
            return prts[-1].surface  # 最後を返す
        else:
            return ''
