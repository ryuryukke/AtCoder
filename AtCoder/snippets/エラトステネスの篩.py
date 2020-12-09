"""
エラトステネスの篩とは、n以下の整数の素数を高速に求めるアルゴリズムである。(0(nloglogn))
<素数>
1とその数字自身の2つのみが正の約数である自然数。
したがって、1は素数ではない。
"""
# コード始まり
# primes(n)はn以下の整数のうちの、素数を返す。
def primes(n):
    # is_prime[n]は整数nが素数であればTrue, そうでなければFalseを持つ。
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]
# コード終わり
"""
print(primes(10))
⇨[2, 3, 5, 7]
"""