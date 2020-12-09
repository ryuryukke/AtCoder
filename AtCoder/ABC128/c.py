import itertools
n, m = map(int, input().split())
ans = 0
switches = []
for i in range(m):
    lst = list(map(int, input().split()))
    switches.append(lst[1:])
p = list(map(int, input().split()))
for ptr in itertools.product([0, 1], repeat=n):
    for idx, nums in enumerate(switches):
        res = 0
        for num in nums:
            if ptr[num-1] == 1:
                res += 1
        if res % 2 != p[idx]:
            # breakの時の処理
            break
    else:
        # breakを通らずに抜けた時の処理
        ans += 1
print(ans)


