s, p = map(int, input().split())
for i in range(1, int(p**(1/2))+1):
    if p % i == 0:
        n, m = i, p//i
        if n + m == s:
            print("Yes")
            exit()
print("No")
exit()
    