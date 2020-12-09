"""
・Union-Find木
グループ分けを木構造で管理するデータ構造のこと.
同じグループに属する=同じ木に属するという木構造でグループ分けをする際,以下の2点を高速に行える.

1. 要素xと要素yが同じグループに属するかどうかを判定したい
　→ 要素xの根と要素yの根が同じならば同じグループ，要素xの根と要素yの根が同じでないならば異なるグループにあることが分かる．
2. 要素xと要素yが同じグループに属する場合，要素xの属するグループと要素yの属するグループの併合する．

"""
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

    """
    members() はO(N)で遅いことに注意！！
    """
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
        # コメントアウトしたこのコードはmembers()を使っているため計算量かかる
        # return {r:self.members(r) for r in self.roots()}
        self.group = {r:[] for r in self.roots()}
        for i in range(self.n):
            self.group[self.find(i)].append(i)
        return self.group
    
    # printでの表示用, ルート要素: [そのグループに含まれる要素のリスト]を文字列で返す
    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

"""
<<<union-findの使い方>>>
n = int(input())
ab = [tuple(map(int, input().split())) for _ in range(n)]
tree = UnionFind(n)
for a, b in ab:
    a,b = a-1, b-1
    if not tree.same(a, b):
        tree.union(a, b)

これで、木完成。
"""