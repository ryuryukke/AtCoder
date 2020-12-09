import sys
a = [list(map(int, input().split())) for _ in range(3)]
n = int(input())
b = []
cnt = 0
for _ in range(n):
    b.append(int(input()))
for i in range(3):
    for j in range(3):
        if a[i][j] in b:
            cnt += 1
            a[i][j] = 0
if cnt < 3:
    print("No")
else:
    if a[0][0]==a[1][1]==a[2][2]:
        print("Yes")
        sys.exit()
    elif a[2][0]==a[1][1]==a[0][2]:
        print("Yes")
        sys.exit()
    else:
        for k in range(3):
            if a[k][0]==a[k][1]==a[k][2] or a[0][k]==a[1][k]==a[2][k]:
                print("Yes")
                sys.exit()
    print("No")
