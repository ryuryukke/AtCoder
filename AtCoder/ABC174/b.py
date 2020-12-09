n, d = map(int, input().split())
xy = [list(map(int, input().split())) for _ in range(n)]
def f(a, b):
    num = (a**2 + b**2) ** (1/2)
    return num
ans = 0
for x, y in xy:
    if f(x, y) <= d:
        ans += 1
print(ans)