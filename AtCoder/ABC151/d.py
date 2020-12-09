def dfs(h, w): # startからの距離の最大値をreturnする
    res = -1
    dist = [[-1] * W for _ in range(H)]
    stack = []
    dist[h][w] = 0
    stack.append([h, w])
    while stack:
        h, w = stack.pop()
        for i in range(4):
            nh = h + dy[i]
            nw = w + dx[i]
            if nh >= H or nh < 0 or nw >= W or nw < 0:
                continue
            if s[nh][nw] == "#":
                continue
            if dist[nh][nw] == -1:
                dist[nh][nw] = dist[h][w] + 1
                stack.append([nh, nw])
            if dist[nh][nw] != -1:
                if dist[nh][nw] > (dist[h][w]+1):
                    dist[nh][nw] = dist[h][w] + 1
                    stack.append([nh, nw])
    for i in range(H):
        if res <= max(visited[i]):
            res = max(visited[i])
    return res

H, W = map(int, input().split())
s = [input() for _ in range(H)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
m = -1
dist = 0
for i in range(H):
    for j in range(W):
        if s[i][j] == ".":
            dist = dfs(i, j)
            if m <= dist:
                m = dist
print(m)
