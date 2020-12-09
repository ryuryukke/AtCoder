# 何が何個あるかという問題についてはCounterを使おう！
# from collections import Counter
# in演算子の計算量は,リストやタプルだとO(N)だが,setやdictだとなんとO(1)なんだと。
n = int(input())
table = [input() for _ in range(n)]
# c = Counter(table)
d = dict()
for s in table:
    if s in d.keys():
        d[s] += 1
    else:
        d[s] = 0
# m = max(c.values())
m = max(d.values())
l = [key for key, value in d.items() if value == m]
l.sort()
print(*l, sep = "\n")
