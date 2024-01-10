# 백준 1753번 최단경로 : https://www.acmicpc.net/problem/1753

from collections import defaultdict, deque
from functools import cmp_to_key
import heapq as hq
import math
import sys
input = sys.stdin.readline

v, e = map(int, input().split())
k = int(input())
graph = [[] for _ in range(v + 1)]
cost = [1e9] * (v + 1)
for i in range(e):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    
heap = []
hq.heappush(heap, (0, k))

while heap:
    co, now = hq.heappop(heap)
    for nx in graph[now]:
        if nx != k and co + nx[1] < cost[nx[0]]:
            cost[nx[0]] = co + nx[1]
            hq.heappush(heap, (cost[nx[0]], nx[0]))
            
for i in range(1, v + 1):
    if i == k : print(0)
    elif cost[i] == 1e9: print("INF")
    else: print(cost[i])

# 알고리즘 : 다익스트라
'''
풀이 : 정점 k로 부터 모든 노드에 대한 최단 거리를 다익스트라로 계산한다.
cost 배열에 시작 정점 k에서 특정 정점까지 가는 비용을 모두 임의로 1e9로 저장한다.
k에서 특정 정점까지 직접 가는 방법(cost[nx])보다 어떤 정점 now를 거쳐 가는 방법이 더 짧다면 cost를 교체한다.
모든 정점을 탐색하며 cost가 최종 교체되었으면 차례대로 출력한다.

단, 다익스트라에서는 일반적인 BFS 처럼 방문체크를 해서는 안된다.
이미 방문한 정점이더라도 다음 방문에서 더 짧은 가중치가 나오면 교체해야하기 때문이다.
'''
