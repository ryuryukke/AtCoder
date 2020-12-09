import itertools
a, b, c, d = map(int, input().split())
lst = [a, b, c, d]
ans = 0
for ptr in itertools.product([0, 1], repeat=4):
    main, rest = 0, 0
    for i, v in enumerate(ptr):
        if v == 1:
            main += lst[i]
        else:
            rest += lst[i]
    if main == rest:
        print("Yes")
        break
else:
    print("No")
