n, q = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n-1)]
px = [list(map(int, input().split())) for _ in range(q)]
count = [0] * n

def dfs(node, point):
    global n, count
    visited = [-1] * n
    stack = []
    stack.append(node)
    visited[node] = 0
    while stack:
        target = stack.pop()
        for i in graph[target]:
            if visited[i] != -1:
                continue
            if i < node:
                continue
            else:
                visited[i] = 0
                stack.append(i)
    for i, v in enumerate(visited):
        if v == 0:
            count[i] += point
    return 0


# グラフ作成
graph = [[] for _ in range(n)]
for node1, node2 in ab:
    node1, node2 = node1 - 1, node2 - 1
    graph[node1].append(node2)
    graph[node2].append(node1)

# 一回の操作に対して、そのノードをスタートとするDFSを行い、countに足していく
for p, x in px:
    dfs(p-1, x)
print(*count, sep=" ")






n,q=map(int,input().split())
cnt=[0]*(n+1)
g=[[] for _ in range(n+1)]
for _ in range(n-1): #木グラフの隣接リストを作成
 a,b=map(int,input().split())
 g[a].append(b)
 g[b].append(a)
for _ in range(q): #各頂点についてcount[v]を計算
 v,val=map(int,input().split())
 cnt[v]+=val
q=[]
q.append(1) #DFSのスタックによる実装、まずスタックに始点1を積む
checked=[0]*(n+1) #各頂点を見たかどうかのフラグを持っておく
while q:
 v=q.pop()
 checked[v]=1 #頂点を見たかどうかのフラグを更新する
 for u in g[v]:
   if checked[u]==1: #vの子ノードuについて、まだ見ていない頂点であればcount[u]をcount[u]+=count[v]として更新する
     continue
   cnt[u]+=cnt[v]
   q.append(u) #スタックに子ノードuを積む
print(*cnt[1:]) #各頂点のcountが答えとなる
