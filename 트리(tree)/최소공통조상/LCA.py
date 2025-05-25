# 백준 11437번 LCA : https://www.acmicpc.net/problem/11437

from collections import defaultdict, deque
import heapq as hq
import math
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n = int(input())
graph = [[] for _ in range(n + 1)]
for i in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

parent = [0] * (n + 1)
depth = [0] * (n + 1)
chk = set()
chk.add(1)
def DFS(k, d):
    depth[k] = d
    for nx in graph[k]:
        if nx not in chk:
            chk.add(nx)
            parent[nx] = k
            DFS(nx, d + 1)
DFS(1, 0)
        
m = int(input())
for i in range(m):
    a, b = map(int, input().split())
    if depth[b] > depth[a]: a, b = b, a
    while a != b:
        if depth[a] != depth[b]: a = parent[a]
        else:
            a = parent[a]
            b = parent[b]
    print(a)

# 알고리즘 : 최소 공통 조상(LCA) 알고리즘
'''
풀이 : 두 노드의 깊이가 같아질 때까지 부모노드로 올리고, 같아지면 두 노드를 함께 올리며 만나는 노드를 출력한다.
간선들을 DFS로 탐색하면서 깊이와 부모 정보를 저장한다.
이 후, 노드 쌍이 입력되면, 둘 중 더 깊은 노드를 다른 노드와 깊이가 같아질 때까지 올린다.
깊이가 같아지면, 두 노드가 만날 때까지 모두 부모 노드로 올린다.
'''
