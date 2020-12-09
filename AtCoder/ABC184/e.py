import bisect
n, t = map(int, input().split())
a = list(map(int, input().split()))
a = sorted(a)
i, j = 0, 0
su = 0
ans = float("-inf")
for j in range(len(a)):
    su += a[j]
    if i == j:
        continue
    while su > t:
        su -= a[i]
        i += 1
    ans = max(ans, su)
print(ans)

        

