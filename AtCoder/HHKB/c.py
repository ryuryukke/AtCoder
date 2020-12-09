# import heapq
n = int(input())
p = list(map(int, input().split()))
# a = list(range(200001))
# heapq.heapify(a)
# cache = set()
# for i in p:
#     cache.add(i)
#     num = a[0]
#     if num in cache:
#         while num in cache:
#             num = heapq.heappop(a)
#         print(num)
#         heapq.heappush(a, num)
#     else:
#         print(num)
min_num = 0
cache = set()
for num in p:
    cache.add(num)
    if num == min_num:
        while 1:
            min_num += 1
            if min_num not in cache:
                break
    print(min_num)

        
        
