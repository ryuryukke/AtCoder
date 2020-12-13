"""
EDIT DISTANCEを復習しましょうバグらせてしまった。。。。
このコードは間違っています。コンテスト中に書いたものです
"""
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
if len(set(a)) * len(set(b)) == 1 and len(a) == len(b):
    print(len(a))
    exit() 
dp = [[0] * (m) for _ in range(n)]
dp[0][0] = 0 if a[0] == b[0] else 1
for i in range(n):
    for j in range(m):
        if i * j == 0:
            dp[i][j] = dp[0][0] + abs(i-j)
        else:
            if i == j:
                if a[i] != b[j]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = dp[i-1][j-1] 
            else:
                dp[i][j] = dp[min(i, j)][min(i, j)] + abs(i - j)
print(dp)
print(dp[n-1][m-1])
