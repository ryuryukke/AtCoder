# from collections import deque
# n, m, k = map(int, input().split())
# A = deque(map(int, input().split()))
# B = deque(map(int, input().split()))
# time = 0
# ans = 0
# if (sum(A) + sum(B)) <= k:
#     print(len(A)+len(B))
#     exit()
# while len(A) != 0 or len(B) != 0:
#     if len(A) == 0:
#         time += B[0]
#         if time <= k:
#             ans += 1
#             B.popleft()
#         else:
#             print(ans)
#             exit()
#     elif len(B) == 0:
#         time += A[0]
#         if time <= k:
#             ans += 1
#             A.popleft()
#         else:
#             print(ans)
#             exit()
#     else:
#         if A[0] <= B[0]:
#             time += A[0]
#             if time <= k:
#                 ans += 1
#                 A.popleft()
#             else:
#                 print(ans)
#                 exit()
#         else:
#             time += B[0]
#             if time <= k:
#                 ans += 1
#                 B.popleft()
#             else:
#                 print(ans)
#                 exit()
# print(len(A)+len(B))
# 3回目(9/24)
from bisect import bisect_right
n, m, k = map(int, input().split())
a = tuple(map(int, input().split()))
b = tuple(map(int, input().split()))
ans = 0
cum_a, cum_b = [0], [0]
for num in a:
    cum_a.append(cum_a[-1] + num)
for num in b:
    cum_b.append(cum_b[-1] + num)
for i, v in enumerate(cum_a):
    target = k - v
    if target < 0:
        break
    idx = bisect_right(cum_b, target)
    ans = max(ans, i+idx-1)
print(ans)
