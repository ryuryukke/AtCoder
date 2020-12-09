n, m = map(int, input().split())
a = [int(input()) for _ in range(m)]
ans = 1
MOD = 10**9+7
MAX = 10**5+1

fib = [0] * MAX
fib[0], fib[1] = 1, 2
for i, j in zip(a[:m-1], a[1:]):
    if j - i == 1:
        print(0)
        exit()

for i in range(2, MAX):
    fib[i] = fib[i-1] + fib[i-2]

for i in range(m+1):
    left = 0 if i == 0 else a[i-1] + 1
    right = n if i == m else a[i] - 1
    between = right - left
    if not between:
        continue
    ans *= fib[between-1]
    ans %= MOD
print(ans)