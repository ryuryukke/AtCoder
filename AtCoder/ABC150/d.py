from functools import reduce
n, m = map(int, input().split())
a = list(map(int, input().split()))
l = [set() for _ in range(n)]
for i in range(n):
    j = 1
    while ((a[i]//2) * j) < m:
        l[i].add((a[i]//2) * j)
        j += 2
print(len(reduce(lambda a, b:a&b,l)))
# また後でむずかった
