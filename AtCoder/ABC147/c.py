# def dfs(a):
# 	stack = []
# 	visited = [False] * N
# 	visited[a] = True
# 	stack.append(a)
# 	while stack:
# 		start = stack.pop()
# 		for i in node[start]:
# 			if visited[i] == False:
# 				visited[i] = True
# 				stack.append(i)

# 	return [i for i, j in enumerate(visited) if j]

# # Yes同士のノードをくっつけて強連結成分の問題かと思った。
# N = int(input())
# maximum = -1
# node = [[] for _ in range(N)]
# # まず有向グラフを作る
# for i in range(N):
#     num = int(input())
#     for j in range(num):
#         x, y = map(int, input().split())
#         if y == 1:
#         	node[i].append(x-1)
# for i in range(N):
# 	maximum = max(maximum, dfs(i))
# print(maximum)


"""
bit全探索
# """
# n = int(input())
# table = [[] for _ in range(n)]
# for i in range(n):
# 	a = int(input())
# 	for j in range(a):
# 		x, y = map(int, input().split())
# 		table[i].append((x, y))
#
# for i in range(2**n):
# 	select = [0] * n
# 	for j in range(n):
# 		if (i >> j) & 1:
# 			select[n-j-1] = 1
# arr = [1,0,2,3,0,4,5,0]
# 		flag = False
#         origin = []
#         for i in range(len(arr)-1):
#             if flag:
#                 flag = False
#                 continue
#             if arr[i] == 0:
#                 if i != len(arr)-2:
#                     origin = arr
#                     for j in range(i+2,len(arr)):
#                         arr[j] = origin[j-1]
#                 arr[i+1] = 0
#                 flag = True
# n = int(input())
# xy = [[] for _ in range(n)]
# ans = -float("inf")
#
# for i in range(n):
# 	a = int(input())
# 	for _ in range(a):
# 		x, y = map(int, input().split())
# 		xy[i].append(tuple([x-1, y]))
#
# for i in range(2**n):
# 	flag = False
# 	cnt = 0
# 	for j in range(n):
# 		if (i >> j) & 1:
# 			cnt += 1
# 			for x, y in xy[j]:
# 				if y == 1:
# 					if (i >> x & 1) == 0:
# 						flag = True
# 				elif y == 0:
# 					if (i >> x & 1) == 1:
# 						flag = True
# 	if not flag:
# 		ans = max(ans, cnt)
# print(ans)
import sys

n = int(input())
for _ in range(n):
	a = input()
for line in sys.stdin:
	line = line.rstrip("\n")
	if line == "2":
		print("Hi!")
	else:
		print("Good!")
