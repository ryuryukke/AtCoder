# from collections import defaultdict
# n = int(input())
# s = [input() for _ in range(n)]
# table = defaultdict(int)
# for i in s:
#     table[i] += 1
# for j in ["AC", "WA", "TLE", "RE"]:
#     print(j+" "+"x"+" "+str(table[j]))
from collections import Counter
n = int(input())
s = [input() for _ in range(n)]
s = Counter(s)
for select in ["AC", "WA", "TLE", "RE"]:
    print(f"{select} x {s[select]}")