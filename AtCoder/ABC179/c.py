n = int(input())
ans = 0
for a in range(1, 10**6):
    for b in range(1, 10**6):
        if a * b >= n:
            break
        else:
            ans += 1
print(ans)
# for c in range(1, n):
#     for a in range(1, n-c+1):
#         if (n-c)/a.is_integer():