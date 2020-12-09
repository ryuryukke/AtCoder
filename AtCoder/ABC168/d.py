# from collections import defaultdict
from collections import deque
n, m = map(int,input().split())
AB = [tuple(map(int, input().split())) for _ in range(m)]

def bfs(start):
    queue = deque()
    visited = [False] * n
    visited[start-1] = True
    queue.append(start)
    while queue:
        target = queue.popleft()
        for i in g[target]:
            if not visited[i-1]:
                ans[i-2] = target
                visited[i-1] = True
                queue.append(i)

ans = [0] * (n-1)
g = dict()
for a, b in AB:
    if a in g:
        g[a].append(b)
    if b in g:
        g[b].append(a)
    if a not in g:
        g[a] = [b]
    if b not in g:
        g[b] = [a]
start = 1
bfs(start)
if len([i for i in ans if i == 0]) == 0:
    print("Yes")
    print(*ans, sep="\n")
else:
    print("No")