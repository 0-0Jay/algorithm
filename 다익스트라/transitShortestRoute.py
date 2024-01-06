# 백준 1504번 특정한 최단 경로 : https://www.acmicpc.net/problem/1504

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[1e12] * (n + 1) for _ in range(n + 1)]
for i in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = graph[b][a] = min(c, graph[a][b]) 
for i in range(1, n + 1):
    graph[i][i] = 0
v1, v2 = map(int, input().split())
dist = [1e12] * (n + 1)

def dijkstra(st):
    global dist
    dist = [1e12] * (n + 1)
    chk = [0] * (n + 1)
    dist[st] = 0
    idx = st
    for _ in range(n - 1):
        if idx == -1: break
        chk[idx] = 1
        s, min = -1, 1e12
    
        for i in range(1, n + 1):
            if chk[i] == 1: continue
            now = dist[idx] + graph[idx][i]
            if now < dist[i]:
                dist[i] = now
            if dist[i] < min:
                s, min = i, dist[i]
        idx = s

dijkstra(1)  # 1번을 정점으로 잡고 다익스트라를 돌리면 1 - v1과 1 - v2를 구할 수 있다.
st_v1 = dist[v1]
st_v2 = dist[v2]
dijkstra(v1)  # v1번을 정점으로 잡고 다익스트라를 돌리면 v1 - v2와 v1 - n을 구할 수 있다.
v1_v2 = dist[v2]
v1_n = dist[n]
dijkstra(v2)  # v2번을 정점으로 잡고 다익스트라를 돌리면 v2 - n을 구할 수 있다.
v2_n = dist[n]

ans = 1e12
ans = min(1e12, st_v1 + v1_v2 + v2_n, st_v2 + v1_v2 + v1_n)
if v1_v2 == 1e12 or ans == 1e12: print(-1)
else: print(ans)

# 알고리즘 : 다익스트라
'''
풀이 : 다익스트라를 3번 수행하여 모든 경로에 대한 최소값을 구한 후, 가장 짧은 노선을 선택한다.
1번, v1번, v2번 정점을 기준으로 다익스트라를 돌리면 모든 경로에 대한 최단 경로를 구할 수 있다.
문제에서 1에서 출발해 v1과 v2를 거쳐 n으로 가는 최단 경로를 구하라는 문제가 주어지는데 이는 두가지 경우가 있다.
1. v1을 먼저 거쳐가는 경우 : 1 -> v1 -> v2 -> n
2. v2를 먼저 거쳐가는 경우 : 1 -> v2 -> v1 -> n
1번 루트, 2번 루트를 구한 후, 더 작은 값을 출력하면 된다.

만약 v1과 v2를 연결하는 루트가 존재하지 않다면 두 노드를 경유하는 루트 자체가 불가능하다.
또한, ans가 1e12라면, 어떤 경우로도 경유 루트를 만들 수 없다는 의미다.
따라서 위 두 경우에는 -1을 출력한다.

얼핏 생각하면 왜 두가지 경우로 나누어야 하는지 의문이 들지만 반례가 존재한다.
1 - v2 - v1 - n 로 연결된 루트가 있다고 가정하자.
1번 방식으로 돌게 되면 1 -> v2 -> v1 -> v2 -> v1 -> n 이라는 상당히 비효율적인 루트를 타게 된다.
'''
