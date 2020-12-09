# def main():
#     n = int(input())
#     s = input()
#     whole = (n*(n-1)*(n-2))//6
#     num = n-2
#     cnt = 0
#     for i in range(n-3):
#         for j in range(i+1,n-1):
#             if j == i+1:
#                 if s[i] == s[j]:
#                     cnt += (n-(j+2))
#                     continue
#                 for k in range(j+2,n):
#                     if (j-i) == (k-j) or s[j] == s[k] or s[i] == s[k]:
#                         cnt += 1
#             else:
#                 if s[i] == s[j]:
#                     cnt += (n-(j+1))
#                     continue
#                 for k in range(j+1,n):
#                     if (j-i) == (k-j) or s[j] == s[k] or s[i] == s[k]:
#                         cnt += 1
#     print(whole-num-cnt)
#
# if __name__ == "__main__":
#     main()




n = int(input())
S = input()
k = 0
num = 0
r, g, b = 0, 0, 0
for s in S:
    if s == "R": r += 1
    elif s == "G": g += 1
    else: b += 1
whole = r * g * b
for i in range(n-2):
    for j in range(i+1,n-1):
        k = 2 * j - i # kが自動的に決まる！
        if k >= n:
            continue
        if S[i] != S[j] and S[j] != S[k] and S[i] != S[k]:
            num += 1
print(whole - num)
