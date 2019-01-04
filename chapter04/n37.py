"""
出現頻度が高い10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ.
"""
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from collections import defaultdict
from constants import FNAME_PARSED
from n30 import neko_lines

if __name__ == '__main__':
    word_count = defaultdict(lambda: 0)
    for morphemes in neko_lines(FNAME_PARSED):
        for morpheme in morphemes:
            if morpheme['pos'] == '名詞':
                word_count[morpheme['surface']] += 1

    # 頻度上位の10語取得
    size = 10
    top_of_word_count = dict(sorted(word_count.items(), key=lambda x: -x[-1])[:size])
    top_words = top_of_word_count.keys()
    top_counts = top_of_word_count.values()

    # グラフで使うフォント情報(デフォルトのままでは日本語が表示できない)
    fp = FontProperties(
        fname='/usr/share/fonts/truetype/takao-gothic/TakaoGothic.ttf'
    )

    plt.bar(
        range(0, size),  # x軸の値(0,1,2...9)
        top_words,  # それに対応するラベル
        align='center'  # x軸における棒グラフの表示位置
    )

    # x軸のラベルの指定
    plt.xticks(
        range(0, size),  # xの値(0,1,2...9)
        top_words,  # それに対応するラベル
        fontproperties=fp  # 使うフォント情報
    )

    # x軸の値の範囲の調整
    plt.xlim(
        xmin=-1, xmax=size  # -1~10
    )

    # グラフのタイトル, ラベル指定
    plt.title(
        '37. 頻度上位10語',  # タイトル
        fontproperties=fp
    )

    plt.xlabel(
        '出現頻度が高い10語',  # x軸ラベル
        fontproperties=fp  # 使うフォント情報
    )

    # グリッドを表示
    plt.grid(axis='y')

    # 表示
    plt.show()
