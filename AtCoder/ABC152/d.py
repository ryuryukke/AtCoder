N = int(input())
N_ = str(N)
f_N, l_N = int(N_[0]), int(N_[-1])
digit = len(N_)
if digit > 2:
    inter_N = int(N_[1:digit-1])
cnt = 0
for num in range(1, N+1):
    num = str(num)
    f, l = int(num[-1]), int(num[0])
    if f == 0:
        continue
    for i in range(1, digit+1):
        if i == 1:
            if f == l:
                cnt += 1
            else:
                continue
        else:
            if i != digit:
                cnt += 10**(i-2)
            elif digit == 2 and i == digit:
                if f*10+l <= N:
                    cnt += 1
                else:
                    continue
            else:
                if f > f_N:
                    continue
                elif f == f_N:
                    if l > l_N:
                        cnt += inter_N
                    elif l <= l_N:
                        cnt += (inter_N+1)
                else:
                    cnt += 10**(i-2)
print(cnt)



