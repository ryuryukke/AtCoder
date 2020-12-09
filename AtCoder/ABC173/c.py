import itertools
# import copy
# h, w, k = map(int, input().split())
# table = [list(input()) for _ in range(h)]
# ans = 0
# for ptr_h in itertools.product([0, 1], repeat=h):
#     for ptr_w in itertools.product([0, 1], repeat=w):
#         times = 0
#         tmp = copy.deepcopy(table)
#         for i, v in enumerate(ptr_w):
#             if v == 1:
#                 for p in tmp:
#                     p[i] = "red"
#         for i, v in enumerate(ptr_h):
#             if v == 1:
#                 for ind, l in enumerate(tmp):
#                     if ind == i:
#                         for n in range(w):
#                             l[n] = "red"
#         for i in tmp:
#             for j in i:
#                 if j == "#":
#                     times += 1
#         if times == k:
#             ans += 1
# print(ans)
import itertools
h, w, k = map(int, input().split())
table = [list(input()) for _ in range(h)]
ans = 0
for ptr_h in itertools.product([0, 1], repeat=h):
    for ptr_w in itertools.product([0, 1], repeat=w):
        cnt = 0
        for i in range(h):
            for j in range(w):
                if ptr_h[i] == 0 and ptr_w[j] == 0:
                    if table[i][j] == "#":
                        cnt += 1
        if cnt == k:
            ans += 1
print(ans)





