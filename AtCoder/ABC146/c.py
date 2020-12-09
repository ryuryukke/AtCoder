# import sys
# sys.setrecursionlimit(10**7)
# a, b, x = map(int, input().split())
# ans = 10**9 if x // a >= 10**9 else x // a 
# if ans == 0:
#     print(ans)
#     exit()
# dim = lambda x: len(str(x)) if x >= 0 else 0
# while (a * ans + b * dim(ans)) > x:
#     tmp = ans
#     ans = 10**(dim(ans)-1) - 1
# while (a * tmp + b * dim(tmp)) > x:
#     tmp -= 1
# print(tmp)

# 　二分探索
# a, b, x = map(int, input().split())
# left = 1
# right = 10 ** 9
# dim = lambda x: len(str(x))
# if a * left + b * dim(left) > x:
#     print(0)
#     exit()
# if a * right + b * dim(right) < x:
#     print(10**9)
#     exit()
# while right - left > 1:
#     mid = (left + right) // 2
#     if a * mid + b * dim(mid) > x:
#         right = mid
#     else:
#         left = mid
# print(left)


