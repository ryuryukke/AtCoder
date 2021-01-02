from math import ceil
t = int(input())
nsk = [list(map(int, input().split())) for _ in range(t)]
for n, s, k in nsk:
    diff, change = -1, -1
    if n - s < k:
        diff = n - s
    else:
        diff = (n - s) % k

    if diff == 0:
        print((n - s) // k)
        continue
    else:
        if n > k:
            change = n % k
        else:
            change = ceil(n / k) * k - n
    if change == 0:
        print(-1)
        continue
    if diff < change:
        if change % diff != 0:
            print(-1)
        else:
            print((diff+1)*n, (change+1)*n, (diff + change+1)*n, 249561088 * k - n + s)
            print((change) // k)
    else:
        if diff % change != 0:
            print(-1)
        else:
            print((((diff // change) + 1) * n + (n - s)) // k)
    
    
