# import itertools
# n, m, x = map(int, input().split())
# CA = [tuple(map(int, input().split())) for _ in range(n)]
#
# minimum = float("inf")
# for i in range(2**n):
#     select = [0] * n
#     a = [0] * m
#     money = 0
#     for j in range(n):
#         if (i>>j)&1:
#             select[n-1-j] = 1
#     for i, v in enumerate(select):
#         if v == 1:
#             money += CA[i][0]
#             for j, u in enumerate(CA[i][1:]):
#                 a[j] += u
#     # if all(l >= x for l in a):
#     if not len([l for l in a if l < x]):
#         minimum = min(minimum, money)
# print(-1 if minimum == float("inf") else minimum)
l1 = False
l2 = False
def m(l1, l2):
    if not l1 or not l2:
        return l1 or l2
print(m(l1, l2))
# ans = []
# for i in range(1,n+1):
#     for cap in itertools.combinations(table, i):
#         money = 0
#         a = [0] * m
#         for j in cap:
#             money += j[0]
#             for k in range(m):
#                 a[k] += j[k+1]
#         if not len([l for l in a if l < x]):
#             ans.append(money)
# if not ans:
#     print(-1)
# else:
#     print(min(ans))
