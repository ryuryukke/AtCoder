N = int(input())
A = tuple(map(int, input().split()))
MOD = 10**9+7

arr = [0] * 60
for a in A:
    for i in range(60):
        if a>>i & 1:
            arr[59-i] += 1

ans = 0
for i, a in enumerate(arr):
    b = N - a
    ans += (a*b) * (2**(59-i))
    ans %= MOD
print(ans)

