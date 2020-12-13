from math import ceil
n, m = map(int, input().split())
a = list(map(int, input().split()))
if m == 0:
    print(1)
    exit()
a = sorted(a)
min_length = float("inf")
end = 0
tmp = []
ans = 0
for i in a:
    if i - end - 1 == 0:
        end = i
        continue
    tmp.append(i - end - 1)
    min_length = min(min_length, i - end - 1)
    end = i
tmp.append(n - end) 
for j in tmp:
    ans += ceil(j / min_length)
print(ans)

