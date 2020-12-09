# from collections import defaultdict
# from collections import deque
# N = int(input())
# ab = [tuple(map(int, input().split())) for _ in range(N-1)]
# connect = defaultdict(list)
# used_color = set()
# node_has_color = defaultdict(set)
# # 木構造生成
# for a, b in ab:
#     connect[a].append(b)

# def bfs(start):
#     queue = deque()
#     queue.append(start)
#     while queue:
#         target = queue.popleft()
#         if not connect[target]:
#             continue
#         for dst in connect[target]:
#             if not node_has_color[target]:
#                 node_has_color[target].add(1)
#                 node_has_color[dst].add(1)
#                 used_color.add(1)
#                 queue.append(dst)
#             else:
#                 can_color = used_color - node_has_color[target]
#                 if not can_color:
#                     tmp = max(used_color) + 1
#                     node_has_color[target].add(tmp)
#                     node_has_color[dst].add(tmp)
#                     used_color.add(tmp)
#                     queue.append(dst)
#                 else:
#                     lst = sorted(list(can_color))
#                     node_has_color[target].add(lst[0])
#                     node_has_color[dst].add(lst[0])
#                     queue.append(dst)
                    

# bfs(1)
# print(len(used_color))
# for a, b in ab:
#     ans = list(set(node_has_color[a]) & set(node_has_color[b]))
#     if len(ans) == 1:
#         print(ans[0])
#     else:
#         ans.sort()
#         print(ans[-1])
# from collections import deque
# N = int(input())
# ab = [tuple(map(int, input().split())) for _ in range(N-1)]
# # 隣接リスト
# G = [[] for _ in range(N)]
# # グラフ作成
# for a, b in ab:
#     a, b = a-1, b-1
#     G[a-1].append(b-1)
#     G[b-1].append(a-1)

# def dfs(start, color):
    

n=int(input())
G=[[] for i in range(n+1)]
G_order=[]
for i in range(n-1):
  a,b=map(int,input().split())
  G[a].append(b)
  G_order.append(b)

from collections import deque
q=deque([1])
color=[0]*(n+1)
while q:
  cur=q.popleft()
  c=1
  for nx in G[cur]:
    if c==color[cur]:
      c+=1
    color[nx]=c
    c+=1
    q.append(nx)

print(max(color))
for i in G_order:
  print(color[i])
