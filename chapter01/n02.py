"""
「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ
"""

word = "".join([c1 + c2 for c1, c2 in zip('パトカー', 'タクシー')])

print(word)
