dp = [[0] * 10 for _  in range(101)]
for i in range(1, 101):
    for j in range(1, 10):
        dp[i][j] = dp[i - 1][j - 1] + 2
print(*dp)
