# 백준 4386번 별자리 만들기 : https://www.acmicpc.net/problem/4386

from collections import defaultdict, deque
import heapq as hq
import math
import sys
input = sys.stdin.readline

n = int(input())
loc = [list(map(float, input().split())) for _ in range(n)]
graph = []
parent = [i for i in range(n)]
sum = 0

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

for i in range(n):
    for j in range(i + 1, n):
        line = math.sqrt((loc[i][0] - loc[j][0]) ** 2 + (loc[i][1] - loc[j][1]) ** 2)
        graph.append([i, j, line])
        
graph.sort(key=lambda x: (x[2], x[0]))

for a, b, cost in graph:
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        sum += cost
        
print("%0.2f" % sum)

# 알고리즘 : 최소 스패닝 트리
'''
풀이 : 이중 for문으로 모든 좌표간 거리를 구해 graph에 저장한 후, 거리를 오름차순 정렬하여 union/find로 연결한다.
별들 간 거리는 피타고라스 공식으로 구한다. -> ((x좌표 차의 제곱 + y좌표 차의 제곱)의 제곱근)
거리가 짧은 것부터 연결하는 것이 유리하기 때문에 거리순으로 정렬한다.
find 함수를 통해 두 별의 그룹이 같은지 검사한다. 만약 그룹이 다르다면, union함수로 연결한다.
정렬할 때 거리가 같다면 별 인덱스가 작은 걸 우선으로 정렬하게 해두었기 때문에 0번 별을 기준으로 그룹화 된다.
union으로 연결할 때마다 연결값을 sum에 저장한다.
'''
