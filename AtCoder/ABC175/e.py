import bisect
T = int(input())
ans = dict()
for i in range(T):
    N, B = map(int, input().split())
    a = list(map(int, input().split()))
    acc = [0]
    a.sort()
    for num in a:
        acc.append(acc[-1] + num)
    idx = bisect.bisect(acc, B)
    ans[i+1] = idx-1
for j in range(T):
    print(f"Case #{j+1}: {ans[j+1]}")
  