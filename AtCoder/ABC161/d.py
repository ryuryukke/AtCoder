# k = int(input())
# M = 2
# def dfs(A):
#     if len(A) == 3:
#         print(A)
#         return 0
#     for v in range(M):
#         A.append(v)
#         dfs(A)
#         A.pop()

# dfs([])

# length = 0
# for num in range(1, 10**10+1):
#     num = str(num)
#     for i in range(len(num)-1):
#         if abs(int(num[i]) - int(num[i+1])) > 1:
#             break
#     else:
#         length += 1
#         if length == k:
#             print(num)
#             exit()

# k = int(input())
# lunlun = []
# def dfs(A):
#     if len(A) == 10:
#         return
#     else:
#         start = int(A[-1])
#         if start == 9:
#             for i in range(start-1, start+1):
#                 A.append(str(i))
#                 lunlun.append("".join(A))
#                 dfs(A)
#                 A.pop()
#         elif start == 0:
#             for i in range(start, start+2):
#                 A.append(str(i))
#                 lunlun.append("".join(A))
#                 dfs(A)
#                 A.pop()
#         else:
#             for i in range(start-1, start+2):
#                 A.append(str(i))
#                 lunlun.append("".join(A))
#                 dfs(A)
#                 A.pop()
# for j in range(1, 10):
#     lunlun.append(str(j))
#     dfs([str(j)])
# lunlun = list(map(int, lunlun))
# lunlun.sort()
# print(lunlun[k-1])



k = int(input())
lunlun = []
def dfs(A):
    if len(A) > 10:
        return 
    else:
        num = int(A[-1])
        lunlun.append(int("".join(A)))
        if num == 0:
            for i in range(0, 2):
                A.append(str(i))
                dfs(A)
                A.pop()
        elif num == 9:
            for i in range(8, 10):
                A.append(str(i))
                dfs(A)
                A.pop()
        else:
            for i in range(num-1, num+2):
                A.append(str(i))
                dfs(A)
                A.pop()

for i in range(1, 10):
    dfs([str(i)])
lunlun.sort()
print(lunlun[k-1])




