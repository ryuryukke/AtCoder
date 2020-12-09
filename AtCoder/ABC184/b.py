n, x = map(int, input().split())
s = input()
for st in s:
    if st == "o":
        x += 1
    else:
        if x > 0:
            x -= 1
print(x)