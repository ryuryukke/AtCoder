"""
競プロにおいて"最小値を求めろ"という時に,0からインクリメントしていき,
初めて条件を満たすものを出力するという考え方がよくある！！
"""
n, m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(m)]
if n == 1:
    for i in range(10):
        tmp = str(i)
        flag = True
        for j in range(m):
            if tmp[arr[j][0]-1] != str(arr[j][1]):
                flag = False
        if flag:
            print(i)
            exit()
    print(-1)
else:
    for i in range(10**(n-1),10**n):
        tmp = str(i)
        flag = True
        for j in range(m):
            if tmp[arr[j][0]-1] != str(arr[j][1]):
                flag = False
        if flag:
            print(i)
            exit()
    print(-1)
