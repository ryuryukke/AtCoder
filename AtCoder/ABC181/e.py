# import bisect
# import copy
# import heapq
# n, m = map(int, input().split())
# h = list(map(int, input().split()))
# w = list(map(int, input().split()))
# h = sorted(h)
# ans_ = float("inf")
# for i in w:
#     ans = []
#     res = 0
#     tmp = copy.copy(h)
#     bisect.insort_right(tmp, i)
#     for i in range(n):
#         ans.append(tmp[i+1] - tmp[i])
#     print(tmp, ans)
#     heapq.heapify(ans)
#     while 1:
#         heapq.heapify(ans)
#         target = ans[0]
#         print(target)
#         if target == float("inf"):
#             break
#         res += target
#         idx = ans.index(target)
#         print(idx)
#         ans[idx] = float("inf")
#         if idx == 0:
#             ans[idx+1] = float("inf")
#         elif idx == n:
#             ans[idx-1] = float("inf")
#         else:
#             ans[idx-1] = float("inf")
#             ans[idx+1] = float("inf")
#     ans_ = min(ans_, res)
# print(ans_)
from collections import Counter
S = "4512583"
c = Counter(S)
print(c)
c2 = Counter("144")
print(c2)
print(c & c2)
if c & c2 == c2:
    print("Yes")
else:
    print("No")