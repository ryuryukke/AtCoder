from math import gcd
a, b, c, d = map(int, input().split())
def f(n):
    x = n // c
    y = n // d
    z = n // (c*d//gcd(c,d))
    return n - x - y + z

whole = b - a + 1
sum_c = b//c - (a-1)//c
sum_d = b//d - (a-1)//d
div = (c*d)//gcd(c, d)
sum_c_d = b//div - (a-1)//div
print(whole - ((sum_c + sum_d) - sum_c_d))
