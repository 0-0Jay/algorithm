# 백준 1922번 네트워크 연결 : https://www.acmicpc.net/problem/1922

from collections import defaultdict, deque
import heapq as hq
import math
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [list(map(int, input().split())) for i in range(m)]
parent = [i for i in range(n + 1)]
graph.sort(key=lambda x : (x[2], x[0]))

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

cost = 0
for i in range(m):
    if find(parent, graph[i][0]) != find(parent,graph[i][1]):
        union(parent, graph[i][0], graph[i][1])
        cost += graph[i][2]
        
print(cost)

# 알고리즘 : 최소 스패닝 트리
'''
풀이 : 네트워크 연결 비용을 기준으로 오름차순 정렬하여 union/find로 연결한다.
비용이 작은 네트워크부터 연결하고, find를 통해 이미 같은 네트워크에 소속된 컴퓨터면 연결하지 않는다.
union 함수를 통해 연결하면서 cost에 해당 연결에 대한 비용을 누적한다.
'''
