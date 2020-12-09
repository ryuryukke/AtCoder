"""
エラトステネスの篩で、「その数をふるい落とした素数」を配列Dに記録.
その配列Dを利用すれば、ある数を素因数分解するときに、配列Dの値で割っていけば良い.
この方法は素因数分解のための√nまでの試し割りの発展系で、√nまでの素数をあらかじめ求めておき、素数だけで割れば
高速になるというもの.
"""
# MAX_Nは制約最大の数を入れる(例10**6+1)
MAX_N = 10**12+1
# sieve[n]は、その数を最初にふるいに落とした数を格納

def prime_factor_table(n):
    # sieveとはふるいの意味
    sieve = [i for i in range(n+1)]
    # n以下の整数を最初にふるい落とす数(√n以下に必ず存在)を求める.
    for i in range(2, int(n**0.5)+1):
        if sieve[i] == i:
            for j in range(2*i, n+1, i):
                if sieve[j] == j:
                    sieve[j] = i
    return sieve

# nは制約最大のやつを入れる
sieve = prime_factor_table(MAX_N)
# MAX_Nが50の時、[0, 1, 2, 3, 2, 5, 2, 7, 2, 3, 2, 11, 2, 13,
#  2, 3, 2, 17, 2, 19, 2, 3, 2, 23, 2, 5, 2, 3, 2, 29, 2, 31, 
# 2, 3, 2, 5, 2, 37, 2, 3, 2, 41, 2, 43, 2, 3, 2, 47, 2, 7, 2]
# となる。

def prime_factor(n):
    # 素数は英語でprime number
    # prime = set()
    prime = []
    while n > 1:
        # prime.add(sieve[n])
        prime.append(sieve[n])
        n //= sieve[n]
    return prime

print(prime_factor(120))
# ⇨[2, 2, 5]
