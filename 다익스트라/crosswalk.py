# 백준 24042번 횡단보도 : https://www.acmicpc.net/problem/24042

import heapq as hq
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for i in range(1, m + 1):
    a, b = map(int, input().split())
    graph[a].append((b, i))
    graph[b].append((a, i))

que = [(0, 1, 0)] # 시간, 정점, 주기에서의 위치
time = [1e12] * (n + 1)
time[1] = 0
while que:
    cost, now, num = hq.heappop(que)
    if now == n:
        print(time[n])
        break
    if time[now] < cost: continue
    for nx, id in graph[now]:
        tmp = id - num
        if tmp <= 0: tmp += m
        if time[nx] > cost + tmp:
            time[nx] = cost + tmp
            hq.heappush(que, (time[nx], nx, id))

# 알고리즘 : 다익스트라
'''
풀이 : 대기시간 + 건너는 시간을 두 지역을 잇는 간선의 가중치로 두고 다익스트라로 최단거리를 탐색한다.
입력단계에서 횡단보도 신호의 순서를 인덱스로 두고 인접리스트에 (연결된 노드, i번째 신호)의 쌍으로 저장한다.
이 다음, 우선순위 큐를 이용해 가장 짧은 (대기시간 + 건너는 시간)을 가지는 간선부터 뽑아 탐색한다.

이동하는데 걸리는 시간은 우선 (신호의 인덱스 - 방금 내가 건넜던 신호의 인덱스)(tmp)의 값이다.
그러나, 현재 주기에서 방금 내가 건넜던 신호의 인덱스 이후에 내가 건널 지역과 연결된 횡단보도의 신호가 없을 수 있다.
이 경우 다음 주기의 신호가 돌아올 때까지 대기해야하기 때문에 만약 tmp가 0이하라면, 주기의 길이(m)를 더해준다.
이 과정이 끝났을 때의 tmp가 각 다음 지역으로 이동하는데 소요되는 시간 가중치가 된다.

다른 과정은 일반적인 다익스트라와 같다.
우선순위 큐에 의해 만약 now가 n이라면, 그 경로가 가장 짧은 시간을 가진 경로이므로 time[n]을 출력하고 break로 종료한다.
'''
