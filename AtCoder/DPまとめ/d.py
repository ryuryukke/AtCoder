# ナップサックDP
N, W = map(int, input().split())
x = []
for i in range(N):
    w, v = map(int, input().split())
    x.append((w, v))

"""
<<ナップサック -Dynamic Programmingで解く->>
まずどんな状態をdp配列にするかを考える.
最終地点の状態から,一般状態を考えるのがコツ.
最終地点: 「持ち帰る品物の重さの総和が W 以下で,かつ価値の総和が最大値である」
一般状態を次のように考えてみる.
dp[i]: 0~i-1番目の品物の中から,品物の重さの総和が W 以下になるように選んだ時の,
       価値の総和の最大値
しかし,これだとdp[i] → dp[i+1]の時に,価値の総和が最大でも,品物の重さの総和
が W 以下かどうかがわからない.
したがって,
dp[i][sum]: 0~i-1番目の荷物の中から,重さの総和がsum以下となるように選んだ
            時の,価値の総和の最大値
とすると良い.
"""
dp = [[0] * (W+1) for _ in range(N+1)]
for i in range(1, N+1):
    w, v = x[i-1]
    for sum in range(W+1):
        if sum >= w:
            dp[i][sum] = max(dp[i-1][sum-w]+v, dp[i-1][sum])
        else:
            dp[i][sum] = dp[i-1][sum]
ans=-1
for j in range(W+1):
    ans=max(ans,dp[N][j])
print(ans)
