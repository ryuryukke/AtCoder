s = input()
t = input()

def check(l, r):
    res = 0
    for i, j in zip(l, r):
        if i != j:
            res += 1
    return res
ans = float("inf")
for i in range(len(s)-len(t)+1):
    ans = min(ans, check(s[i:len(t)+i], t))
print(ans)

     