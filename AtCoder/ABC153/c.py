n, k = map(int, input().split())
h = list(map(int, input().split()))
h.sort(reverse=True)
if k >= len(h):
    print(0)
else:
    print(sum(h[k:]))
