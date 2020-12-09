x = int(input())
total = 100
i = 0
while total < x:
    i += 1
    total *= 1.01
    total = int(total)
print(i)
