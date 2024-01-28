# 백준 2611번 자동차경주 : https://www.acmicpc.net/problem/2611

from collections import defaultdict, deque
import heapq as hq
import math
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
bef = [0] * (n + 1)
cost = [0] * (n + 1)
route = [0] * (n + 1)
for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    bef[b] += 1
    
que = deque()
que.append((1, 0))

while que:
    now, tmp = que.popleft()
    
    for nx, co in graph[now]:
        if cost[nx] < tmp + co:
            route[nx] = now
            cost[nx] = tmp + co
        bef[nx] -= 1
        if bef[nx] == 0 and nx != 1:
            que.append((nx, cost[nx]))
            
print(cost[1])
cos = [1]
while route[cos[-1]] != 1:
    cos.append(route[cos[-1]])
print(1, *reversed(cos))

# 알고리즘 : 위상 정렬 + DP
'''
풀이 : 어떤 정점을 향하고 있는 루트의 값들 중 최대값을 해당 정점에 기록하면서 순회한다.
입력 단계에서 위상 정렬을 활용하기 위해 bef 배열에 이전 노드가 있음을 카운팅하며 graph를 채워넣는다.
반드시 1로 시작하기 때문에 que에 1을 넣고 BFS를 수행한다.
(현재 노드에 저장된 값 + 간선의 점수)를 다음 노드에 저장된 비용과 비교해 더 큰값으로 저장한다.
이 때, 값 교체가 일어났다면, route에 현재 노드를 기록하여 후에 역추적으로 경로를 추적할 수 있게 한다.
값 교체가 일어나지 않았더라도 해당 간선은 계산에서 제외된 간선이므로 bef에서 -1해준다.
만약 다음 노드의 bef가 0이라면 모든 간선이 계산되어 있으므로 que에 넣어준다.
모든 계산이 끝났다면, 1로 돌아오기 때문에 cos[1]을 출력하고, route를 역추적하여 이동 경로를 출력한다.
'''
