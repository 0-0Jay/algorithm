# 백준 1162번 도로포장 : https://www.acmicpc.net/problem/1162

import heapq as hq
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))
    
dist = [[1e12 for _ in range(k + 1)] for _ in range(n + 1)]
dist[1] = [0] * (k + 1)
heap = [(0, 1, 0)]

while heap:
    cost, now, cnt = hq.heappop(heap)

    if dist[now][cnt] < cost:  # cost가 이미 기록된 최소 시간보다 크다면
        continue  # 이 후 탐색은 어짜피 전부 걸러질 것이므로 continue

    for co, nx in graph[now]:
        if dist[nx][cnt] > cost + co:  # 포장 안했을 경우
            dist[nx][cnt] = cost + co
            hq.heappush(heap, (dist[nx][cnt], nx, cnt))
        if cnt < k and dist[nx][cnt + 1] > cost:  # 포장 가능한 도로가 남아있을 때 포장한 경우
            dist[nx][cnt + 1] = cost
            hq.heappush(heap, (cost, nx, cnt + 1))

print(min(dist[n]))  # 도착 지점에서 각 포장 횟수 별 최소 비용 중 가장 작은 비용 출력

# 알고리즘 : 다익스트라
'''
풀이 : 다익스트라를 수행할 때, 도로를 포장한 횟수별로 나누어 체크한다.
cnt를 통해 도로를 포장한 횟수를 카운팅 하며 heap에 넣고 뺀다.
만약 cnt가 k보다 작은 경우 heap에는 다음 두 경우를 넣는다.
1. 다음 도로를 포장하지 않고 가는 최단 시간
2. 다음 도로를 포장하고 가는 최단 시간
이 때, 도로를 포장하면 다음 도로의 시간이 0으로 바뀌므로 다음 도로의 가중치를 추가하지 않고 계산한다.

이렇게 하면 도로를 n회 포장했을 때에 대한 각각의 최소 시간이 구해지는데, 이 중 가장 작은 값을 출력한다.
'''
