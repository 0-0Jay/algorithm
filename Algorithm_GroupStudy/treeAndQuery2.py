# 백준 13511번 트리와 쿼리 2 : https://www.acmicpc.net/problem/13511

from collections import deque
import math
import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
    
parent = [[0] * (n + 1) for _ in range(19)]
cost = [[0] * (n + 1) for _ in range(19)]
depth = [0] * (n + 1)
que = deque([1])
chk = set({1})
while que:
    now = que.popleft()
    for nx, co in graph[now]:
        if nx not in chk:
            chk.add(nx)
            parent[0][nx] = now
            cost[0][nx] = co
            depth[nx] = depth[now] + 1
            que.append(nx)
    
for i in range(18):
    for j in range(1, n + 1):
        parent[i + 1][j] = parent[i][parent[i][j]]
        cost[i + 1][j] = cost[i][j] + cost[i][parent[i][j]]

m = int(input())
for _ in range(m):
    cmd = tuple(map(int, input().split()))
    a, b = u, v = cmd[1:3]
    if depth[v] > depth[u]: u, v = v, u
    diff = depth[u] - depth[v]
    lca = 0
    for i in range(18):
        if diff & (1 << i):
            u = parent[i][u]
            if depth[u] == depth[v]: break
    if u == v: lca = u
    else:
        for i in range(17, -1, -1):
            if parent[i][u] != parent[i][v]:
                u = parent[i][u]
                v = parent[i][v]
        lca = parent[0][u]
    if cmd[0] == 1:
       ans = 0
       a_diff = depth[a] - depth[lca]
       b_diff = depth[b] - depth[lca]
       for i in range(18):
           if a_diff & (1 << i):
               ans += cost[i][a]
               a = parent[i][a]
           if b_diff & (1 << i):
               ans += cost[i][b]
               b = parent[i][b]
       print(ans)
    else:
        k = cmd[-1]
        cnt = depth[a] - depth[lca]
        if k <= cnt:
            diff = k - 1
            for i in range(18):
                if diff & (1 << i):
                    a = parent[i][a]
            print(a)
        else:
            diff = (depth[b] - depth[lca]) - (k - cnt - 1)
            for i in range(17, -1, -1):
                if diff & (1 << i):
                    b = parent[i][b]
            print(b)

# 알고리즘 : LCA(최소 공통 조상) + 희소 배열(DP)
'''
풀이 : 희소 배열을 사용하여 최소 공통 조상을 찾고, 각 정점과의 깊이 차이를 활용한다.
어떤 명령(cmd[0])이 오든 최소 공통 조상을 찾아야 하므로 먼저 LCA 알고리즘을 수행한다.
(비용의 경우, LCA 알고리즘을 수행하며 바로 계산할 수 있기 때문에 그렇게 해도 무방하다.)

명령이 1인 경우에는 u -> v 경로의 비용을 계산한다.
u에서 v까지의 비용은 곧, u에서 LCA까지의 비용과 v에서 LCA까지의 비용을 합한 것과 같다.
희소배열을 이용해 2^i 씩 올려가며 비용을 계산한다.

명령이 2인 경우에는 u -> 경로에 존재하는 정점 중 u로부터 k번째 정점을 탐색한다.
이를 위해 처음 구했던 LCA의 깊이를 이용하여 LCA와 u의 깊이 차이를 구한다(cnt)
만약 쿼리 명령에 주어진 k의 값이 cnt 이하라면, v의 깊이는 고려하지 않아도 된다.
즉, k - 1만큼 a를 올려준 정점이 k번째 정점이된다.(k - 1인 이유는 a 정점을 포함하지 않기 때문)
반대로 cnt 보다 k가 크다면, k - cnt만큼 LCA에서 내려가면 된다.

그러나 희소배열의 탐색을 위해 올라가는 방식으로 바꿔주어야 한다.
이를 위해 LCA와 v의 깊이 차이 에서 k - cnt - 1를 뺀 만큼 올려 준다. (a와 같이 b 정점을 포함하지 않기 때문에 -1)
즉, LCA에서 k - cnt만큼 v쪽으로 내려간 정점이 K번째 정점이 된다.
'''
