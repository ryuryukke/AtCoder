N,M,K = map(int,input().split())
AB = [tuple(map(int,input().split())) for i in range(M)]
CD = [tuple(map(int,input().split())) for i in range(K)]

class UnionFind:
    def __init__(self,N): # 最初の状態を作る
        self.parent = [i for i in range(N)]
        self.rank = [0] * N
        self.count = 0

    # そのノードの根を返す過程で,集合の要素を根に直接つなぎかえる
    def root(self,a):
        if self.parent[a] == a:
            return a
        else:
            self.parent[a] = self.root(self.parent[a])
            return self.parent[a]
    def is_same(self,a,b): # aとbの根が同じ,つまり同じ連結成分内かどうかを返す
        return self.root(a) == self.root(b)
    def unite(self,a,b): # 集合同士をつなげる
        # まず互いの根を確認
        ra = self.root(a)
        rb = self.root(b)
        if ra == rb: return
        if self.rank[ra] < self.rank[rb]: # 各集合の根の小さい方を大きい方にくっつける
            self.parent[ra] = rb
        else:
            self.parent[rb] = ra
            if self.rank[ra] == self.rank[rb]: self.rank[ra] += 1
        self.count += 1

blocks = [[] for _ in range(N)]
for c,d in CD:
    c,d = c-1,d-1
    blocks[c].append(d)
    blocks[d].append(c)

friends = [0] * N # 隣り合っているノード数を保持する
uf = UnionFind(N)
for a,b in AB:
    a,b = a-1,b-1
    friends[a] += 1
    friends[b] += 1
    # aとbが既に同じ集合内にいれば何もしない
    if uf.is_same(a,b): continue
    # aとbが同じ集合内にいない場合,集合同士をくっつける
    uf.unite(a,b)

# 効率の良い繋ぎ方にする
for i in range(N):
    uf.root(i)

from collections import Counter
# ctrは根がいくつかの値である集合内にノードがいくつあるかを示す
ctr = Counter()
for i in range(N):
    r = uf.root(i)
    ctr[r] += 1

ans = []
for i in range(N):
    tmp = ctr[uf.root(i)] - 1 - friends[i]
    for b in blocks[i]:
        if uf.is_same(i,b):
            tmp -= 1
    ans.append(tmp)
print(*ans)
