n = int(input())
ab = [list(map(int, input().split())) for _ in range(n)]
acc = [0]
for i in range(1, 10**6+1):
    acc.append(acc[-1]+i)
ans = 0
for a, b in ab:
    ans += (acc[b] - acc[a-1])
print(ans)