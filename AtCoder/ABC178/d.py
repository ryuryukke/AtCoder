# import sys
# sys.setrecursionlimit(10**7)
# s = int(input())
# ans = 0
# summ = 0
# MOD = 10**9 + 7
# def dfs(A):
#     global ans, summ
#     print(A, summ)
#     # summ = sum(A)
#     if summ == s:
#         ans += 1
#         ans %= MOD
#         return False
#     elif summ < s:
#         for i in range(3, s+1):
#             if s - summ < 3:
#                 break
#             A.append(i)
#             summ += i
#             if dfs(A) == False:
#                 summ -= A[-1]
#                 A.pop()
#                 break
#             summ -= A[-1]
#             A.pop()
#         return True
#     else:
#         return False

# dfs([])
# print(ans%MOD)
s = int(input())
MOD = 10 ** 9 + 7
ans = 0
fact = [0] * 10000
fact[0], fact[1] = 1, 1
for i in range(2, 10000):
    fact[i] = (fact[i-1] * i) % MOD

def f(n, r):
    return fact[n] * pow(fact[n-r], -1, MOD) * pow(fact[r], -1, MOD)

for i in range(1, s//3+1):
    if i == 1:
        ans += 1
    else:
        m = s - i * 3
        ans += f(m+i-1, m)
        ans %= MOD
print(ans%MOD)
