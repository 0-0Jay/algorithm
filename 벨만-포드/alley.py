# 백준 1738번 골목길 : https://www.acmicpc.net/problem/1738

from collections import defaultdict, deque
import math
import heapq as hq
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]
graph = [[] for _ in range(n + 1)]
for i in range(m):
    a, b, cost = arr[i]
    graph[b].append(a)

chk = set({n})    
que = deque([n])
while que:  # 내 경로 상에 사이클이 존재하는지 판별하기 위한 BFS
    now = que.popleft()
    for i in graph[now]:
        if i not in chk:
            chk.add(i)
            que.append(i)

INF = -1e9
dist = [(0, INF)] * (n + 1)
dist[1] = (0, 0)
cycle = False
for i in range(1, n + 1):
    for a, b, cost in arr:
        if dist[a][1] == INF: continue
        if dist[b][1] < dist[a][1] + cost:
            dist[b] = (a, dist[a][1] + cost)
            if i == n and a in chk: cycle = True

def DFS(n):  # 경로 역추적
    if n == 0: return
    DFS(dist[n][0])
    print(n, end=" ")
           
if cycle or dist[-1] == INF: print("-1")
else: DFS(n)

# 알고리즘 : 벨만-포드 + DFS + BFS
'''
풀이 : 내 경로 상에 존재하는 길만 골라서 벨만 포드를 수행한다.
처음 간선을 모두 입력받으면, BFS를 통해 나와 콘도 사이에 연결된 사이클만 골라낸다.
이 후, 간선내에서 벨만-포드를 수행하여 사이클이 발생하는지 여부를 판독한다.
이 때, 탐색하면서 더 많은 금품을 얻는 루트를 기록해야 하기때문에 dist에 금품 양과 이전 노드를 함께 저장해둔다.
cycle이 발생하지 않았고, 콘도에 금품양이 기록되어 있다면, DFS를 통해 경로를 역추적하여 출력한다.
'''
