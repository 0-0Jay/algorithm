# 백준 1717번 집합의 표현 : https://www.acmicpc.net/problem/1717

import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

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

n, m = map(int, input().split())
parent = [i for i in range(n + 1)]
arr = []
for i in range(m):
    c, a, b = map(int, input().split())
    if c == 0:
        if find(parent, a) != find(parent, b):
            union(parent, a, b)
    else:
        print("NO" if find(parent, a) != find(parent, b) else "YES")

# 알고리즘 : 크루스칼
'''
풀이 : 0이면 루트노드를 비교해 다르면 합치고, 1이면 루트노드를 비교해 결과값을 출력한다.
union 함수를 이용해 연결, find 함수를 이용해 루트노드를 찾는다.
'''
    
