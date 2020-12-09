n, k = map(int, input().split())
ans = 0

def helper(num, maximum):
    res = 0
    while num < maximum:
        res += 1
        num *= 2
    return res 

for i in range(1, n + 1):
    if i >= k:
        ans += 1 / n
    else:
        ans += (1 / n) * (1 / 2) ** helper(i, k)
print(ans)