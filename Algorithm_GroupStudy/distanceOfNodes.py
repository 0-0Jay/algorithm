# 백준 1761번 정점들의 거리 : https://www.acmicpc.net/problem/1761

from collections import defaultdict, deque
import math
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n = int(input())
logn = math.ceil(math.log2(n))
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
parent = [[0] * (n + 1) for _ in range(logn)]
cost = [[0] * (n + 1) for _ in range(logn)]
depth = [0] * (n + 1)

que = deque([(1, 0)])
chk = set([1])
while que:
    now, d = que.popleft()
    depth[now] = d
    for nx, val in graph[now]:
        if nx not in chk:
            chk.add(nx)
            que.append((nx, d + 1))
            parent[0][nx] = now
            cost[0][nx] = val
            
for i in range(logn - 1):
    for j in range(1, n + 1):
        parent[i + 1][j] = parent[i][parent[i][j]]
        cost[i + 1][j] = cost[i][j] + cost[i][parent[i][j]]
        
m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    dist = 0
    if depth[a] < depth[b]: a, b = b, a
    diff = depth[a] - depth[b]
    for i in range(logn):
        if diff & (1 << i):
            dist += cost[i][a]
            a = parent[i][a]
        if depth[a] == depth[b]: break
    if a == b: print(dist)
    else:
        for i in range(logn - 1, -1, -1):
            if parent[i][a] != parent[i][b]:
                dist += cost[i][a] + cost[i][b]
                a = parent[i][a]
                b = parent[i][b]
        print(dist + cost[0][a] + cost[0][b])

# 알고리즘 : 최소 공통 조상(LCA)
'''
풀이 : 부모 정보를 기록할 희소배열과 거리 정보를 기록할 희소배열을 생성하여 탐색한다.
양방향 트리의 특성상 루트 노드는 아무 지점이나 잡아도 무관하므로 편의상 1번으로 잡는다.
1번 트리를 기준으로 입력받았던 간선정보를 이용해 BFS로 트리 자료를 만든다.
트리 자료를 만들면서, parent와 cost에 해당 노드의 부모 노드와 부모 노드까지의 거리를 기록한다.
DP를 사용해서 parent와 cost를 희소배열로 만든다.
이를 이용해 최소 공통 조상을 찾고, 두 노드가 최소 공통 조상까지 오는 거리를 구해 더한다.
'''
