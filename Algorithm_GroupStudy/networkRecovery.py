# 백준 2211번 네트워크 복구 : https://www.acmicpc.net/problem/2211

import heapq as hq
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
dist = [1e12] * (n + 1)
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

que = [(0, 1)]  # (시간, 노드)
network = [0] * (n + 1)
while que:
    time, now = hq.heappop(que)
    if time > dist[now]: continue
    for nx, co in graph[now]:
        if nx != 1 and dist[nx] > time + co:
            dist[nx] = time + co
            network[nx] = now
            hq.heappush(que, (dist[nx], nx))

result = []
for i in range(1, n + 1):
    if network[i] != 0:
        result.append((network[i], i))

print(len(result))
for a, b in result:
    print(a, b)

# 알고리즘 : 다익스트라
'''
풀이 : 다익스트라로 1번 컴퓨터에서 다른 모든 컴퓨터까지의 최단 거리를 구한 후, 사용된 경로를 출력한다.
다익스트라 수행 과정에서 갱신이 발생할때마다 network 배열에 바뀐 경로를 저장한다.
이 과정이 모두 수행되면, network배열의 각 인덱스에는 어떤 정점과 연결되어 있는지 기록되어 있다.
이 정점들을 배열에 쌓아서, 배열의 길이와 원소들을 출력한다.
'''
            
