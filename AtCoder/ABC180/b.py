n = int(input())
x = list(map(int, input().split()))
ans_m, ans_y, ans_c = 0, 0, float("-inf")
for num in x:
    ans_m += abs(num)
    ans_y += abs(num)**2
    ans_c = max(ans_c, abs(num))
print(ans_m)
print(ans_y**(1/2))
print(ans_c)