r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())
ans = 0
if r1 != c1:
    if (r1+c1) % 2 != 0:
        if abs(r1 - c1) < 3:
            ans += 1
            r1, c1 = (r1+c1-1) // 2, (r1+c1-1) // 2
        else:
            ans += 2
            r1, c1 = (r1+c1-1) // 2, (r1+c1-1) // 2
    else:
        ans += 1
        r1, c1 = (r1+c1) // 2, (r1+c1) // 2 
if r1 != r2 or c1 != c2:
    ans += 1
if r2 != c2:
    if (r2+c2) % 2 != 0:
        if abs(r2 - c2) < 3:
            ans += 1
            r2, c2 = (r2+c2-1) // 2, (r2+c2-1) // 2
        else:
            ans += 2
            r2, c2 = (r2+c2-1) // 2, (r2+c2-1) // 2
    else:
        ans += 1
        r2, c2 = (r2+c2) // 2, (r2+c2) // 2 

print(ans)


