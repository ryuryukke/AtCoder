# nC3を順当にやったのであれば、O(10^9)となり、TLE

# import itertools
# from math import factorial
# N = int(input())
# L = tuple(map(int, input().split()))
# nums = [0] * (N-3) + [1, 1, 1]
# ans = 0
# for ptr in itertools.permutations(nums):
#     edge = []
#     for i, v in enumerate(ptr):
#         if v == 1:
#             edge.append(L[i])
#     if edge[0] < edge[1] + edge[2] and edge[1] < edge[2] + edge[0] and edge[2] < edge[0] + edge[1]:
#         ans += 1
# ans //= (factorial(3)*factorial(N-3))
# print(ans)

# 結局のこのやり方も2^NとなりTLE
# import sys
# sys.setrecursionlimit(1000000)
# N = int(input())
# L = list(map(int, input().split()))
# res = 0
# def dfs(A):
#     global res, L
#     ans = [i for i, v in enumerate(A) if v == 1]
#     if len(A) == N:
#         if len(ans) == 3:
#             a, b, c = L[ans[0]], L[ans[1]], L[ans[2]]
#             if a < (b + c) and b < (c + a) and c < (a + b):
#                 res += 1
#         return
#     elif len(ans) == 3:
#         a, b, c = L[ans[0]], L[ans[1]], L[ans[2]]
#         if a < (b + c) and b < (c + a) and c < (a + b):
#             res += 1
#         return
#     else:
#         for v in range(2):
#             A.append(v)
#             dfs(A)
#             A.pop()
# dfs([])
# print(res)

"""
この問題で学ぶべきは、"全探索をやってみてうまくいかなかった場合"、"要素のうちのいくつかを固定して考える"という思考パターン。
"""
# O(N^2logN)で実行可能
import bisect
N = int(input())
L = list(map(int, input().split()))
ans = 0
L.sort()
for a_i in range(N-2):
    for b_j in range(a_i+1, N-1):
        c_idx = bisect.bisect_left(L, L[a_i]+L[b_j])
        if c_idx > b_j:
            ans += c_idx - b_j - 1
print(ans)
            

