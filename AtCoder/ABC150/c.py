# from math import factorial as f

#
# sum = 0
# ok = []
# for i in range(n):
#     if p[i] > q[i]:
#         sum += f(n-i-1)*abs(p[i]-q[i])
#         ok.append(p[i])
#         q = []
#         for k in ok:
#             q.append(k)
#         for j in range(1,n+1):
#             if j not in ok and j != p[i]:
#                 q.append(j)
#     elif p[i] < q[i]:
#         sum += f(n-i-1)*abs(p[i]-q[i])
#         ok.append(q[i])
#         p = []
#         for k in ok:
#             p.append(k)
#         for j in range(1,n+1):
#             if j not in ok and j != q[i]:
#                 p.append(j)
#     else:
#         ok.append(p[i])
#
# print(sum-1)
#########################################################
"""
順列の全列挙問題
→itertoolsをimportして用いる。
"""
import itertools
n = int(input())
p = tuple(map(int, input().split()))
q = tuple(map(int, input().split()))
num_list = list((itertools.permutations(range(1,n+1))))
print(abs(num_list.index(p)-num_list.index(q)))
