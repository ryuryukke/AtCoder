import math
from decimal import Decimal
a, b = input().split()
a = Decimal(a)
b = Decimal(b)
print(math.floor(a*b))
