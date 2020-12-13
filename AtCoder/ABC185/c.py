l = int(input())
ans = [1, 1, 2]
for i in range(3, 201):
    ans.append(i * ans[-1])
def nCr(n, r):
    return ans[n] // (ans[n-r] * ans[r])
print(nCr(l-1, 11))