from math import gcd
from functools import reduce
n = int(input())
def lcm(x, y):
    return x // gcd(x, y) * y
print(reduce(lcm, range(2, n+1)) + 1)