"""
タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ
"""
from sys import argv


# text内にある特定の文字を置換
def replace_symbols(text, symbols):
    # symbolsは文字列のリスト
    for symbol in symbols:
        text = text.replace(symbol, ' ')
    return text


if __name__ == '__main__':
    with open(argv[1]) as f:
        print(replace_symbols(f.read(), '\t'))

# cat ../data/highttemp.txt | tr '\t' ' '
