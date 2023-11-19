# 백준 1647번 도시 분할 계획 : https://www.acmicpc.net/problem/1647

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]
arr.sort(key = lambda x : (x[2]))
parent = [0] + [i for i in range(1, n + 1)]
chk = []
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
        chk.append(node[2])
        sum += node[2]
        

print(sum - max(chk))

# 알고리즘 : 크루스칼 알고리즘
'''
풀이 : 크루스칼 알고리즘을 이용해 최소 신장 트리를 구하고, 트리의 간선중 가장 비싼 간선을 끊는다.
최소 신장트리를 구하면서 sum에 총 유지비를 더하고, chk에 유지비를 append해준다.
이러면 sum에는 총 유지비가, chk에는 간선별 유지비가 기록된다.
이 후, chk에서 가장 비싼 간선을 끊으면(sum - max(chk)) 가장 싸게 두개의 마을로 분리할 수 있다.
'''    
