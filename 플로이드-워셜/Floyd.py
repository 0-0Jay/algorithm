# 백준 11404번 플로이드 : https://www.acmicpc.net/problem/11404

from collections import defaultdict, deque
import math
import heapq as hq
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

INF = 1e9   
cost = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1): cost[i][i] = 0

for i in range(m):
    a, b, c = map(int, input().split())
    cost[a][b] = min(c, cost[a][b])
    
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])
            
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(cost[i][j] if cost[i][j] < INF else 0, end = " ")
    print()

# 알고리즘: 플로이드-워셜
'''
풀이 : 최소 비용만 cost에 저장해두고, 플로이드 워셜을 수행한다.
i에서 j까지 바로 가는 비용과 i에서 k를 거쳐서 j로 가는 비용을 비교해 더 작은 값으로 교체하는 방식이다.
'''
