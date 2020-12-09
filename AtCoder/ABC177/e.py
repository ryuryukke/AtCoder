from math import gcd
from functools import reduce
n = int(input())
a = list(map(int, input().split()))

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

sieve = prime_factor_table(10**6+1)

def prime_factor(n):
    # 素数は英語でprime number
    prime = set()
    while n > 1:
        prime.add(sieve[n])
        n //= sieve[n]
    return prime

for i, v in enumerate(a):
    if i == 0:
        tmp = prime_factor(v)
    else:
        prime = prime_factor(v)
        for j in prime:
            if j in tmp:
                if reduce(gcd, a) == 1:
                    print("setwise coprime")
                    exit()
                else:
                    print("not coprime")
                    exit()
            tmp.add(j)
print("pairwise coprime")

"""
------------------------------------------------------------------------------
"""

# N = int(input())
# M = 10**6 + 1

# counts = [0 for _ in range(M)]
# for a in list(map(int, input().split())):
#   counts[a] += 1

# integers = [0,0] + [1 for _ in range(M-2)]
# max_count = 0
# for i in range(M):
#   if integers[i] >= 1:
#     count = 0
#     for j in range(i,M,i):
#       count += counts[j]
#       integers[j] = 0
#     max_count = max(max_count,count)

# if max_count == N:
#   answer = 'not coprime'
# elif max_count >= 2:
#   answer = 'setwise coprime'
# else:
#   answer = 'pairwise coprime'

# print(answer)

"""
-----------------------------------------------------
"""


