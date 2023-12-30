# 백준 1833번 고속철도 설계하기 : https://www.acmicpc.net/problem/1833

from collections import defaultdict, deque
import heapq as hq
import math
import sys
input = sys.stdin.readline

n = int(input())
cost = 0
graph = []
for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(i + 1,n):  # i + 1부터만 graph에 저장해서 탐색할 루트를 최소화 한다.
        if tmp[j] < 0: cost += -tmp[j]
        graph.append([i, j, tmp[j]])
graph.sort(key = lambda x : (x[2], x[0]))
parent = [i for i in range(n + 1)]

def union(parent, a, b):
    rootA = find(parent, a)
    rootB = find(parent, b)
    if rootA > rootB:
        parent[rootA] = rootB
    else:
        parent[rootB] = rootA
        
def find(parent, x):
    if parent[x] == x:
        return x
    parent[x] = find(parent, parent[x])
    return parent[x]

cnt = 0
route = []
for a, b, co in graph:
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        if (co > 0):
            route.append((a, b))
            cost += co
            cnt += 1
            
print(cost, cnt)
for a, b in route:
    print(a + 1, b + 1)

# 알고리즘 : 최소 스패닝 트리
'''
풀이 : 행렬로 입력되는 철도 연결 정보에서 간선과 비용을 추출하여 union/find 방식으로 연결한다.
행렬 정보를 입력받을 때 양방향에 대한 정보로 입력된다.
그러나 두 지점의 고속철도는 방향성이 없기 때문에 대각선으로 대칭 구조를 띈다.
방향성이 없다면 굳이 양방향을 모두 계산할 필요가 없으므로 단방향에 대한 정보만 graph에 저장한다.
이 때, 두 지점을 연결하는데 드는 비용이 음수라면 이미 연결된 철도이므로 양수로 전환하여 cost에 저장한다.

graph를 cost로 오름차순 정렬하여 최소 비용이 드는 간선부터 연결한다.
만약 두 노드가 직접 연결되어 있지 않더라도, 다른 루트를 통해 간접적으로 연결이 되어 있다면 연결할 필요가 없다.
따라서 find로 간접적으로 연결되어 있는지 확인한다.
두 노드의 find가 서로 다르다면 서로 어떤 경로로도 연결되어 있지 않다는 의미이므로, 두 노드를 연결한다.
연결하면서 두 노드를 route에 append하고, cnt와 cost도 누적시킨다.
이 때, cost가 음수인 경우는 이미 설치된 철도이며, 입력받을 때 바로 계산했기 때문에 양수인 경우만 계산한다.
'''
