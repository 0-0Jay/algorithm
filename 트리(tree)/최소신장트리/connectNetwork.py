# 백준 1922번 네트워크 연결 : https://www.acmicpc.net/problem/1922

from collections import defaultdict, deque
from functools import cmp_to_key
import heapq as hq
import math
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
res = 0
cost = [[10001] * (n + 1) for _ in range(n + 1)]
for i in range(m):
    a, b, c = map(int, input().split())
    cost[a][b] = c
    cost[b][a] = c

chk = set()
que = []
hq.heappush(que, (0, 1))

while que:
    co, node = hq.heappop(que)
    
    if node not in chk:
        res += co
        chk.add(node)
        
        for i in range(1, n + 1):
            if cost[node][i] != 10001:
                hq.heappush(que, (cost[node][i], i))
    
print(res)

# 알고리즘 : 프림
'''
풀이 : 힙을 이용한 프림 알고리즘을 통해 최소 비용으로 네트워크를 연결한다.
노드를 연결할 때마다 그 노드와 연결된 다른 노드들을 힙에 넣는다.
힙에서 뺄때는 자연스럽게 현재 연결할 수 있는 네트워크 중 가장 작은 것이 빠져나온다.
'''
