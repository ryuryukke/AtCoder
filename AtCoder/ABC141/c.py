n, k, q = map(int, input().split())
points = [k] * n
a = []
for i in range(q):
    a.append(int(input())-1)
for cand in a:
    points[cand] += 1
points = [i-q for i in points]
ans = ["Yes" if i > 0 else "No" for i in points]
print(*ans, sep="\n")




