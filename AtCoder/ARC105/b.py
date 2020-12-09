from math import gcd
from functools import reduce
N = int(input())
a = list(map(int, input().split()))
print(reduce(gcd, a))