n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]
ans = 0
for i in range(n-1):
    for j in range(i+1, n):
        x1, y1 = xy[i]
        x2, y2 = xy[j]
        if -1 <= (y2 - y1) / (x2 - x1) <= 1:
            ans += 1
print(ans)