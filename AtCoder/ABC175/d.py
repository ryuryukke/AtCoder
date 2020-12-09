n, k = map(int, input().split())
p = list(map(int, input().split()))
c = list(map(int, input().split()))

def check(start):
    lst = [start]
    while 1:
        tmp = p[start]-1
        if tmp in lst:
            return lst
        else:
            lst.append(tmp)
        start = tmp

cand = []
for idx in range(n):
    for j in cand:
        if idx in j:
            break
    else:
        cand.append(check(idx))
cache = []
for lst in cand:
    cache.append([c[i] for i in lst])
ans = float("-inf")
for nums in cache:
    for i in range(len(nums)):
        if len(nums) == k:
            ans = max(ans, sum(nums))
            break
        elif len(nums) < k:
            summ = 0
            for g in range(i, i+(k%len(nums))+1):
                if g > len(nums)-1:
                    summ += c[g-len(nums)]
                else:
                    summ += c[g]
            ans = max(ans, sum(nums) * (k // len(nums)) + summ)
        else:
            ans = max(ans, sum([c[i+h] for h in range(1, k+1)]))
print(ans)

            

