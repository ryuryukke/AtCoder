k, n = map(int, input().split())
a = list(map(int, input().split()))
l = []
for i in range(1,len(a)):
    l.append(a[i]-a[i-1])
if a[0] == 0:
    l.append(k-a[len(a)-1])
else:
    l.append(k-a[len(a)-1]+a[0])
print(k-max(l))
