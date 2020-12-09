n_, m_ = map(int, input().split())
a_ = list(map(int, input().split()))
b_ = list(map(int, input().split()))
cd_ = [list(map(int, input().split())) for _ in range(m_)]
if sum(a_) != sum(b_):
    print("No")
    exit()
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
        # return {r: self.members(r) for r in self.roots()}
        self.group = {r:[] for r in self.roots()}
        for i in range(self.n):
            self.group[self.find(i)].append(i)
        return self.group
    
    # printでの表示用, ルート要素: [そのグループに含まれる要素のリスト]を文字列で返す
    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

tree = UnionFind(n_)
for c, d in cd_:
    c, d = c-1, d-1
    tree.union(c, d)
# if tree.group_count() == 1:
#     print("Yes" if sum(a_) == sum(b_) else "No")
#     exit()
for k, v in tree.all_group_members().items():
    if sum(a_[i] for i in v) != sum(b_[i] for i in v):
        print("No")
        exit()
print("Yes")

# for rt in tree.roots():
#     num, num_ = 0, 0
#     for i in tree.members(rt):
#         num += a_[i]
#         num_ += b_[i]
#     if num != num_:
#         print("No")
#         break
# else:
#     print("Yes")
