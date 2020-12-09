n, k = map(int, input().split())
lr = [list(map(int, input().split())) for _ in range(k)]
MOD = 998244353
cand = []
for l, r in lr:
    for i in range(l, r+1):
        cand.append(i)
cand.sort()
cand = tuple(cand)
# print(cand)
dp = [0] * (n+1)
dp[0] = 1
# dpを累積和しないといけないみたい，，
for i in range(1, n+1):
    tmp = 0
    for num in cand:
        if i - num >= 0:
            tmp += dp[i-num]
            tmp %= MOD
        else:
            dp[i] = (tmp % MOD)
            break    
    dp[i] = (tmp % MOD)
print(dp[-2])









# def dfs(A):
#     global ans
#     tmp = sum(A)
#     if tmp == n-1:
#         ans += 1
#         return
#     elif tmp > n-1:
#         return  
#     else:
#         for i in cand:
#             A.append(i)
#             dfs(A)
#             A.pop()

# dfs([])


