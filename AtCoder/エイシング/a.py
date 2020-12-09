L, R, d = map(int, input().split())
if d == 1:
    print(R-L+1)
else:
    if R == L:
        if R % d == 0:
            print(1)
        else:
            print(0)
    else:
        print(R//d - L//d)