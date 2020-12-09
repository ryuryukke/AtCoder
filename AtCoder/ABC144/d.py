from math import atan, degrees
a, b, x = map(int, input().split())
vol = a**2*b/2
if x < vol:
    ans = atan((a*b**2)/(2*x))
elif x > vol:
    ans = atan((-2/a**3)*(x-a**2*b))
else:
    ans = atan(b/a)
print(degrees(ans))
