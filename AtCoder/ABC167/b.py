a,b,c,k = map(int, input().split())
if k >= a+b:
    print(a+(-1*(k-(a+b))))
else:
    if k <= a:
        print(k)
    else:
        print(a)
