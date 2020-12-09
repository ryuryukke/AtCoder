n = int(input())
a = list(map(int, input().split()))
MOD = 10**9+7
acc = [0]
ans = 0
for i in a:
    acc.append(acc[-1]+i)
acc = acc[1:]
for i, v in enumerate(a):
    ans += (v*(acc[-1]-acc[i]))%MOD
print(ans%MOD)







# MOD = 10**9+7
# ans = 0
# def dfs(A, start):
#     global ans
#     if len(A) == 2:
#         ans += ((A[0]*A[1])%MOD)
#         return
#     else:
#         for i in range(start, len(a)):
#             A.append(a[i])
#             dfs(A, i+1)
#             A.pop()

# dfs([], 0)
# print(ans%MOD)