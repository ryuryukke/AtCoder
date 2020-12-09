from collections import defaultdict
n, m = map(int, input().split())
h = list(map(int, input().split()))
d = defaultdict(set)
num = 0
for _ in range(m):
    a, b = map(int, input().split())
    d[a].add(b)
    d[b].add(a)
num += len(set(range(1,n+1)) - set(d))
for i, v in d.items():
    flag = False
    for j in v:
        if h[i-1] <= h[j-1]:
            flag = True
    if not flag:
        num += 1
print(num)
