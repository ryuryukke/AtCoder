import string
n = int(input())
# s = [0] * 15
# for i in range(15):
#     if i == 0:
#         s[i] = 26**(i+1)
#     else:
#         s[i] = s[i-1] + 26**(i+1)
# max_len = 1
# for i, v in enumerate(s):
#     if v >= n:
#         max_len = i+1
#         break
# res = n - 26 ** (max_len-1)
# s_ = [0] * max_len
# length = 0
# for i in range(max_len):
#     if i == 0:
#         s_[i] = 26**(i+1)
#     else:
#         s_[i] = s_[i-1] + 26**(i+1)
# for i, v in enumerate(s_):
#     if v >= res:
#         length = i+1
#         break
# def Base_10_to_n(X, n):
#     if (int(X/n)):
#         return Base_10_to_n(int(X/n), n)+str(X%n)
#     return str(X%n)
# n_ary.py
def base10to(n, b):
    if (int(n/b)):
        return base10to(int(n/b), b) + str(n%b)
    return str(n%b)

ans = []
print(base10to(n, 26))
for i in base10to(n, 26):
    ans.append(string.ascii_lowercase[int(i)-1])
print("".join(ans))