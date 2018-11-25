# 与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．
#
# 英小文字ならば(219 - 文字コード)の文字に置換
# その他の文字はそのまま出力
# この関数を用い，英語のメッセージを暗号化・復号化せよ．


import re


def cipher(str):
    p = re.compile("[a-z]")
    code = []
    for ch in str:
        code.append(chr(219 - ord(ch)) if p.match(ch) else ch)
    return "".join(code)


print(cipher("this is a test message of the question n08."))
print(cipher("gsrh rh z gvhg nvhhztv lu gsv jfvhgrlm m08."))
