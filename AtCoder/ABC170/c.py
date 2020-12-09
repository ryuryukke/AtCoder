x, n = map(int, input().split())
p = list(map(int, input().split()))
if not p:
    print(x)
    exit()
left_x = right_x = x
if x not in p:
    print(x)
    exit()
while 1:
    left_x = left_x - 1
    right_x = right_x + 1
    if left_x not in p:
        print(left_x)
        exit()
    elif right_x not in p:
        print(right_x)
        exit()
