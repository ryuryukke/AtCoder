import math
from functools import reduce

def gcd(*numbers):
    print(type(numbers))
    return reduce(math.gcd, numbers)

k = int(input())
sum = 0
for i in range(1,k+1):
    for j in range(1,k+1):
        for l in range(1,k+1):
            sum += gcd(i,j,l)
print(sum)
