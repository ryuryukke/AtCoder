# from collections import deque
# h, w = map(int, input().split())
# c = tuple(map(int, input().split()))
# d = tuple(map(int, input().split()))
# s = [input() for _ in range(h)]
# town = [[0] * w for _ in range(h)]
# dh = [-1, 0, 0, 1]
# dw = [0, 1, -1, 0]

# def dfs(h, w, tmp):
#     queue = deque()
#     queue.append((h, w))
#     town[h][w] = tmp
#     while queue:
#         start = queue.popleft()
#         for i in range(4):
#             p, q = start[0] + dh[i], start[1] + dw[i]
#             if 0 <= p < len(s) and 0 <= q < len(s[0]):
#                 if s[p][q] == "#":
#                     continue
#                 if town[p][q] != 0:
#                     continue
#                 town[p][q] = tmp if not town[p][q] else town[p][q]
#                 queue.append((p, q))

# #　まずは町番号をつける
# tmp = 0
# for i in range(h):
#     for j in range(w):
#         if s[i][j] == "#":
#             continue
#         else:
#             if town[i][j] != 0:
#                 continue
#             tmp += 1
#             dfs(i, j, tmp)

# for i in range(h):
#     for j in range(w):
#         if s[i][j] == "#":
#             continue
#         else:
#             if town[i][j] != 0:
#                 continue
#             tmp += 1
#             dfs(i, j, tmp)
nums = [-1, 0, 1, 2, -1, -4]
# ans = set()
# for i, v in enumerate(nums):
#     target = -v
#     lst = nums[i+1:]
#     cache = dict()
#     for idx, num in enumerate(lst):
#         tmp = target - num
#         if tmp in cache:
#             ans.add((nums[i], nums[cache[tmp]], nums[idx+(i+1)]))
#         else:
#             cache[num] = idx+(i+1)
# print(ans)




