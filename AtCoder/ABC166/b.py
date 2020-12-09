n, k = map(int, input().split())
ans = set()
for _ in range(k):
    d = int(input())
    ans = ans | set(map(int,input().split()))
print(n-len(ans))
