# 백준 2307번 도로검문 : https://www.acmicpc.net/problem/2307

from collections import defaultdict, deque
import copy
from functools import cmp_to_key
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

dist = []
route = [[] for _ in range(n + 1)]
def dijkstra(st):
    global graph, route, dist
    dist = [1e12] * (n + 1)
    dist[st] = 0
    heap = []
    hq.heappush(heap, (0, st))

    while heap:
        cost, now = hq.heappop(heap)
        
        for nx, co in graph[now].items():
            if nx != st and dist[nx] > cost + co:
                dist[nx] = cost + co
                hq.heappush(heap, (dist[nx], nx))
                route[nx].clear()
                route[nx].append(now)
            elif dist[nx] == cost + co:
                route[nx].append(now)
                
    return dist[n]

time = dijkstra(1)  # 막지 않았을 때의 시간
result = copy.deepcopy(route)  # 다음 다익스트라가 최초 최단루트에 영향을 주지 않도록 깊은 복사
max_delay = 0
que = deque()
que.append(n)
while que:
    now = que.popleft()
    if len(result[now]) > 1:  # 만약 현재 지점으로 올 수 있는 최단 경로가 2개 이상이면 막아도 의미 없음
        for bef in result[now]:  # 따라서 경로만 넣어주고 continue
            que.append(bef)
        continue
    for bef in result[now]:
        tmp = graph[bef][now]
        graph[bef][now] = graph[now][bef] = 1e12
        now_time = dijkstra(1)  # 도로를 막고 다익스트라
        delay = now_time - time if now_time != 1e12 else 1e12  # 만약에 완전 봉쇄되었으면 1e12로 지정
        max_delay = max(max_delay, delay)
        graph[bef][now] = graph[now][bef] = tmp
        que.append(bef)
        
print(max_delay if max_delay < 1e12 else -1)

# 알고리즘 : 다익스트라
'''
풀이 : 다익스트라로 최단 경로를 구하고, 최단 경로에 포함된 도로를 하나씩 막으며 최대 딜레이 시간을 계산한다.
최단 경로에 포함되지 않은 도로는 계산할 필요가 없다.
왜냐하면 막아봤자 최단 경로로 도주하면 delay를 전혀 시킬 수 없기 때문이다.
따라서 최단 경로에 포함된 도로만 route를 통해 알아내고, BFS로 역추적하며 도로를 봉쇄해본다.
도로 봉쇄 후, 다익스트라를 수행했을 때, 걸리는 최소 시간과 최초의 도주 시간의 차가 delay 시간이다.
각 도로별로 봉쇄 시 delay시간 중 최대 값을 구한다.

만약 한번이라도 딜레이 시간이 1e12면 완전 봉쇄되었으므로 -1을 출력한다.
'''

