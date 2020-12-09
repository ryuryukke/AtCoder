n = int(input())
ab = [list(map(int, input().split())) for _ in range(n)]
ab.sort(key=lambda x:x[1])
comp = []
for lst in ab:
    comp.append(lst[1])
acc = [0]
for i, v in enumerate(ab):
    acc.append(acc[-1] + v[0])
for x, y in zip(acc[1:], comp):
    if x > y:
        print("No")
        break
else:
    print("Yes")
