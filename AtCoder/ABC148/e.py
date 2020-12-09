n = int(input())
if n % 2 != 0:
    print(0)
else:
    n //= 2
    div = 5
    cnt = 0
    while n//div != 0:
        cnt += (n//div)
        div *= 5
    print(cnt)
