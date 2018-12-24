"""
テンプレートの内容を利用し，国旗画像のURLを取得せよ．
"""
import re
import json
import urllib.parse
import urllib.request


def remove_markup(target):
    '''マークアップの除去
    強調マークアップを除去する

    引数：
    target -- 対象の文字列
    戻り値：
    強調マークアップを除去した文字列
    '''
    # 強調マークアップの除去
    markup_pattern = re.compile(r'''
        (\'{2,5})  # 2~5個の'（マークアップの開始）
        (.*?)  # 任意の1文字以上（対象の文字列）
        (\1)  # 1番目のキャプチャと同じ（マークアップの終了）
        ''', re.MULTILINE + re.VERBOSE)
    target = markup_pattern.sub(r'\2', target)

    return target


def remove_internallinks(target):
    '''内部リンクの除去
    内部リンクを除去する

    引数：
    target -- 対象の文字列
    戻り値：
    内部リンクを除去した文字列
    '''
    # 内部リンクの削除
    internallinks_pattern = re.compile(r'''
        \[\[      # '[['（マークアップの開始）
        (?:      # キャプチャ対象外のグループ開始
            [^|]*?  # '|'以外の文字が0文字以上, 非貪欲
            \|      # '|'
        )?      # グループ終了, このグループが0または1回出現
        ([^|]*?)  # キャプチャ対象, '|'以外が0文字以上, 非貪欲（表示対象の文字列）
        \]\]
        ''', re.MULTILINE + re.VERBOSE)
    target = internallinks_pattern.sub(r'\1', target)

    return target


def remove_media(target):
    # Template:Langの除去        {{lang|言語タグ|文字列}}
    pattern = re.compile(r'''
        \{\{lang    # '{{lang'（マークアップの開始）
        (?:         # キャプチャ対象外のグループ開始
            [^|]*?  # '|'以外の文字が0文字以上、非貪欲
            \|      # '|'
        )*?         # グループ終了、このグループが0以上出現、非貪欲
        ([^|]*?)    # キャプチャ対象、'|'以外が0文字以上、非貪欲（表示対象の文字列）
        \}\}        # '}}'（マークアップの終了）
        ''', re.MULTILINE + re.VERBOSE)
    target = pattern.sub(r'\1', target)

    # 外部リンクの除去  [http://xxxx] 、[http://xxx xxx]
    pattern = re.compile(r'''
        \[http:\/\/ # '[http://'（マークアップの開始）
        (?:         # キャプチャ対象外のグループ開始
            [^\s]*? # 空白以外の文字が0文字以上、非貪欲
            \s      # 空白
        )?          # グループ終了、このグループが0か1出現
        ([^]]*?)    # キャプチャ対象、']'以外が0文字以上、非貪欲（表示対象の文字列）
        \]          # ']'（マークアップの終了）
        ''', re.MULTILINE + re.VERBOSE)
    target = pattern.sub(r'\1', target)

    # <br>、<ref>の除去
    pattern = re.compile(r'''
        <           # '<'（マークアップの開始）
        \/?         # '/'が0か1出現（終了タグの場合は/がある）
        [br|ref]    # 'br'か'ref'
        [^>]*?      # '>'以外が0文字以上、非貪欲
        >           # '>'（マークアップの終了）
        ''', re.MULTILINE + re.VERBOSE)
    target = pattern.sub('', target)

    return target


# 基礎情報テンプレートの抽出条件のコンパイル
extract_pattern = re.compile(r'''
    ^\{\{基礎情報.*?$  # '{{基礎情報'で始まる行
    (.*?)  # キャプチャ対象, 任意の0文字以上, 非貪欲
    ^\}\}$  # '}}'の行
    ''', re.MULTILINE + re.VERBOSE + re.DOTALL)

# 抽出結果からのフィールド名と値の抽出条件のコンパイル
field_value_pattern = re.compile(r'''
    ^\|         # '|'で始まる行
    (.+?)       # キャプチャ対象（フィールド名）、任意の1文字以上、非貪欲
    \s*         # 空白文字0文字以上
    =
    \s*         # 空白文字0文字以上
    (.+?)       # キャプチャ対象（値）、任意の1文字以上、非貪欲
    (?:         # キャプチャ対象外のグループ開始
        (?=\n\|)    # 改行+'|'の手前（肯定の先読み）
        | (?=\n$)   # または、改行+終端の手前（肯定の先読み）
    )           # グループ終了
    ''', re.MULTILINE + re.VERBOSE + re.DOTALL)


with open('britain.txt', 'r') as britain_file:
    # 基礎情報テンプレートの抽出
    contents = extract_pattern.findall(britain_file.read())  # findallは正規表現にマッチする部分文字列を全て探し出しリストとして返す（インデックスは0ベース）
    # フィールド名と値の抽出
    fiels_values = field_value_pattern.findall(contents[0])  # キャプチャの機能により ('フィールド名', 'キャプチャ名')の形式で複数のデータがリストに格納される

    # 辞書にセット
    result = {}
    for field_value in fiels_values:
        """
        field_valueには ('略名', 'イギリス') や ('確立形態4', "現在の国号「'''グレートブリテン及び北アイルランド連合王国'''」に変更")の形で値が代入される
        """
        result[field_value[0]] = remove_markup(remove_internallinks(remove_media(field_value[1])))

    # 国旗画像の値を取得
    fname_flag = result['国旗画像']

    # リクエスト生成
    url = 'https://www.mediawiki.org/w/api.php?' \
    + 'action=query' \
    + '&titles=File:' + urllib.parse.quote(fname_flag) \
    + '&format=json' \
    + '&prop=imageinfo' \
    + '&iiprop=url'

    # MediaWikiのサービスへリクエスト送信
    request = urllib.request.Request(url,
        headers={'User-Agent': 'NLP100_Python(@segavvy)'})
    connection = urllib.request.urlopen(request)

    # jsonとして受信
    data = json.loads(connection.read().decode())

    # URL取り出し
    url = data['query']['pages'].popitem()[1]['imageinfo'][0]['url']
    print(url)
