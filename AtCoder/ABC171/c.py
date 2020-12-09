import collections
from collections import defaultdict
n = int(input())
a = list(map(int, input().split()))
table = defaultdict(int)
for i in a:
    table[i] += 1
q = int(input())
bc = [tuple(map(int, input().split())) for _ in range(q)]
whole = sum(a)
ans = 0
for b, c in bc:
    if b in table:
        whole = whole + table[b] * (c-b)
        print(whole)
        table[c] += table[b]
        table[b] = 0
    else:
        print(whole)

