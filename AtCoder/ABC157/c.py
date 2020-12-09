# # import sys
# n, m = map(int, input().split())
# d = {1:None, 2:None, 3:None}
# for i in range(m):
#     s, c = map(int, input().split())
#     if s == 1 and c == 0:
#         print("-1")
#         exit()
#     if c is not None and d[s] != c:
#         print("-1")
#         exit()
#     d[s] = c
# if d[2] == 0 and 1 not in d.keys():
#     if d[3] == "0":
#         print("100")
#         exit()
#     else:
#         print("-1")
#         exit()
# target = 0
# for s, c in map(int, d.items()):
#     if c is None:
#         continue
#     target += 10**(n-s)*c
# print(target)
