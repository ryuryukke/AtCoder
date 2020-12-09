from collections import defaultdict
n, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
col_num, row_num = 0, 0
# col_num, row_num = set(), set()
for n_col, col in enumerate(a):
    for i in range(n-1):
        for j in range(i+1, n):
            if col[i] + col[j] <= k:
                # print(n_col, i, j)
                col_num += 1
                # print(i, j)
                # col_num.add((i, j))
# print(len(col_num))
# print(col_num)
print(col_num)
for n_row in range(n):
    for i in range(n-1):
        for j in range(i+1, n):
            if a[i][n_row] + a[j][n_row] <= k:
                # print(n_row, i, j)
                row_num += 1
                # print(i, j)
                # row_num.add((i, j))
# print(len(row_num))
print(row_num)
print(col_num * row_num // ((n-1)**2))