n = int(input())
p = list(map(int, input().split()))
cnt = 0
m = float("inf")
for i in p:
    if i <= m:
        cnt += 1
        m = i
print(cnt)
