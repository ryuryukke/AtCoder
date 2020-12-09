"""
Pythonにおける"ある条件を満たす「数列」を全探索"する方法
1. itertools.productを用いる方法
2. 再帰を用いた方法(応用が効く)
なぜ2.の方が応用が効くのかというと、itertoolsに頼ってばかりいると、ある特殊な順列の全探索の時に
itertools.(何か)を知らなければ途端に解けなくなってしまうからである。
2.の書き方を知っていると、どんな条件を持った順列でも全探索することができる。
"""
# import itertools
# # 1. itertools.productを用いる方法
# for pattern in itertools.product([0, 1], repeat=3):
#     print(pattern)

"""
(0, 0, 0)
(0, 0, 1)
(0, 1, 0)
(0, 1, 1)
(1, 0, 0)
(1, 0, 1)
(1, 1, 0)
(1, 1, 1)
"""

# 2. 再帰を用いた方法(応用が効く)
# M = 2
# repeat = 3
# def dfs(A):
#     if len(A) == repeat:
#         print(A)
#         return
#     for v in range(M):
#         A.append(v)
#         dfs(A)
#         A.pop()
# dfs([])

"""
<<<テンプレート>>>
def dfs(A):
    if len(A) == (求めたい順列の長さ):
        処理
        return
    else:
        for v in range(順列を構成する数字):
            A.append(v)
            dfs(A)
            A.pop()
dfs([])
<<<テンプレート>>>

[0, 0, 0]
[0, 0, 1]
[0, 1, 0]
[0, 1, 1]
[1, 0, 0]
[1, 0, 1]
[1, 1, 0]
[1, 1, 1]
"""

"""
ちなみに今回の問題ABC165Cだと、対象にする順列は1 <= a <= b <= c <= d <= 5を満たすような順列abcdである。
これを全探索するようなitertoolsはitertools.cobinations_with_replacementであるようだが覚えるの大変よなあ
まあ、itertools.permutationsとかitertools.combinations, itertools.productとか覚えててもいいかも。
"""
# N, M, Q = map(int, input().split())
# abcd = [tuple(map(int, input().split())) for _ in range(Q)]
# ans = float("-inf")
# # 全探索して条件に合うものだけに処理をしていく感じ、、ABC147のHonestOrUnkind2に似てるな！
# def calcu(arr):
#     res = 0
#     for a, b, c, d in abcd:
#         if arr[b-1] - arr[a-1] == c:
#             res += d
#     return res

# def dfs(A):
#     global ans
#     if len(A) == N:
#         ans = max(ans, calcu(A))
#         return
#     else:
#         start = A[-1] if len(A) > 0 else 1
#         for num in range(start, M+1):
#             A.append(num)
#             dfs(A)
#             A.pop()

# dfs([])
# print(ans)
candidates = [2,3,6,7]
target = 7
ans = []  

def dfs(A):
    global ans
    num = sum(A)
    if num > target:
        return 
    elif num == target:
        ans.append(A[:])
        return
    for i in candidates:
        A.append(i)
        dfs(A)
        A.pop()

dfs([])
print(ans)

