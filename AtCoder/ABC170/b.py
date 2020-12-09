x, y = map(int, input().split())
if y % 2 != 0:
    print("No")
else:
    a = 2*x - (y//2)
    if a >= 0:
        if a > x:
            print("No")
        else:
            print("Yes")
    else:
        print("No")
