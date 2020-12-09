# def main():
#     n = int(input())
#     x = []
#     for _ in range(n):
#         a, b, c = map(int, input().split())
#         x.append([a, b, c])
#     dp = [[0] * 3 for _ in range(n)]
#     # i日目の幸福度dp[i-1]
#     # まず1日目の幸福度を設定
#     dp[0] = [x[0][l] for l in range(3)]
#     for i in range(1,n):
#         for j in range(3):
#             dp[i][j] = max([dp[i-1][k]+x[i][j] for k in range(3) if k != j]+[dp[i][j]])
#     print(max(dp[n-1]))
#
# if __name__ == "__main__":
#     main()

###################################################################################
# setは{1, 3, 4}な感じで,tupleは(1, 3, 4)な感じだ！！
# 今度からは,挿入変更削除をしないような値はtupleに格納しよう。tupleの方がlistよりも速度速い
def main():
    n = int(input())
    x = []
    for _ in range(n):
        a, b, c = map(int, input().split())
        x.append((a, b, c))
    dp0 = [0]*(n+1)
    dp1 = [0]*(n+1)
    dp2 = [0]*(n+1)
    for i in range(1,n+1):
        a, b, c = x[i-1]
        dp0[i] = max(dp1[i-1]+a, dp2[i-1]+a)
        dp1[i] = max(dp0[i-1]+b, dp2[i-1]+b)
        dp2[i] = max(dp0[i-1]+c, dp1[i-1]+c)
    print(max(dp0[n], dp1[n], dp2[n]))

if __name__ == "__main__":
    main()
