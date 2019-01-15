from models import Morph


def make_morphs(fname_parsed):
    '''「吾輩は猫である」の係り受け解析結果のジェネレータ

   「吾輩は猫である」の係り受け解析結果を読み込んで,
    1文ずつMorphクラスのリストを返す

    戻り値：
    1文のMorphクラスのリスト(yieldで返す)
    '''
    with open(fname_parsed) as file_parsed:
        morphs = []  # Morphクラスのリスト
        for line in file_parsed:

            # 1文の終了判定
            if line == 'EOS\n':
                yield morphs  # 1文が終了するごとにその文の形態素のリストを返し, リストの空にする.
                morphs = []

            else:
                '''係り受け解析結果の様式(lineにはこれらのうちの１行のみ入っている)
                * 1 2D 0/1 -0.764522
                吾輩	名詞,代名詞,一般,*,*,*,吾輩,ワガハイ,ワガハイ,,
                は	助詞,係助詞,*,*,*,*,は,ハ,ワ,,
                '''
                # 先頭が*の行は係り受け解析結果なのでスキップ
                if line[0] == '*':
                    continue  # 次の行へ

                # 表層系はtab区切り, それ以外は','区切りでバラす
                cols = line.split('\t')
                res_cols = cols[1].split(',')

                # Morph作成, リストmorphsに追加
                morphs.append(Morph(
                    cols[0],  # surface
                    res_cols[6],  # base
                    res_cols[0],  # pos
                    res_cols[1],  # pos1
                ))

        raise StopIteration
