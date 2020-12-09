w, h, x, y = map(int, input().split())
ans1 = w*h/2
if w % 2 != 0 or h % 2 != 0:
    print(ans1, 0)
elif x == w//2 and y == h//2:
    print(ans1, 1)
else:
    print(ans1, 0)
