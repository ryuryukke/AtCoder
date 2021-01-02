n = int(input())
ab = [list(map(int, input().split())) for _ in range(n)]
ab = sorted(ab, key=lambda x: (sum(x) + x[0]), reverse=True)
ans = 0
taka = 0
aoki = sum(a for a, b in ab)
for a, b in ab:
    taka += (a + b)
    aoki -= a
    ans += 1
    if taka > aoki:
        print(ans)
        exit()
print(ans)
