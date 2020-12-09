import itertools
n = input()
ans = float("inf")
for ptr in itertools.product([0, 1], repeat=len(n)):
    res, num = 0, 0
    for i, v in enumerate(ptr):
        if v == 1:
            num += 1
            res += int(n[i])
    if res == 0:
        continue
    if res % 3 == 0:
        ans = min(ans, len(n)-num)
print(-1 if ans == float("inf") else ans)
