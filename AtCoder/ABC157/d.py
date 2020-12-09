from collections import deque
import collections
def bfs(G, start):
    label[start] = start
    queue = deque()
    visited = [False] * (len(G))
    queue.append(start)
    while queue:
        target = queue.popleft()
        label[target] = start
        for j in G[target]:
            if visited[j] == False:
                visited[j] = True
                queue.append(j)
    # visited = [k for k, x in enumerate(visited) if x ]
    # return set(visited)

N, M, K = map(int, input().split())
F_G = [[] for _ in range(N)]
B_G = [[] for _ in range(N)]
# ↓これは連結グラフの集まりを示しており,実体はset()の集合となっている.
renketu = {}
# print(renketu)
# renketu[2]=({3})
# print(renketu)
# renketu[2].add(4)
# print(renketu)
# 無向グラフ及び,連結成分の作成
for _ in range(M):
    flag = False
    a, b = map(int, input().split())
    if len(renketu) == 0:
        renketu[a-1] = ({a-1})
        renketu[a-1].add(b-1)
        continue
    for i, l in list(renketu.items()):
        if a-1 in l or b-1 in l:
            index = i
            flag = True
    if flag:
        renketu[i].add(a-1)
        renketu[i].add(b-1)
    else:
        renketu[a-1] = ({a-1})
        renketu[a-1].add(b-1)

    F_G[a-1].append(b-1)
    F_G[b-1].append(a-1)


sub = list(range(N))
for i in sub:
    


# sub = list(range(N))
# # bfsでラベル付けすることで連結成分を作成
# for i in sub:
#     if label[i] == -1:
#         bfs(F_G, i)
#
# c = collections.Counter(label)
# for i, j in c.items():
#     size[i] = j
# print(size)
# for _ in range(K):
#     c, d = map(int, input().split())
#     if label[c-1] == label[d-1]:
#         link[c-1] -= 1
#         link[d-1] -= 1
#     B_G[c-1].append(d-1)
#     B_G[d-1].append(c-1)


# for i in sub:
#     linked_node = [j for j, x in enumerate(label) if x == label[i]]
#     linked_num = len(linked_node)
#     next_to_num = len(F_G[i])
#     block_num = len([k for k in linked_node if k in B_G[i]])
#     if i != N-1:
#         print(linked_num - next_to_num - block_num - 1, end=" ")
#     else:
#         print(linked_num - next_to_num - block_num - 1)












# for i in sub:
#     can = list(range(N))
#     can.pop(i) # 自分自身を友達候補から削除
#     can = set(can)
#     can -= set(B_G[i])     # ブロック関係にある人を友達候補から削除
#     can -= set(F_G[i])     # 友達関係に既にある人を友達候補から削除
#     if label[i] != -1:
#         v = [l for l, x in enumerate(label) if x == label[i]]
#         v = set(v)
#     else:
#         v = bfs(F_G, i)    # 友達グラフ上でつながっている友達をsetで取得
#     can &= v               # 今の候補と積集合とって完成
#     if i != N-1:
#         print(len(can), end=" ")
#     else:
#         print(len(can))
