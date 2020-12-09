a, b, n = map(int, input().split())
x = 0
if n >= b:
    x = b-1
    print((a*x)//b - a*(x//b))
else:
    x = n
    print((a*x)//b - a*(x//b))
