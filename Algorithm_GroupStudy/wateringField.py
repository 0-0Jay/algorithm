# 백준 1368번 물대기 : https://www.acmicpc.net/problem/1368

import sys
input = sys.stdin.readline

n = int(input())
sum = 0
parent = [i for i in range(n + 1)]
route = []
for i in range(1, n + 1):
    route.append((int(input()), 0, i))

for i in range(1, n + 1):
    field = list(map(int, input().split()))
    for j in range(n):
        if i == j + 1: continue
        route.append((field[j], i, j + 1))
route.sort()

def find(parent, x):
    if parent[x] == x:
        return x
    parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b, cost):
    global sum
    rootA = find(parent, a)
    rootB = find(parent, b)
    
    if rootA != rootB:
        sum += cost
        parent[rootB] = rootA

for i in range(len(route)):
    cost, a, b = route[i]
    union(parent, a, b, cost)
    
print(sum)

# 알고리즘 : 크루스칼(union/find)
'''
풀이 : 어떤 가상의 노드를 루트로 잡고, 각 논에 우물을 파는 것을 루트와 연결한다고 생각한다.
어떤 논의 경우, 해당 논에서 우물을 파는 것이 다른 논에서 물을 댈 통로를 만드는 것보다 비용이 낮을 수 있음에 유의한다.
따라서 우물을 파는 비용을 가상 노드(0)에서 i번 우물로 통로를 만드는 비용으로 route에 저장한다.
모든 통로비용을 저장했다면, 정렬한 후 일반적인 크루스칼 알고리즘으로 모든 논을 연결하면 된다. 
'''
