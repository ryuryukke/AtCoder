h, n = map(int, input().split())
a = list(map(int, input().split()))
for i in a:
    h -= i
    if h <= 0:
        print("Yes")
        exit()
print("No")
