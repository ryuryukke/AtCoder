a, b = map(int, input().split())
a, b = str(a), str(b)
print(max(sum(int(i) for i in a), sum(int(j) for j in b)))