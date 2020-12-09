# import itertools
# from collections import Counter
n, k = map(int, input().split())
A = list(map(int, input().split()))
MOD = 10**9+7
# ans = float("-inf")
# for ptr in itertools.product([0, 1], repeat=n):
#     if Counter(ptr)[1] == k:
#         cand = 1
#         for i, v in enumerate(ptr):
#             if v == 1:
#                 cand *= A[i]
#         ans = max(ans, cand)
# print(ans%MOD)

# マイナスの個数
minus_num = len([i for i in A if i < 0])
A.sort(key=lambda x: abs(x), reverse=True)
A_k, k1_A = A[:k], A[k:]
tmp = 1
for num in A_k:
    tmp *= num
if tmp >= 0:
    print(tmp%MOD)
else:
    a = float("-inf")
    b = float("inf")
    c = float("-inf")
    d = float("inf")
    e = float("-inf")
    f = float("inf")
    # k+1以降でabsが最大のマイナスa
    for i in k1_A:
        if i < 0:
            a = max(a, abs(i))
    # k個のうちでabsが最小のプラスb
    for i in A_k:
        if i > 0:
            b = min(b, i)
    # k+1以降でabsが最大のプラスc
    for i in k1_A:
        if i > 0:
            c = max(c, i)
    # k個のうちでabsが最小のマイナスd
    for i in A_k:
        if i < 0:
            d = min(d, abs(i))
    # k個の内でabsが最大のマイナスe
    for i in A_k:
        if i < 0:
            e = max(e, abs(i))
    # k+1以降でabsが最小のマイナスf
    for i in k1_A:
        if i < 0:
            f = min(f, abs(i))

    if a == float("-inf"):
        if c == float("-inf"):
            print(tmp%MOD)
        else:
            tmp = tmp * c // (-d)
            print(tmp%MOD)
    elif c == float("-inf"):
        if b == float("inf"):
            tmp = tmp * (-f) // (-e)
            print(tmp%MOD)
        else:
            tmp = tmp * (-a) // b
            print(tmp%MOD)
    else:
        if (-a) * (-d) > c * b:
            tmp = tmp * c // d
            print(tmp%MOD)
        else:
            tmp = tmp * a // b
            print(tmp%MOD)


        
        
        





