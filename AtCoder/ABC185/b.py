n, m, t = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(m)]
tmp = n
tmp -= ab[0][0]
if tmp <= 0:
    print("No")
    exit()
end = 0
for i, (a, b) in enumerate(ab):
    if i != 0:
        tmp -= (a - end)
        if tmp <= 0:
            print("No")
            exit()
    tmp = min((b - a) + tmp, n)
    end = b
tmp -= (t - end)
if tmp <= 0:
    print("No")
else:
    print("Yes")


