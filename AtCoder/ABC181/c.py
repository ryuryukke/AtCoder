n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]

def helper(a, b, c):
    x1, y1 = a
    x2, y2 = b
    x3, y3 = c
    return True if (y1-y2)*(x2-x3) == (y2-y3)*(x1-x2) else False

for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            if helper(xy[i], xy[j], xy[k]):
                print("Yes")
                exit()
print("No")


