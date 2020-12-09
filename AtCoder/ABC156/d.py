"""
差分更新,二項定理の問題
"""
"""そもそも2**nでO(N)となっているから不可
from math import factorial
def combinations_count(n, r):
    return factorial(n) // (factorial(n - r) * factorial(r))
def main():
    n, a, b = map(int, input().split())
    whole = 2**n-1
    a = cmb(n, a)
    b = cmb(n, b)
    print((whole-a-b)%(10**9+7))

if __name__ == "__main__":
    main()
"""
##################################################################
"""
繰り返し二乗法O(logN)を用いる, modの計算(特に逆元)
2**nの計算量を落とす方法
"""
mod = 10**9+7 # p=MOD
# pythonにおいては繰り返し二乗法で累乗を解いてくれる組み込み関数powが存在する。が練習のため。
"""繰り返し二乗法を自分で実装
def pow(a, x):
    ans = 1
    while x > 0:
        if x&1 == 1:
            ans = ans * a % MOD
        a *= a
        x >>= 1
    return ans
"""
n, a, b = map(int, input().split())
whole = pow(2, n, mod)-1 # 2^n-1(mod p)を計算。
# nCaの計算
comb1=1
for i in range(n-a+1,n+1): # n*(n-1)*(n-2)*...*(n-a+1)(mod p)を計算
  comb1 *= i
  comb1 %= mod
for i in range(1,a+1): # 1/a!(mod p)を計算 フェルマーの小定理:1/a = a^p-2(mod p)を利用
  comb1 *= pow(i,mod-2,mod)
  comb1 %= mod
comb2=1
for i in range(n-b+1,n+1): # n*(n-1)*(n-2)*...*(n-b+1)(mod p)を計算
  comb2 *= i
  comb2 %= mod
for i in range(1,b+1):
  comb2 *= pow(i,mod-2,mod)
  comb2 %= mod
whole -= (comb1+comb2)
whole %= mod
print(whole)
