# 백준 13418번 학교 탐방하기 : https://www.acmicpc.net/problem/13418

from collections import defaultdict, deque
from functools import cmp_to_key
import heapq as hq
import math
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for i in range(m + 1):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])
    
def up(k, t):
    if k // 2 == 0: return
    if heap[k][1] * t < heap[k // 2][1] * t:
        heap[k], heap[k // 2] = heap[k // 2], heap[k]
        up(k // 2, t)
    
            
def down(k, t):
    sub = k * 2
    if sub >= len(heap): return
    if sub + 1 < len(heap) and heap[sub][1] * t > heap[sub + 1][1] * t:
        sub += 1
    if heap[k][1] * t > heap[sub][1] * t:
        heap[k], heap[sub] = heap[sub], heap[k]
        down(sub, t)
                
tmp = [0, 0, 0]
for case in (-1, 1):
    heap = [0]
    heap.append(graph[0][0])
    chk = set()
    chk.add(0)
    while len(heap) > 1:
        now, cost = heap[1]
        heap[1] = heap[-1]
        heap.pop(-1)
        down(1, case)
        
        if now not in chk:
            tmp[case] += cost ^ 1
            chk.add(now)
            
            for nx in graph[now]:
                heap.append(nx)
                up(len(heap) - 1, case)
                
print(tmp[1] ** 2 - tmp[-1] ** 2)

# 알고리즘 : 프림
'''
풀이 : 프림 알고리즘을 통해 최소 피로도 트리와 최대 피로도 트리를 만든다.
for문을 통해 case가 -1인 경우와 1인 경우를 계산했다.
up과 down을 통해 힙을 구현할 때, 파라미터로 case를 전달할 t를 하나 더 지정했다.
up과 down 내부에서 우선순위 계산을 수행할 때, t를 한번 곱하게 해뒀기 때문에 case에 따라 최대 신장 트리가 될지 최소 신장 트리가 될지 결정되게 만들었다.
다른 부분은 모두 기존의 프림 알고리즘과 동일하다.오전 11:49 2024-01-05

문제에서 주의할 사항이 있는데 오르막길이 0, 내리막길이 1이다.
즉, 평범하게 코드를 짜면 최소 트리에서 가장 많은 오르막길을, 최대 트리에서 가장 많은 내리막길을 가게된다.
따라서 tmp에 값을 누적할 때, 비트 XOR 연산자를 통해 1과 0을 반전시켜서 기록한다.
'''

'''
크루스칼 알고리즘으로 해결한 풀이

from collections import defaultdict, deque
from functools import cmp_to_key
import heapq as hq
import math
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for i in range(m + 1):
    a, b, c = map(int, input().split())
    graph.append([a, b, c ^ 1])
    
graph.sort(key = lambda x : x[2])
    
def union(parent, a, b):
    rootA = find(parent, a)
    rootB = find(parent, b)
    
    if rootA < rootB:
        parent[rootB] = rootA
    else:
        parent[rootA] = rootB
            
def find(parent, x):
    if parent[x] == x:
        return x
    parent[x] = find(parent, parent[x])
    return parent[x]

min, max = 0, 0
parent = [i for i in range(n + 1)]
for i in range(len(graph)):
    info = graph[i]
    if find(parent, info[0]) != find(parent, info[1]):
        union(parent, info[0], info[1])
        min += info[2]
        
parent = [i for i in range(n + 1)]       
for i in range(len(graph) - 1, -1, -1):
    info = graph[i]
    if find(parent, info[0]) != find(parent, info[1]):
        union(parent, info[0], info[1])
        max += info[2]
        
print(max ** 2 - min ** 2)
'''
