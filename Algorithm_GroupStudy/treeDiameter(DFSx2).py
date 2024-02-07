# 백준 트리의 지름 : https://www.acmicpc.net/problem/1167

from collections import defaultdict, deque
import heapq as hq
import math
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n = int(input())
graph = [[] for _ in range(n + 1)]
for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(1, len(tmp) - 1, 2):
        graph[tmp[0]].append(tmp[j:j + 2])

chk = set()      
max_depth = 0
max_node = -1
def DFS(k, cost):
    global max_depth, max_node
    if max_depth < cost:
        max_node = k
        max_depth = cost        
    for nx, val in graph[k]:
        if nx not in chk:
            chk.add(nx)
            DFS(nx, cost + val)
            chk.remove(nx)
   
chk.add(1)
DFS(1, 0)
chk.remove(1)
chk.add(max_node)
DFS(max_node, 0)
print(max_depth)

# 알고리즘 : DFS
'''
풀이 : 임의 노드로 DFS를 수행해 가장 멀리있는 노드를 찾고, 그 노드에서 DFS를 수행해 가장 멀리 있는 노드를 구한다.
어떤 노드에서 출발하던 가장 멀리있는 노드는 가장 멀리 떨어진 두 노드 중 하나가 나온다.
따라서 가장 멀리 떨어진 노드를 찾아 해당 노드에서 가장 멀리 있는 노드를 구하면 트리의 지름을 구할 수 있다.
''' 
