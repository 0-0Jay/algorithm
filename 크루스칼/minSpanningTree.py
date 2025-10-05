# 백준 1197번 최소 스패닝 트리 : https://www.acmicpc.net/problem/1197

from collections import deque
import sys
input = sys.stdin.readline

v, e = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(e)]
arr.sort(key = lambda x : (x[2], x[0]))
parent = [0] + [i for i in range(1, v + 1)]
sum = 0

def find(parent, x):
    if parent[x] == x:
        return x
    parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    rootA = find(parent, a)
    rootB = find(parent, b)
    
    if rootA < rootB:
        parent[rootB] = rootA
    else:
        parent[rootA] = rootB
        
for node in arr:
    if find(parent, node[0]) != find(parent, node[1]):
        union(parent, node[0], node[1])
        sum += node[2]

print(sum)

# 알고리즘 : 크루스칼 알고리즘
'''
풀이 : 간선의 가중치를 오름차순으로 정렬하고, 최소값을 시작점으로 잡아 간선을 이어붙인다.
최소값부터 탐색하다가 모든 정점이 연결되면 그 값이 최소 신장 트리가 된다고 생각하는 그리디 알고리즘의 일환이다.
크루스칼 알고리즘을 위해 union find 함수를 활용한다.
1. find 함수를 통해 각 정점의 부모를 찾는다.
2. 만약 node[0]의 부모 정점과 node[1]의 부모 정점이 같다면, node[0]과 node[1]을 연결하면 순환이 발생하니 간선을 연결하지 않는다.
3. 만약 두 부모 정점이 다르면 정점을 union함수로 연결한다. parent에 각 간선의 부모 정점을 저장한다.
  3-1. union 함수에서 node[0]과 node[1]을 연결하면 node[1]의 부모 정점에 node[0]을 기록한다.
4. union함수로 간선이 연결되었다면 해당 간선의 가중치를 sum에 누적한다.
5. 1~4를 모든 노드만큼 반복한다.
'''
