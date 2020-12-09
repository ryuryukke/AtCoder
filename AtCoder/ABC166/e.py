# n = int(input())
# a = list(map(int, input().split()))
# d = dict()
# for i, v in enumerate(a):
#     d[i] = v
# d = sorted(d.items(), key=lambda x:x[1])
# print(d)
# # i = 0
# # for j in range(len(a)):
# #     while
# d = dict()
# d[1] = 4
# d[5] = 6
# d[2] = 9
# d[7] = 8
# print(d)
# for i in d:
#     print(i)

# a = [(2, 2), (-1, 2), (1, 1), (3, 1), (4, 1)]
# print(list(map(lambda x: x[0],a[:3])))
import heapq
a = [1, 7, 4, 8]
heapq.heapify(a)
print(a)
a = [(1,412), (7,0), (4,2), (8,7)]
heapq.heapify(a)
print(a)
