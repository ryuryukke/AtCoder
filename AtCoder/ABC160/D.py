from collections import deque
# 標準入力の高速化↓
# import sys
# input = sys.stdin.readline
def main(): # main()化することで,pythonによる変数アクセスコストが軽くなり,コード全体が高速化する
    n, x, y = map(int, input().split())
    g = dict()
    for i in range(n):
        if i == 0:
            g[i] = [i+1]
        elif i == n-1:
            g[i] = [i-1]
        else:
            g[i] = [i-1, i+1]
    g[x-1].append(y-1)
    g[y-1].append(x-1)
# print(g)
    distance = [0]*(n-1)
# 1番ノードから各ノードへの最短距離を求めていく.(BFS)
    for i in range(n):
        queue = deque()
        visited = [0]*n
    # まず処理される予定のノードが格納されているqueueに最初のノードを格納する
        queue.append(i)
        while queue:
            target = queue.popleft()
            for j in g[target]:
                if visited[j] == 0 or visited[j] > visited[target] + 1:
                    visited[j] = visited[target] + 1
                    queue.append(j)
        for k, a in enumerate(visited):
            if k > i:
                if a >= 1:
                    distance[a-1] += 1
    # print(f"{i}番ノードからの各ノードへの最短距離は{visited}である")
    print(*distance, sep="\n")
    # for l in distance:
    #     print(l)

if __name__ == "__main__":
    main()

"""
Pythonでの添字アクセスは本当に遅いので,インデックスが必要なときは,enumerateを使おう
    for k in range(len(visited)):
        if k > i:
            if visited[k] >= 1:
                distance[visited[k]-1] += 1
"""
# 二次元配列の初期化
# l = [[None] * N for _ in range(N)]
# A.sort(key=lambda x: x[1])

# 特定の条件のデータを数える
# data = range(1,10)
# cnt = len[x for x in data if x % 3 == 0]
