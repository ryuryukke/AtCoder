"""
1. 累積和+二分探索
2. しゃくとり法
"""

# 1. 累積和+二分探索
import itertools
from bisect import bisect
N, M, K = map(int, input().split())
A = tuple(map(int, input().split()))
B = tuple(map(int, input().split()))
A_sum = [0]
for a in A:
    A_sum.append(A_sum[-1]+a)
B_sum = [0]
for b in B:
    B_sum.append(B_sum[-1]+b)
# A_sum = tuple(itertools.accumulate(A))
# B_sum = tuple(itertools.accumulate(B))
ans = 0
for i, num in enumerate(A_sum):
    target = K - num
    if target < 0:
        break
    j = bisect(B_sum, target)
    ans = max(ans, i+j-1)
print(ans)

# lst = [7, 7, 31, 41, 78]
# import itertools
# from bisect import bisect
# lst_sum = tuple(itertools.accumulate(tuple(lst)))
# print(lst_sum)
# print(bisect(lst, 8))
# print(bisect(lst, 7))
# print(bisect(lst, 6))
# print(bisect(lst, 32))
