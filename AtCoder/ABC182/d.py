n = int(input())
a = list(map(int, input().split()))
acc = [0]
stack = []
for i in a:
    acc.append(acc[-1] + i)
acc = acc[1:]
for j in range(n):
    if j == 0:
        stack.append(acc[j])
    else:
        tmp = acc[:j+1]
        for n in tmp:
            stack.append()

