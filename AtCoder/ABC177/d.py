n, m = map(int, input().split())
ab = [tuple(map(int, input().split())) for _ in range(m)]

class UnionFind():
    def __init__(self, n):
        self.n = n
        # 要素が根の場合、-(そのグループの要素数)を格納
        self.parents = [-1] * n
        
    # 要素xが属するグループの根を返す    
    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
    
    # 要素xが属するグループと要素yが属するグループとを併合する
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        
        if x == y:
            return
        
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        
        self.parents[x] += self.parents[y]
        self.parents[y] = x
    
    # 要素xが属するグループのサイズ(要素数)を返す
    def size(self, x):
        return -self.parents[self.find(x)]

    # 要素x, yが同じグループに属すかどうか返す
    def same(self, x, y):
        return self.find(x) == self.find(y)
    
    # 要素xが属するグループに属する要素をリストで返す
    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]
    
    # 全ての根の要素をリストで返す
    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    # グループの数を返す
    def group_count(self):
        return len(self.roots())
    
    # {ルート要素: [そのグループに含まれる要素のリスト], ...}の辞書を返す
    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}
    
    # printでの表示用, ルート要素: [そのグループに含まれる要素のリスト]を文字列で返す
    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

tree = UnionFind(n)
for a, b in ab:
    a,b = a-1, b-1
    if not tree.same(a, b):
        tree.union(a, b)
ans = float("-inf")
for i in range(n):
    ans = max(ans, tree.size(i))
print(ans)



# if m == 0:
#     print(1)
#     exit()
    
# g = [[] for _ in range(n)]
# visited = [-1] * n
# for a, b in ab:
#     a, b = a-1, b-1
#     g[a].append(b)
#     g[b].append(a)
# # print(g)
# def dfs(start):
#     global visited
#     if visited[start] != -1:
#         return 1
#     stack = []
#     stack.append(start)
#     visited[start] = start
#     while stack:
#         root = stack.pop()
#         for j in g[root]:
#             if visited[j] == -1:
#                 visited[j] = start
#                 stack.append(j)

# for i in range(n):
#     dfs(i)
# # print(visited)
# tmp = Counter(visited)
# # print(tmp)
# p = sorted([v for i, v in tmp.items() if v != 1])
# island = len(p)
# # print(island)
# if island == 1:
#     print(n)
# else:
#     print(p[-1])

# """
# ------------------------------------------------------------------
# """
# # union findスニペット
# def find(x):
#     '''
#     xの根を求める
#     O(α(N))
#     '''
#     if par[x] < 0:
#         return x
#     else:
#         par[x] = find(par[x])
#         return par[x]


# def union(x, y):
#     '''
#     xとyの属する集合を併合する
#     '''
#     x = find(x)
#     y = find(y)
    
#     if x == y:
#         return False

#     if par[x] > par[y]:
#         x, y = y, x

#     par[x] += par[y]
#     par[y] = x
#     return True


# def size(x):
#     '''
#     xが属する集合の個数を求める
#     '''
#     return -par[find(x)]


# def same(x, y):
#     '''
#     xとyが同じ集合に属するかを判定する
#     '''
#     return find(x) == find(y)


# n, m = map(int, input().split())

# par = [-1] * n
# for _ in range(m):
#     a, b = map(int, input().split())
#     if not same(a-1, b-1):
#         union(a-1, b-1)

# res = 0
# for i in range(n):
#     res = max(res, size(i))

# print(res)




