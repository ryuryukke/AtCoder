# s = input()
# n = len(s)
# if n%2 == 0:
#     print("No")
#     exit()
# else:
#     for i in range(n//2):
#         if S[i] != S[(n-1)-i]:
#             print("No")
#             exit()
#     for i in range(((n-1)//2)//2):
#         if S[i] != S[(((n-1)//2)-1)-i]:
#             print("No")
#             exit()
#     for i in range((n//2)+1,(n//2)+1+(n-(n//2)+1)//2):
#         if S[i] != S[(n-1)-i]:
#             print("No")
#             exit()
#     print("Yes")

"""
回文であることの確認方法
1. 全てのi(1 <= i <= N)についてSのi文字目と(N-i-1)文字目が等しい
ことを確認する
2. Sを反転した文字列とSが等しいかどうかを調べる
"""
# lambda式を用いる
check = lambda x: x == x[::-1]
if check(s) and check(s[:(n-1)//2]) and check(s[(n+3)//2-1:]):
    print("Yes")
else:
    print("No")

list = [1, 2, 4]
str = "koike"
print(list[::-1], type(list[::-1]))
print(str[::-1], type(str[::-1]))
print(reversed(str))

# print("Yes" if S == S[::-1] and left == left[::-1] and right == right[::-1] else "No")
