n = int(input())
df_de = [list(map(int, input().split())) for _ in range(n)]
ans = 0
cand = []
for d1, d2 in df_de:
    if d1 == d2:
        ans += 1
    else:
        cand.append(ans)
        ans = 0
cand.append(ans)
print("Yes" if len([i for i in cand if i >= 3]) else "No")

