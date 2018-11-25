# 引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．
# さらに，x=12, y="気温", z=22.4として，実行結果を確認せよ


def template_sentence(x, y, z):
    return ("{time}時の{temperature}は{value}".format(time=x, temperature=y, value=z))


print(template_sentence(x=12, y="気温", z=22.4))
