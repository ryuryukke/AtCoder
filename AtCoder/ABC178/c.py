# mathモジュールのpowではなく，pythonの組み込み関数のpowを使うことに注意．
n = int(input())
MOD = 10**9+7

def f(num):
    return pow(num, n, MOD)
    # res = 1
    # for _ in range(n):
    #     res *= num
    #     res %= MOD
    # res %= MOD
    # return res

print((f(10)-f(9)-f(9)+f(8))%MOD)