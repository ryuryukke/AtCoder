# from collections import defaultdict
# n = int(input())
# # Aはフレンドリーさを表す
# A = list(map(int, input().split()))
# A.sort(reverse=True)
# table = defaultdict(list)
# tmp = []
# ans = 0
# for i, v in enumerate(A):
#     if i == 0:
#         table[str(v)+str(i)] = []
#         tmp.append(v)
#     if i == 1:
#         ans += tmp[0]
#         table[str(v)+str(i)] = [tmp[0]]
#         table[str(tmp[0])+str(i)] = [v]
#         tmp.append(v)
#     else:
#         for index, lst in sorted(table.items(), reverse=True):
#             t = [j for j in lst if j >= index]
#             if len(t) >= 1:
#                 ans += index
#                 print(table)
#                 table[index].remove(t[0])
#                 table[index].append(v)
#                 table[t[0]].remove(index)
#                 table[t[0]].append(v)
#                 table[v] = [index, t[0]]
# print(ans)
import heapq
n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
ans = 0
tmp = []
heapq.heappush(tmp, -a[0])
for i in range(1, n):
    point = -heapq.heappop(tmp)
    ans += point
    heapq.heappush(tmp, -a[i])
    heapq.heappush(tmp, -a[i])
print(ans)








        

        