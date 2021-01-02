from collections import defaultdict
n = int(input())
ab = [list(map(int, input().split())) for _ in range(n-1)]
q = int(input())
tex = [list(map(int, input().split())) for _ in range(q)]
graph = defaultdict(list)
c = [0] * n
for a, b in ab:
    a, b = a-1, b-1
    graph[a].append(b)
    graph[b].append(a)
memo = [[-1] * n for _ in range(n)]

def dfs(start, stop, add_p):
    global n, c
    if len(memo[start][stop]) != 1:
        for i in memo[start][stop][1:]:

    seen = [False] * n
    seen[start] = True
    stack = [start]
    c[start] += add_p
    while stack:
        target = stack.pop()
        for dest in graph[target]:
            if not seen[dest] and dest != stop:
                memo[start][stop].append(dest)
                memo[stop][start].append(dest)
                seen[dest] = True
                c[dest] += add_p
                stack.append(dest)


for t, e, x in tex:
    e -= 1
    if t == 1:
        start, stop = ab[e][0]-1, ab[e][1]-1
        dfs(start, stop, x)
    else:
        start, stop = ab[e][1]-1, ab[e][0]-1
        dfs(start, stop, x)
print(*c, sep="\n")
