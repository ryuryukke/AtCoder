# nCk(mod p)の計算
from math import factorial
X, Y = map(int, input().split())
MOD = 10**9+7
MAX = 10**6+1

 # a!のテーブルfact
fact = [0] * MAX
# (a!)^-1のテーブルfinv
finv = [0] * MAX

def comb_init():
    # a!と(a!)^-1のテーブルを作る
    # 累積積のイメージ
    fact[0] = fact[1] = 1
    finv[0] = finv[1] = 1
    for i in range(2, MAX):
        fact[i] = i * fact[i-1] % MOD
        finv[i] = pow(i, -1, MOD) * finv[i-1] % MOD

def comb(n, r):
    return fact[n] * (finv[n-r] * finv[r] % MOD) % MOD    

if (X+Y) % 3 != 0:
    print(0)
else:
    num = (X+Y)//3
    p = (Y - X + num) // 2
    q = (X + num - Y) // 2
    if not num >= min(p, q) >= 0:
        print(0)
        exit()
    comb_init()
    print(comb(num, min(p, q)))
# import time
# from math import factorial
# import sys
# sys.setrecursionlimit(1000000)
# def fact(n):
#     if n == 0:
#         return 1
#     else:
#         return n * fact(n-1)

# tik = time.time()
# fact(100000)
# tok = time.time()
# print(f"fact(1000): {tok-tik}")

# tik = time.time()
# factorial(100000)
# tok = time.time()
# print(f"factorial(1000): {tok-tik}")

