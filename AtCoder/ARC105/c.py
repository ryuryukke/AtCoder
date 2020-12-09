n, m = map(int, input().split())
w = list(map(int, input().split()))
lv = [list(map(int, input().split())) for _ in range(m)]
num = 0
for l, v in lv:
    num += l
    print(num)

a = sorted(lv, key=lambda x:x[1])
b = sorted(lv, reverse=True)
ans = 0
if len([i for i in w if i > a[0][1]]):
    print(-1)
    exit()
min_weight = a[0][1]
max_length = b[0][0]
w = sorted(w)
tmp = 0
for l, v in lv:
    num = 0
    while 1:
        num += w[tmp]
        if num > min_weight:
            break
        tmp += 1
        if tmp == len(w):
            print(l, v)
            print(ans)
            exit()
    ans += l
num = 0
while 1:
    num += w[tmp]
    if num > min_weight:
        num = 0
        ans += max_length
        continue
    else:
        tmp += 1
        if tmp == len(w):
            break
print(ans + max_length - l)




