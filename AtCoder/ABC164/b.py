b, a, d, c = map(int, input().split())
flag = False
while b > 0 and d > 0:
    if flag == False:
        d -= a
        flag = True
    else:
        b -= c
        flag = False
print("Yes" if d <= 0 else "No")
