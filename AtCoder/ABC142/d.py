# 2つの公約数は2つの数の最大公約数の約数
from math import gcd
A, B = map(int,input().split())
max_cmn_div = gcd(A, B)

# 約数列挙関数
def make_divisor(n):
    divisor = []
    for i in range(1, int(n**(1/2))+1):
        if n % i == 0:
            divisor.append(i)
            if i != n//i:
                divisor.append(n//i)
    return divisor

def check_prime(n):
    for i in range(2, int(n**(1/2))+1):
        if n % i == 0:
            return 0
    return 1

cmn_div = make_divisor(max_cmn_div)
ans = 0
for i in cmn_div:
    if check_prime(i):
        ans += 1
print(ans)