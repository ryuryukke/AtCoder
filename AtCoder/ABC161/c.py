n, k =map(int,input().split())
n %= k
origin = n
while n-k >= 0:
    n = abs(n-k)
    origin = n
if origin >= abs(n-k):
    print(abs(n-k))
else:
    print(origin)
