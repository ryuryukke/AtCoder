a, b = map(int, input().split())
dp = [0] * 41
dp[1] = 1
for i in range(2, 41):
    if i >= 5:
        if i >= 10:
            dp[i] = min(dp[i-1], dp[i-5], dp[i-10]) + 1
        else:
            dp[i] = min(dp[i-1], dp[i-5]) + 1
    else:
        dp[i] = dp[i-1] + 1
if a == b:
    print(0)
    exit()
elif a > b:
    print(dp[a - b])
    exit()
else:
    print(dp[b - a])
    exit()


