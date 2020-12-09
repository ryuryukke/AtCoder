N = int(input())
a = list(map(int, input().split()))
ans = 0
for i, v in enumerate(a):
    if i % 2 == 0:
        if v % 2 == 1:
            ans += 1
print(ans)

