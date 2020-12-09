import heapq
n, m = map(int, input().split())
a = list(map(int, input().split()))
heapq.heapify(a)
bc = [tuple(map(int, input().split())) for _ in range(m)]
bc = sorted(bc, key=lambda x: x[1], reverse=True)
# bcをソートしておくことにより、途中でfor文から抜けることができる。
# できるだけ大きいものからで変換していきたい。
for b, c in bc:
    flag = True
    for _ in range(b):
        if a[0] < c:
            heapq.heappop(a)
            heapq.heappush(a, c)
        else:
            flag = False
            break
    if not flag:
        break
print(sum(a))