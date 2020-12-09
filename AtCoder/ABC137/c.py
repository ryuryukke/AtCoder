from collections import defaultdict
n = int(input())
s = [input() for _ in range(n)]
table = defaultdict(int)
ans = 0
for i in s:
    table["".join(sorted(i))] += 1
for num in table.values():
    ans += (num*(num-1)//2)
print(ans)

