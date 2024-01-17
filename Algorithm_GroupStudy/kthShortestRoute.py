# 백준 1854번 K번째 최단경로 찾기 : https://www.acmicpc.net/problem/1854

from collections import defaultdict, deque
import heapq as hq
import math
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    
dist = [[] for _ in range(n + 1)]
dist[1].append(0)
heap = [(0, 1)]
    
while heap:
    cost, now = hq.heappop(heap)
                
    for nx, co in graph[now]:
        if len(dist[nx]) < k:
            hq.heappush(dist[nx], -(cost + co))
            hq.heappush(heap, (cost + co, nx))
        elif dist[nx][0] < -(cost + co):
            hq.heappop(dist[nx])
            hq.heappush(dist[nx], -(cost + co))
            hq.heappush(heap, (cost + co, nx))
            
for i in range(1, n + 1):
    print(-dist[i][0] if len(dist[i]) == k else -1)

# 알고리즘 : 다익스트라
'''
풀이 : 다익스트라를 수행하되, 최단 거리를 비교를 우선순위 큐를 이용해 수행한다.
기존 다익스트라는 dist 배열을 값으로 저장하지만, k번째 최단경로를 저장하기 위해 heap으로 저장한다.
1번 도시로 가는 1번째 최단 경로는 움직이지 않는 것으로 0을 dist[1]에 초기값으로 저장해준다.

다익스트라 수행은 다음과 같이 진행한다. 
모든 도시에 대해 모든 경로 중 가장 짧은 3개만 유지하기 위해 각 우선순위 큐는 최대 힙으로 설정한다.
1. 만약 dist[nx]가 k보다 작으면 아직 k개의 경로가 저장되지 않았다는 뜻이므로 그냥 현재 경로를 추가한다.
2. 만약 k개의 경로가 있다면 dist[nx]의 top과 현재 경로를 비교한다.
  2-1) 현재 경로가 더 짧다면 dist[nx]에서 top을 pop해주고, 현재 경로를 push한다.
 
모든 다익스트라 탐색이 끝났다면, 각 우선순위 큐의 top을 순서대로 출력한다.
이 때, 우선순위 큐의 길이가 k보다 작다면, k번째 경로를 구할 수 없으므로 -1을 출력한다.
'''
