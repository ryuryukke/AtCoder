import heapq
n, m = map(int, input().split())
a = list(map(lambda x: -int(x), input().split()))
heapq.heapify(a)
num = 0
while num < m:
    maximum = -1 * heapq.heappop(a)
    maximum //= 2
    heapq.heappush(a, -maximum)
    num += 1
print(-sum(a))

