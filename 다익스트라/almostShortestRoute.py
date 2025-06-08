# 백준 5719번 거의 최단 경로 : https://www.acmicpc.net/problem/5719

from collections import defaultdict, deque
from functools import cmp_to_key
import heapq as hq
import math
import sys
input = sys.stdin.readline

dist = []
route = []
def dijkstra(st):  # 다익스트라로 최단 경로 탐색
    global dist, route
    dist = [1e12] * n
    route = [[] for _ in range(n)]
    chk = [0] * (n)
    dist[st] = 0
    idx = st
    for _ in range(n - 1):
        if idx == -1: break
        chk[idx] = 1
        s, min = -1, 1e12
    
        for i in range(n):
            if chk[i] == 1: continue
            now = dist[idx] + graph[idx][i]
            if now < dist[i]:
                dist[i] = now
                route[i].clear()
                route[i].append(idx)
            elif now == dist[i]:
                route[i].append(idx)
            if dist[i] < min:
                s, min = i, dist[i]
        idx = s


def deleteShorcut(nd):  # 최단 경로 제거를 위한 BFS
    que = deque()
    que.append(nd)
    chk = set()
    chk.add(nd)
    while que:
        now = que.popleft()
        for bef in route[now]:
            graph[bef][now] = 1e12
            if bef in chk: continue
            que.append(bef)
            chk.add(bef)
        
while True:
    n, m = map(int, input().split())
    if n == 0: break
    st, ed = map(int, input().split())
    
    graph = [[1e12] * n for _ in range(n)]
    for i in range(m):
        a, b, c = map(int, input().split())
        graph[a][b] = min(c, graph[a][b]) 
    for i in range(n):
        graph[i][i] = 0
        
    dijkstra(st)  # 처음 찾은 최단 경로
    deleteShorcut(ed)  # 최단 경로 삭제
    dijkstra(st)  # 최단 경로를 삭제했을 때 최단 경로
    print(dist[ed] if min(1e12, dist[ed]) != 1e12 else -1)

# 알고리즘 : 다익스트라 + BFS
'''
풀이 : 다익스트라로 최단 경로를 찾은 후, BFS로 모든 최단 경로를 지우고 다시 다익스트라로 최단 경로를 찾는다.
먼저 다익스트라로 최단 경로를 찾고, 이 때 최단 경로를 전부 route배열에 저장해둔다.
즉, route 배열에 저장된 노드는 해당 노드에 최단 경로로 오는 이전 노드를 말한다.
ex) 3 -> 4로 1만에 오고, 5 -> 4로 1만에 오면 route[4]에는 [1, 5]가 저장.

처음 다익스트라를 수행하면 route 배열은 곧 최단 경로 정보를 저장한 인접리스트가 된다.
이 인접리스트를 BFS로 탐색하며 해당하는 경로를 graph에서 1e12로 변경하여 끊어준다.
이 때, 동일한 노드에 오는 최단 경로가 여러개 있을 수 있다.
따라서 불필요한 탐색을 수행하지 않게 이전에 탐색한 노드라면 que에 삽입하지 않는다.

BFS를 통해 최단 경로에 사용된 도로를 모두 끊어주었다면 다시 다익스트라를 수행하여 최단 거리를 구한다.
'''
