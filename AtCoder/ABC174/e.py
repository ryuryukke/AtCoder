# n, k = map(int, input().split())
# a = tuple(map(int, input().split()))
# import heapq

n, k = map(int, input().split())
a = tuple(map(int, input().split()))
ok = 10**9
ng = 0
while abs(ng-ok) > 1:
    mid = (ok + ng) // 2
    cnt = 0
    for i in a:
        cnt += (i+mid-1)//mid-1
    if cnt <= k:
        ok = mid
    else:
        ng = mid
print(ok)
