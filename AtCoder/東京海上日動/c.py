from math import floor
n, k = map(int, input().split())
a = list(map(int, input().split()))
region = dict()
for i, light in enumerate(a):
    left, right = (i+1)-light-0.5, (i+1)+light+0.5
    left, right = max(1, left), min(n, right)
    
    region[i+1] = list(range(floor(left):floor(right)+1))
