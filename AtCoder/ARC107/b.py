from collections import defaultdict
n, k = map(int, input().split())
cache = defaultdict(int)
ans = 0
j = 1
flag = False
for i in range(2, 2*n+1):
    cache[i] = j
    if j == n:
        flag = True
    if flag:
        j -= 1
    else:
        j += 1
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if i + j > 2 * n:
#             break
#         cache[i + j] += 1
for left in range(2, 2*n+1):
    if left - k in cache:
        ans += (cache[left] * cache[left-k])
print(ans)
        
