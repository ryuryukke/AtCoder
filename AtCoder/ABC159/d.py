# N = int(input())
# A = list(map(lambda x: int(x)-1, input().split()))
# """
# 以下のように愚直に調べると,O(N^2)となる。
# for i in range(len(A)):
#     count = 0
#     d = {}
#     A_ = A[:]
#     A_.pop(i)
#     A_.sort()
#     for j in range(len(A_)-1):
#         if A_[j] == A_[j+1]:
#             count += 1
#         elif A_[j] != A_[j+1]:
#             count += 1
#             d[A_[j]] = (count*(count-1))//2
#             count = 0
#     count += 1
#     d[A_[j+1]] = (count*(count-1))//2
#     print(sum(d.values()))
# """
# """
# <差分更新>
# 各kについてそれを除いたものについて考えるタイプの問題には決まったアプローチがある
# 1.まず全体の数列についての答えを求めておいて
# 2.各要素を取り除くことによる"影響"を計算し
# 3.その影響分を引く
# ABC159のD問題にはそのアプローチが取れる
# """
# d = [0] * N
# for i in A:
#     d[i] += 1
# s = sum(map(lambda x: x*(x-1)//2, d))
# for i in A:
#     print(s + (1 - d[i]))
