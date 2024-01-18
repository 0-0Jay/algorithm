# 백준 2325번 개코전쟁 : https://www.acmicpc.net/problem/2325

from collections import defaultdict, deque
import heapq as hq
import math
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [{} for _ in range(n + 1)]
for i in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    graph[b][a] = c

route = [[] for _ in range(n + 1)]
def dijkstra(st):
    global route
    heap = [(0, st)]
    dist = [1e12] * (n + 1)
    dist[st] = 0
    while heap:
        cost, now = hq.heappop(heap)
        if cost > dist[now]: continue  # 만약 현 지점까지의 비용이 dist에 기록된 비용보다 크다면 더 탐색할 필요 없음
        for nx, co in graph[now].items():
            if cost + co < dist[nx]:
                dist[nx] = cost + co
                hq.heappush(heap, (dist[nx], nx))    
                route[nx].clear()  # 더 빠른 경로가 발견되면 route를 비워주고 발견한 경로 추가
                route[nx].append(now)
            elif cost + co == dist[nx]:
                route[nx].append(now)
    return dist
    
max_time = dijkstra(1)[n]
shortcut = []
que = deque()
que.append(n)
chk = set()
while que:
    now = que.popleft()
    if now in chk: continue  # 이전에 한번 탐색한 시작점이면 중복탐색하지 않도록 체크
    chk.add(now)
    for nx in route[now]:
        que.append(nx)
        if len(route[now]) == 1:  # 경로가 유일한 경우만 선별
            shortcut.append((now, nx))
        
for a, b in shortcut:
    tmp, graph[a][b], graph[b][a] = graph[a][b], 1e12, 1e12
    max_time = max(max_time, dijkstra(1)[n])
    graph[a][b] = graph[b][a] = tmp
    
print(max_time)

# 알고리즘 : 다익스트라
'''
풀이 : 최단거리가 되는 루트를 기록해두고, 해당 루트에 해당하는 도로를 하나씩 부숴보며 최대값을 찾는다.
최초로 다익스트라를 돌려서 max_time에 저장한다.
도로를 부순 후의 최단거리는 반드시 최초의 최단거리보다 길 것이기 때문이다.
최초의 최단거리를 구하면서 route에 최단거리에 사용된 경로를 모두 기록해둔다.

route에 기록된 경로를 이용해 n부터 역추적하며 파괴할 도로를 선별한다.
만약 a -> b의 경로가 2개 이상이라면, 어떤 도로를 파괴해도 최단거리가 나올 것이므로 파괴하는 의미가 없다.
따라서 a -> b의 경로가 1개인 경우만 shortcut 배열에 추가해주고, 아닌 경우는 BFS 탐색에만 사용한다.
유일한 경로를 모두 선별했다면, 하나씩 파괴해보며 다익스트라를 돌리며, 가장 긴 경로를 찾는다.
'''
