# 백준 3176번 도로 네트워크 : https://www.acmicpc.net/problem/3176

from collections import defaultdict, deque
import heapq as hq
import math
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n = int(input())
logn = math.ceil(math.log2(n))
graph = [[] for _ in range(n + 1)]
depth = [0] * (n + 1)
parent = [[0] *(n + 1) for _ in range(logn)]
cost = [[[1e12, 0] for _ in range(n + 1)] for _ in range(logn)]

for _ in range(n - 1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
    
que = deque()
que.append((1, 0))
chk = set()
chk.add(1)
while que:
    now, d = que.popleft()
    depth[now] = d
    for nx, val in graph[now]:
        if nx not in chk:
            parent[0][nx] = now
            cost[0][nx] = [val, val]
            chk.add(nx)
            que.append((nx, d + 1))
            
for i in range(logn - 1):
    for j in range(1, n + 1):
        parent[i + 1][j] = parent[i][parent[i][j]]
        cost[i + 1][j][0] = min(cost[i][j][0], cost[i][parent[i][j]][0])
        cost[i + 1][j][1] = max(cost[i][j][1], cost[i][parent[i][j]][1])
        
m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    minlen, maxlen = 1e12, 0
    if depth[a] < depth[b]: a, b = b, a
    diff = depth[a] - depth[b]
    for j in range(logn):
        if diff & (1 << j):
            minlen = min(cost[j][a][0], minlen)
            maxlen = max(cost[j][a][1], maxlen)
            a = parent[j][a]
            if depth[a] == depth[b]:break
    if a == b: print(minlen, maxlen)
    else:
        for j in range(logn - 1, -1, -1):
            if parent[j][a] != parent[j][b]:
                minlen = min(cost[j][a][0], cost[j][b][0], minlen)
                maxlen = max(cost[j][a][1], cost[j][b][1], maxlen)
                a = parent[j][a]
                b = parent[j][b]
        minlen = min(cost[0][a][0], cost[0][b][0], minlen)
        maxlen = max(cost[0][a][1], cost[0][b][1], maxlen)
        print(minlen, maxlen)

# 알고리즘 : 최소 공통 조상(LCA) 알고리즘
'''
풀이 : 두 노드의 최소 공통 조상까지 오는 최소 거리, 최대 거리를 각각 구하고, 한번 더 비교한다.
기본적으로 두 노드의 거리를 구하는 문제와 로직은 동일하되, cost 배열에 최소값, 최대값 계산 결과를 저장한다.
탐색 시, 조상 노드로 이동할 때마다 해당 노드에서의 최소값, 최대값을 계속 계산해준다.
'''
