# import sys
# def expect(x):
#     return sum(list(range(1,x+1)))/x
# input = sys.stdin.readline
# n, k = map(int, input().split())
# p = list(map(int, input().split()))
# table = []
# for i in range(n-k+1):
#     w = 0
#     for j in range(k):
#         w += expect(p[i+j])
#     table.append(w)
# print(max(table))
"""
ある数列の部分和を何度も求める問題では,累積和を考えよう
"""
import sys
input = sys.stdin.readline
n, k = map(int,input().split())
p = list(map(int, input().split()))
p = [(1+i)/2 for i in p]
# 累積和の配列sを作成する
# s = [0] * (n+1)
# for i in range(1,n+1):
#     s[i] = s[i-1] + p[i-1]
"""
もっと簡単な書き方(累積和)
"""
s = [0]
for i in p:
    s.append(s[-1] + i)

max = -1 * float("inf")
for i in range(n-k+1):
    sum = s[k+i] - s[i]
    if max <= sum:
        max = sum
print(max)
