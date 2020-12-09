n = int(input())
A = list(map(int, input().split()))
table = [0] * 32
for a in A:
    for i in range(32):
        if a>>i & 1:
            table[31-i] += 1
arr = [0] * 32
ans = 0
for i, v in enumerate(table):
    if v % 2 == 1:
        arr[i] = 1
for i, a in enumerate(arr):
    ans += a * (2**(31-i))
for a in A:
    print(ans^a, end=" ")