#!/bin/sh

# ソートして重複除去して、その件数でソート
sort result_n45.txt | uniq -c | sort --numeric-sort --reverse > "all.txt"

# 「する」のみ
grep "^する\s" result_n45.txt | sort | uniq -c | sort --numeric-sort --reverse > "suru.txt"

# 「見る」のみ
grep "^見る\s" result_n45.txt | sort | uniq -c | sort --numeric-sort --reverse > "miru.txt"

# 「与える」のみ
grep "^与える\s" result_n45.txt | sort | uniq -c | sort --numeric-sort --reverse > "ataeru.txt"
