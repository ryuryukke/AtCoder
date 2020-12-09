from math import gcd
n = int(input())
a = list(map(int, input().split()))
ans = []
for i in range(2, 1001):
    ans.append(len([j for j in a if j % i == 0]))
print(ans.index(max(ans)) + 2)