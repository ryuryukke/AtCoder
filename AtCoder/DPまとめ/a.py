
# def main(): # DP配列を用いて実装
#     n = int(input())
#     h = list(map(int, input().split()))
#     # dpテーブル作成,スタート地点のdpテーブルの値は0にする
#     dp =[float("inf")] * n
#     dp[0] = 0
#     dp[1] = abs(h[0] - h[1])
#     for i in range(2,n):
#         dp[i] = min([dp[i], dp[i-1]+abs(h[i-1]-h[i]), dp[i-2]+abs(h[i-2]-h[i])])
#     print(dp[n-1])


def res(i):
    if i == 0:
        return 0
    if i > 1:
        dp[i] = min([dp[i], res(i-1)+abs(h[i-1]-h[i]), res(i-2)+abs(h[i-2]-h[i])])
        return dp[i]




def main(): # 再帰関数とメモ化再帰
    n = int(input())
    h = list(map(int, input().split()))
    dp = [float("inf")] * n












if __name__ == "__main__":
    main()
