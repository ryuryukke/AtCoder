H, W, n, m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]
cd = [list(map(int, input().split())) for _ in range(m)]

S = [["."]* H for i in range(W)]
for c, d in cd:
    c, d = c-1, d-1
    S[c][d] = "#"


rs = [[0]*W for i in range(H)]
ls = [[0]*W for i in range(H)]
ds = [[0]*W for i in range(H)]
us = [[0]*W for i in range(H)]

def helper(a, b):
    for i in range(H):
        tmp = 0  
        for j in range(W):
            if S[i][j] == '#':
                tmp = 0
            else:
                tmp += 1
                rs[i][j] = tmp
        tmp = 0
        for j in reversed(range(W)):
            if S[i][j] == '#':
                tmp = 0
            else:
                tmp += 1
                ls[i][j] = tmp
    for j in range(W):
        tmp = 0
        for i in range(H):
            if S[i][j] == '#':
                tmp = 0
            else:
                tmp += 1
                ds[i][j] = tmp
        tmp = 0
        for i in reversed(range(H)):
            if S[i][j] == '#':
                tmp = 0
            else:
                tmp += 1
                us[i][j] = tmp
    return rs[a][b] + ls[a][b] + ds[a][b] + us[a][b] - 3
ans = 0
for a, b in ab:
    a,b = a-1, b-1
    ans += helper(a, b)
    S[a][b] = "#"
    for i in range(W):
        tmp = b + i
        if tmp >= W or S[a][tmp] == "#":
            break
        else:
            S[a][tmp] = "#"
    for j in range(W):
        tmp = b-j
        if tmp <= 0 or S[a][tmp] == "#":
            break
        else:
            S[a][tmp] = "#"
    for k in range(W):
        tmp = a + k
        if tmp >= H or S[tmp][b] == "#":
            break
        else:
            S[tmp][b] = "#"
    for l in range(W):
        tmp = a - l
        if tmp <= 0 or S[tmp][b] == "#":
            break
        else:
            S[tmp][b] = "#"
print(ans)


