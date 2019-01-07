"""
与えられた文の係り受け木を有向グラフとして可視化せよ．
可視化には，係り受け木をDOT言語に変換し，Graphvizを用いるとよい．
また，Pythonから有向グラフを直接的に可視化するには，pydotを使うとよい．
"""
import pydot_ng as pydot
from constants import PARTIAL_FNAME_PARSED
from models import Morph, Chunk
from n41 import neko_chunk


def graph_from_edges_ex(edge_list, directed=False):
    '''pydot_ng.graph_from_edges()のノード識別子への対応版

    graph_from_edges()のedge_listで指定するタプルは
    識別子とグラフ表示時のラベルが同一のため,
    ラベルが同じだが実態が異なるノードを表現することができない.
    例えば文の係り受けをグラフにする際, 文の中に同じ単語が
    複数出てくると, それらのノードが同一視されて接続されてしまう.

    この関数ではedge_listとして次の書式のタプルを受け取り,
    ラベルが同一でも識別子が異なるノードは別のものとして扱う.

    edge_list = [((識別子1,ラベル1),(識別子2,ラベル2)), ...]

    識別子はノードを識別するためのもので表示されない.
    ラベルは表示用で,同じでも識別子が異なれば別のノードになる.

    戻り値：
    pydot.Dotオブジェクト
    '''

    if directed:
        graph = pydot.Dot(graph_type='digraph')

    else:
        graph = pydot.Dot(graph_type='graph')

    for edge in edge_list:
        id1 = str(edge[0][0])
        label1 = str(edge[0][1])
        id2 = str(edge[1][0])
        label2 = str(edge[1][1])

        # ノード追加
        graph.add_node(pydot.Node(id1, label=label1))
        graph.add_node(pydot.Node(id2, label=label2))

        # エッジ追加
        graph.add_edge(pydot.Edge(id1, id2))

    return graph


if __name__ == '__main__':
    for chunks in neko_chunk(PARTIAL_FNAME_PARSED):

        # 係り先があるものを列挙
        edges = []
        for i, chunk in enumerate(chunks):
            if chunk.dst != -1:

                # 記号を除いた表層系をチェック, 空なら除外
                src_surface = chunk.normalized_surface()
                dst_surface = chunks[chunk.dst].normalized_surface()
                if src_surface != '' and dst_surface != '':
                    edges.append(((i, src_surface), (chunk.dst, dst_surface)))

        # 描画
        if len(edges) > 0:
            graph = graph_from_edges_ex(edges, directed=True)
            graph.write_png('result.png')
