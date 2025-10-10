# 백준 1602번 도망자 원숭이 : https://www.acmicpc.net/problem/1602

import sys
input = sys.stdin.readline

n, m, q = map(int, input().split())
dog = list(map(int, input().split()))
INF = 1e9
graph = [[[INF, max(dog[i], dog[j])] for j in range(n)] for i in range(n)]
    
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a - 1][b - 1][0] = graph[b - 1][a - 1][0] = c

dog = sorted([(dog[i], i) for i in range(n)])
    
for dly, k in dog:
    for i in range(n):
        for j in range(i + 1, n):
            ij_sum = graph[i][j][0] + graph[i][j][1]
            ikj_max = max(graph[i][k][1], graph[k][j][1])
            ikj_sum = graph[i][k][0] + graph[k][j][0]
            if ij_sum >= ikj_sum + ikj_max:
                graph[i][j][0] = graph[j][i][0] = ikj_sum
                graph[i][j][1] = graph[j][i][1] = ikj_max

for _ in range(q):
    a, b = map(int, input().split())
    print(sum(graph[a - 1][b - 1]) if graph[a - 1][b - 1][0] < INF else -1)

# 알고리즘 : 플로이드-워셜 + 그리디
'''
풀이 : 멍멍이가 방해하는 시간이 작은 도시부터 오름차순 정렬하여 경유지를 설정하고 플로이드-워셜을 수행한다.
가중치가 있는 정점에서의 플로이드 워셜은 반드시 가장 작은 가중치를 가진 정점부터 탐색해야 한다.
왜냐하면 앞에서 간선 가중치가 크고 정점 가중치가 낮은 경우가 이 후의 간선 가중치가 작고, 정점 가중치가 큰 경우에 영향을 주기 때문이다.
예를 들면 다음과 같다.
간선 가중치가 5, 정점 가중치가 3인 루트 a(8)가 간선 가중치가 2, 정점 가중치가 9인 루트b(11) 보다 합이 더 낮으므로 우선된다.
그러나 멍멍이가 방해하는 정점은 최대 가중치를 가진 정점 단 하나이다.
만약 정점 가중치가 10이며 해당 노드로 가는 간선 가중치가 5인 경로가 들어왔을 경우에 두 가중치를 계산하면 다음과 같다.
a 루트 : 5 + 5 + 10 = 20
b 루트 : 2 + 5 + 10 = 17
이렇게 초기에 배제된 b 루트가 더 적은 가중치를 가지게 된다.
이를 위해 멍멍이가 방해하는 시간을 인덱스와 묶은 후, 시간 기준 오름차순 정렬하여 가장 적게 방해하는 도시부터 탐색한다.

플로이드 워셜을 돌때는 매 루트 비교별로 최대 방해시간을 따로 빼서 계산한다.
위에 말했듯, 최대 가중치를 가진 정점 하나만 계산하기 위해서다.
간선에 대한 최소 가중치는 간선정보만 가지고 일반적인 플로이드-워셜로 탐색한다. 
'''
