x, k, d = map(int, input().split())
tmp = x
limit = abs(x) // d
if limit >= k:
    print(abs(x+k*d) if x < 0 else abs(x-k*d))
else:
    if x > 0:
        plus = abs(x - limit*d)
        minus = abs(x - (limit+1)*d)
        if limit % 2 == 0:
            if k % 2 != 0:
                print(minus)
            else:
                print(plus)
        else:
            if k % 2 != 0:
                print(plus)
            else:
                print(minus)
    else:
        plus = abs(x + (limit+1)*d)
        minus = abs(x + limit*d)
        if limit % 2 == 0:
            if k % 2 != 0:
                print(plus)
            else:
                print(minus)
        else:
            if k % 2 != 0:
                print(minus)
            else:
                print(plus)



# for i in range(k):
#     if tmp < 0:
#         tmp += d
#     else:
#         tmp -= d
# print(abs(tmp))
