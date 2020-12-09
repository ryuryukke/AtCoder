a, v = map(int, input().split())
b, w = map(int, input().split())
t = int(input())
if a >= b:
    if b - w*t <= -1*(10**9):
        if a - v*t <= -1*(10**9):
            print("YES")
        else:
            print("NO")
    else:
        if w >= v:
            print("NO")
        else:
            print("YES" if abs(v-w)*t >= abs(a-b) else "NO")
else:
    if b + w*t >= 10**9:
        if a + v*t >= 10**9:
            print("YES")
        else:
            print("NO")
    else:
        if w >= v:
            print("NO")
        else:
            print("YES" if abs(v-w)*t >= abs(a-b) else "NO")

a, v = map(int, input().split())
b, w = map(int, input().split())
t = int(input())
if a >= b:
    if v <= w:
        print("NO")
    else:
        print("YES" if abs(v-w)*t >= abs(a-b) else "NO")
else:
    if v <= w:
        print("NO")
    else:
        print("YES" if abs(v-w)*t >= abs(a-b) else "NO")
