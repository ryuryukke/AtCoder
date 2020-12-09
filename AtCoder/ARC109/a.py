a, b, x, y = map(int, input().split())
if a < b:
    print(min(x + (b - a) * y, x + 2 * x * (b - a)))
elif a > b:
    print(min(x + (a - 1 - b) * y, x + 2 * x * (a - b - 1)))
else:
    print(x)