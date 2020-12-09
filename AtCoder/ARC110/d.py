n, m = map(int, input().split())
a = list(map(int, input().split()))
minimum = min(a)
tmp = m - (minimum * n) + (n - 1)
