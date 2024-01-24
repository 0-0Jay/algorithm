# 백준 14621번 나만 안되는 연애 : https://www.acmicpc.net/problem/14621

import sys
input = sys.stdin.readline

def union(parent, a, b):
    rootA = find(parent, a)
    rootB = find(parent, b)
    if rootA != rootB:
        parent[rootB] = rootA
       
def find(parent, x):
    if parent[x] == x:
        return x
    parent[x] = find(parent, parent[x])
    return parent[x]

n, m = map(int, input().split())
mw = [0] + input().strip().split(" ")
parent = [i for i in range(n + 1)]
route = []
for i in range(m):
    a, b, c = map(int, input().split())
    if mw[a] != mw[b]: route.append([a, b, c])
route.sort(key=lambda x : x[2])

cost, path = 0, 0
for a, b, c in route:
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        cost += c
        path += 1
        
print(cost if path == n - 1 else -1)

# 알고리즘 : 크루스칼 알고리즘
'''
풀이 : 입력을 받을때, 서로 이성인 경우만 루트에 포함시켜서 union/find를 수행한다.
a, b, c학교를 입력받을 때 a, b가 같은 성이라면 조건에 따라 배제되기 때문에 계산에 포함시킬 이유가 없다.
입력단계에서 예외처리를 해주면 모든 간선을 거리 순으로 오름차순 정렬할 때 정렬할 데이터가 줄어든다.
정렬 후, 가장 작은 간선부터 union/find를 수행하면서 거리와 연결된 간선 수를 체크한다.
모든 학교가 연결되려면 간선의 수는 (학교의 수 - 1)이어야 한다.
따라서 간선 수가 올바른 개수라면 누적한 거리를 출력하고 아니라면 -1을 출력한다.
'''
