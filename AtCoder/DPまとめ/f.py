s = input()
t = input()
# dp[i][j] := 文字列sをi文字目まで、文字列tをj文字目まで見た時のLCS
dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]

for i in range(1, len(s) + 1):
    for j in range(1, len(t) + 1):
        if s[i-1] == t[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

ans = ''
i, j = len(s), len(t)
while i > 0 and j > 0:
    if s[i - 1] == t[j - 1]:
        ans += s[i - 1]
        i, j = i - 1, j - 1
    elif dp[i][j - 1] > dp[i - 1][j]:
        j -= 1
    else:
        i -= 1

print(ans[::-1])

