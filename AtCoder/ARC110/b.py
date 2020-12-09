n = int(input())
t = input()
if n == 1:
    if t == "0":
        print(10000000000)
    else:
        print(20000000000)
else:
    if t[:2] == "11":
        s = "110" * (n // 3 + 1)
        if t not in s:
            print(0)
            exit()
        start = n - 1
    elif t[:2] == "10":
        s = "101" * (n // 3 + 1)
        if t not in s:
            print(0)
            exit()
        start = n
    elif t[:2] == "01":
        s = "011" * (n // 3 + 1)
        if t not in s:
            print(0)
            exit()
        start = n + 1
    else:
        print(0)
        exit()
    print((10**10 * 3 - 1 - start) // 3 + 1)
    

