# import sys
# imput = sys.stdin.readline()

n, k = map(int, input().split())
a = tuple(map(int, input().split()))
for i in range(n-k):
    if a[i] < a[i+k]:
        print("Yes")
    else:
        print("No")









# # 累積積を求める
# acc = []
# acc.append(a[0])
# for v in a[1:]:
#     acc.append(acc[-1]*v)
# cand = []
# cand.append(acc[k-1])
# tmp = k
# while tmp <= n-1:
#     cand.append(acc[tmp]//acc[tmp-k])
#     tmp += 1
# for i in range(len(cand)-1):
#     if cand[i] < cand[i+1]:
#         print("Yes")
#     else:
#         print("No")


