# 백준 13290번 - Big Truck : https://www.acmicpc.net/problem/13290

import heapq as hq
import sys
input = sys.stdin.readline

n = int(input())
box = [0] + list(map(int, input().split()))
route = [[] for _ in range(n + 1)]
for _ in range(int(input())):
    a, b, c = map(int, input().split())
    route[a].append((b, c))
    route[b].append((a, c))
dist = [(1e12, 0)] * (n + 1)
dist[1] = (0, box[1])
que = [(0, 1, box[1])]  # (길이, 현재 위치, 박스 수)

while que:
    d, now, b = hq.heappop(que)
    if d > dist[now][0]: continue
    for nx, co in route[now]:
        if dist[nx][0] > d + co or dist[nx][0] == d + co and dist[nx][1] <= b + box[nx]:
            hq.heappush(que, (d + co, nx, b + box[nx]))
            dist[nx] = (d + co, b + box[nx])
            
if dist[n][0] == 1e12:
    print("impossible")
else:
    print(*dist[n])

# 알고리즘 : 다익스트라
'''
풀이 : 최단 거리를 최우선으로 두되, 같은 거리일 경우에 박스 수의 차이도 고려한다.
전체적인 틀은 일반적인 다익스트라와 같지만, 거리가 같은 경우를 건너뛰지 않는다.
현재 거리(d)가 dist[now]에 저장된 거리보다 큰 경우만 continue로 건너뛴다.

현재 지역과 연결된 다른 지역에 대한 정보를 순서대로 탐색하되, 다음 두가지 경우를 모두 고려해 heap에 삽입한다.
1. 거리가 더 짧은 경우, 박스의 수에 관련없이 진행한다.
2. 거리가 같은 경우, 박수의 수가 더 많은 경우면 진행한다.
진행이 될때마다 dist[nx]를 갱신해준다.

heap에 더이상 새로운 경로가 입력되지 않아 완전히 빌 때까지 탐색한다.
dist[n][0]이 1e12라면, 1에서 n으로 갈 수 없다는 뜻이기 때문에 impossible을 출력한다. 그렇지 않다면 dist[n][1]을 출력한다.

'''
