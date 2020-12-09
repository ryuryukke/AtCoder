h, w = map(int, input().split())
s = [input() for _ in range(h)]
ans = 0
for i in range(h):
    for j in range(w-1):
        if s[i][j] == s[i][j+1] and s[i][j] == ".":
            ans += 1
for k in range(w):
    for l in range(h-1):
        if s[l][k] == s[l+1][k] and s[l][k] == ".":
            ans += 1
print(ans)