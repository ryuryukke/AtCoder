n = input()
s = 0
for i in n:
    s += int(i)
print("Yes" if s % 9 == 0 else "No")