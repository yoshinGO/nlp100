from models import Morph
from models import Chunk
import re


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


def make_chunks(fname_parsed):
        '''ジェネレータ, 戻り値は1文のChunkクラスのリスト'''

        '''係り受け解析結果の様式(lineにはこれらのうちの１行のみ入っている)
        * 1 2D 0/1 -0.764522
        吾輩	名詞,代名詞,一般,*,*,*,吾輩,ワガハイ,ワガハイ,,
        は	助詞,係助詞,*,*,*,*,は,ハ,ワ,,
        '''
        with open(fname_parsed) as file_parsed:
            chunks = dict()  # idx: Chunk という辞書
            idx = -1

            for line in file_parsed:
                # 一文の終了判定
                # 1文の終了判定
                if line == 'EOS\n':

                    # Chunkのリストを返す
                    if len(chunks) > 0:
                        # chunksにChunkオブジェクトを追加する際にバラバラな順番で追加したため、順番通りに要素は並んでいない
                        # chunksをkeyでソートし、valueのみ取り出し
                        sorted_tuple = sorted(chunks.items(), key=lambda x: x[0])  # keyでソート
                        yield list(zip(*sorted_tuple))[1]  # valueのみ(Chunkオブジェクトのみ)取り出せる(これらのChunkオブジェクトは順番通りになっている)
                        chunks.clear()

                    else:
                        yield []

                elif line[0] == '*':

                    # Chunkのインデックス番号と係り先のインデックス番号を取得
                    '''文頭が'*'の行の様式
                    * 1 2D 0/1 -0.764522
                    '''
                    cols = line.split(' ')
                    idx = int(cols[1])  # その文節自体のインデックス番号を取得
                    dst = int(re.search(r'(.*?)D', cols[2]).group(1))  # 正規表現を使ってその文節の係り先の文節のインデックス番号を取得

                    if idx not in chunks:  # 辞書chunksのkeyにidxがないならばChunkを生成し係り先のインデックス番号を追加
                        chunks[idx] = Chunk()
                    chunks[idx].dst = dst

                    if dst != -1:  # 係り先のChunkを生成し, その係り元の番号として今処理の対象となっている文節のインデックス番号を追加
                        if dst not in chunks:
                            chunks[dst] = Chunk()
                        chunks[dst].srcs.append(idx)

                # '*'でもEOS\nでもない行は形態素解析結果なので, Morphを作りchunksに追加
                else:
                    '''形態素解析結果の行の様式
                    吾輩	名詞,代名詞,一般,*,*,*,吾輩,ワガハイ,ワガハイ,,
                    '''
                    # 表層系はtab区切り, それ以外は','で区切る
                    cols = line.split('\t')
                    res_cols = cols[1].split(',')

                    # Morph作成, Chunkオブジェクトのインスタンス変数morphsに生成したMorphを追加
                    chunks[idx].morphs.append(
                        Morph(
                            cols[0],  # surface
                            res_cols[6],  # base
                            res_cols[0],  # pos
                            res_cols[1],  # pos1
                        )
                    )
            raise StopIteration
