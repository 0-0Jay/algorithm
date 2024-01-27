# 백준 11725번 트리의 부모 찾기 : https://www.acmicpc.net/problem/11725

import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n = int(input())
graph = [[] for _ in range(n + 1)]

for i in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
chk = set()
parent = [0] * (n + 1)
def search(k):
    for nx in graph[k]:
        if nx not in chk:
            parent[nx] = k
            chk.add(nx)
            search(nx)
            
chk.add(1)
search(1)
for i in range(2, n + 1):
    print(parent[i])

# 알고리즘 : 트리 탐색
'''
풀이 : 인접리스트로 각 노드 연결 정보를 기록한 뒤, 재귀로 탐색한다.
이 때, 입력이 반드시 정방향으로 주어진다는 보장이 없으므로 갔던 노드를 재방문 하지 않기 위해 중복체크도 해준다.
매 번 다음 노드의 부모에 현재 노드를 기록해주는 방식으로 진행한다.
'''
