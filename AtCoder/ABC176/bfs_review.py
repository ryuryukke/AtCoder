from collections import deque
h, w = map(int, input().split())
c = [input() for _ in range(h)]
dh = [-1, 0, 0, 1]
dw = [0, -1, 1, 0]

# 探索する際に毎度、要素にアクセスすると遅くなるため、enumerateでやる
for i, row in enumerate(c):
    for j, grid in enumerate(row):
        if grid == "s":
            start = (i, j)
        if grid == "g":
            goal = (i, j)

# # bfsの自分の中での書き方をあらかじめ決めておくとミスが起きにくい
# def bfs(start):
#     visited[start[0]][start[1]] = 0
#     queue = deque()
#     queue.append((start[0], start[1]))
#     while queue:
#         th, tw = queue.popleft()
#         for i in range(4):
#             nh, nw = th + dh[i], tw + dw[i]
#             """
#             queueに入れない条件を並べて最後にそれらif文を抜けることのできたものだけappend
#             if文を綺麗な水作るときのフィルターみたいに使う
#             """
#             # 移動先がグラフ外
#             if nh < 0 or nh > h - 1 or nw < 0 or nw > w - 1:
#                 continue

#             # 移動先が壁
#             if c[nh][nw] == "#":
#                 continue

#             # もう既に探索済み
#             if visited[nh][nw] != -1:
#                 continue
#             """
#             今までのif文をすり抜けてきた点だけ探索候補に加える
#             スタートからの最短距離をvisitedの値として保持
#             """
#             visited[nh][nw] = visited[th][tw] + 1
#             queue.append((nh, nw))

def dfs(start):
    visited[start[0]][start[1]] = 0
    stack = []
    stack.append(start)
    while stack:
        th, tw = stack.pop()
        for i in range(4):
            nh, nw = th + dh[i], tw + dw[i]
            # 移動先がグラフ外
            if nh < 0 or nh > h - 1 or nw < 0 or nw > w - 1:
                continue
            # 移動先が壁
            if c[nh][nw] == "#":
                continue
            # もう既に探索済み
            if visited[nh][nw] != -1:
                # 最短距離を更新する必要がある場合、距離更新してstackにいれる
                if visited[nh][nw] > visited[th][tw] + 1:
                    visited[nh][nw] = visited[th][tw] + 1
                    stack.append((nh, nw))
                continue
            # 今まで一度も到達したことのない点の場合
            visited[nh][nw] = visited[th][tw] + 1
            stack.append((nh, nw))

visited = [[-1] * w for _ in range(h)]
dfs(start)
print(visited)
print("No" if not visited[goal[0]][goal[1]] else "Yes") 
