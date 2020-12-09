from collections import deque
n = int(input())
nums = list(map(int, input().split()))
changed = set()
real = list(range(1, n+1))
ans = []
queue = deque()
for j in range(n-1):
    if nums[j] > nums[j+1]:
        queue.append(j)
while queue:
    i = queue.popleft()
    if i in changed:
        continue
    changed.add(i)
    ans.append(i+1)
    tmp = nums[i]
    nums[i] = nums[i+1]
    nums[i+1] = tmp
    if (i >= 1) and (nums[i-1] > nums[i]) and (i-1 not in changed):
        queue.append(i-1)
    if (i + 1 < n - 1) and (nums[i+1] > nums[i+2]) and (i+1 not in changed):
        queue.append(i+1)

if nums == real:
    if len(ans) != n - 1:
        print(-1)
        exit()
    for a in ans:
        print(a)
else:
    print(-1)
    