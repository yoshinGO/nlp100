import requests

URL = "http://www.cl.ecei.tohoku.ac.jp/nlp100/data/neko.txt"

# 本文を抜き出す
response = requests.get(URL)
response.encoding = response.apparent_encoding  # SHIFT_JIS

# 確認
print(response.text)
