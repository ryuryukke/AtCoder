s = input()
t = input()
ans = 0
for i, v in enumerate(s):
    if v != t[i]:
        ans += 1
print(ans)