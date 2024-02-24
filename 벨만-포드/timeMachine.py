# 백준 11657번 타임머신 : https://www.acmicpc.net/problem/11657

from collections import defaultdict, deque
import math
import heapq as hq
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
route = [list(map(int, input().split())) for _ in range(m)]
INF = 1e9

dist = [INF] * (n + 1)
dist[1] = 0
cycle = False
for i in range(1, n + 1):
    for a, b, cost in route:
        if dist[a] != INF and dist[b] > dist[a] + cost:
            dist[b] = dist[a] + cost
            if i == n: cycle = True
            
if cycle:
    print(-1)
else:
    for i in range(2, n + 1):
        print(dist[i] if dist[i] < INF else -1)

# 알고리즘 : 벨만-포드
'''
풀이 : 간선을 최단경로의 비용으로 전환해주는 작업을 n번 수행한다.
간선에 음의 가중치가 있기 때문에 일반적인 다익스트라로 해결할 수 없다.
입력된 간선 정보를 그래프화 하지 않고 바로 탐색을 수행한다.
1번 정점에서 출발하기 때문에 dist[1]을 0으로 미리 설정해두고 시작한다.
모든 간선정보에 따른 dist의 최신화를 총 정점 갯수 - 1번 만큼 수행하면 최단거리 계산이 완료된다.
이 때, 1번 더 수행했을 때도 최단거리에 대한 최신화가 수행된다면, 이는 음의 간선에 의한 무한 사이클이 발생했다는 의미이다.
'''
