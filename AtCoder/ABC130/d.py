# しゃくとり法
n, k = map(int, input().split())
a = tuple(map(int, input().split()))
right = 0
part_sum, ans = 0, 0
for left in range(n):
    while part_sum < k and right < n: # rightが右に進む条件をandでここにまとめる
        part_sum += a[right]
        right += 1
    # rightが数列の右端まで行ってwhileを通らなかったり、抜ける場合があるためにこれを設ける
    if part_sum >= k:
        ans += n-(right-1)
    part_sum -= a[left] # leftが次のループでインクリメントするのでその分を引く
print(ans)

# 累積和+二分探索
from bisect import bisect_right
n, k = map(int, input().split())
a = tuple(map(int, input().split()))
ans = 0
acc = [0]
for i in range(n):
    acc.append(acc[-1]+a[i])
for part in acc:
    if part < k:
        continue
    ans += bisect_right(acc, part-k)
print(ans)