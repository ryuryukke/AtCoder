# これでbit全探索できちゃう。
# import itertools
# for i in itertools.product([0, 1], repeat=4):
#     print(i)

# DFS的な全探索
M = 2
def dfs(A):
    if len(A) == 3:
        print(A)
        return 0
    for v in range(M):
        A.append(v)
        dfs(A)
        A.pop()

dfs([])
