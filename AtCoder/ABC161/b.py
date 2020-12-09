n, m = map(int,input().split())
a = list(map(int,input().split()))
a.sort(reverse = True)
s = sum(a)
# 少数とかそうじゃないとかでごっちゃになるんだったら移行して解く方がいい
if a[m-1]*(4*m) >= s:
    print("Yes")
else:
    print("No")
# for i, l in enumerate(a):
#     if l <= s/(4*m):
#         i -= 1
#         break
# print("Yes" if i >= m-1 else "No")
