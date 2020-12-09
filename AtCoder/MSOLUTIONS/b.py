a, b, c = map(int, input().split())
k = int(input())
num = 0
while a >= b:
    b *= 2
    num += 1
while b >= c:
    c *= 2
    num += 1
print("Yes" if num <= k else "No")
    