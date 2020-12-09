n, m = map(int,input().split())
pS = [input().split() for _ in range(m)]
correct = 0
flag = [False] * n
pena = [0] * n
sum = 0
for p, s in pS:
    p = int(p)
    if flag[p-1] == True:
        continue
    else:
        if s == "WA":
            pena[p-1] += 1
        elif s == "AC":
            sum += pena[p-1]
            correct += 1
            flag[p-1] = True
print(correct, sum)
