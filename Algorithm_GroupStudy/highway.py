# 백준 1884번 고속도로 : https://www.acmicpc.net/problem/1884

import heapq as hq
import math
from copy import deepcopy
import sys
input = sys.stdin.readline

k = int(input())
n = int(input())
r = int(input())
roads = [[] for _ in range(n + 1)]
for _ in range(r):
    tmp = tuple(map(int, input().split())) # 출발, 도착, 길이, 통행료
    roads[tmp[0]].append((tmp[1], tmp[2], tmp[3]))
    
que = [(0, 0, 1)]  # 이동거리, 통행료, 도시
chk = [[1e12 for _ in range(k + 1)] for _ in range(n + 1)]
chk[1][0] = 0
while que:
    dist, cost, now = hq.heappop(que)
    if dist > chk[now][cost]: continue
    
    for nx, di, co in roads[now]:
        if cost + co <= k and dist + di < chk[nx][cost + co]:
            chk[nx][cost + co] = dist + di
            hq.heappush(que, (dist + di, cost + co, nx))
            
m = min(chk[n])
print(m if m < 1e12 else -1)

# 알고리즘 : 다익스트라
'''
풀이 : 각 비용당 최소 거리를 다익스트라로 탐색한 뒤, n번 도시에서 모든 비용을 비교해서 가장 짧은 이동거리를 구한다.
일반적인 다익스트라와 다르게 2차원 배열을 사용하여 거리를 체크한다.
이를 위해 각 도시별로 k(준비한 비용)만큼의 최단거리 저장 배열을 둔다.
각 도시에 도착하는데 드는 비용을 인덱스로하여 각 비용마다 최단 거리를 다익스트라로 구한다.
이 때, 만약 다음 도시까지 드는 비용이 k보다 크다면 불가능한 경로이기 때문에 탐색하지 않는다.

모든 비용에서의 최단 거리가 구해졌다면, n번도시의 모든 비용을 비교하여 그중 가장 짧은 거리를 구해 출력한다.
만약 최단거리가 임의로 설정한 최대값(1e12)과 같다면, 어떤 경로로도 n번 도시에 도착하지 못했으므로 -1을 출력한다.
'''
