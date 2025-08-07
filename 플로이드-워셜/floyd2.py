# 백준 11780번 플로이드 2 : https://www.acmicpc.net/problem/11780

import sys
input = sys.stdin.readline
INF = 1e12
n = int(input())
m = int(input())
graph = [[INF if i != j else 0 for j in range(n + 1)] for i in range(n + 1)]
route = [[tuple() for _ in range(n + 1)] for _ in range(n + 1)]

for i in range(m):
    a, b, c = map(int, input().split())
    if c < graph[a][b]:
        graph[a][b] = c
        route[a][b] = (a, b)

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]
                route[i][j] = route[i][k][:-1] + route[k][j]
                
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(graph[i][j] if graph[i][j] < INF else 0, end = " ")
    print()
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(len(route[i][j]), *route[i][j])


# 알고리즘 : 플로이드-워셜
'''
풀이 : 비용과 경로를 저장해두고, 플로이드 워셜을 수행하면서 비용 감소로 인한 교체 발생마다 경로도 함께 교체한다.
일반적인 플로이드-워셜과 동일하게 수행 하되, 경로 교체만 추가로 처리해주면 된다.
두 경로를 합칠 때, i -> k 와 k -> j가 합쳐지므로 k가 중복된다.
이를 제거하기 위해 슬라이싱으로 한쪽 k를 잘라내어 합쳐준다.
'''
