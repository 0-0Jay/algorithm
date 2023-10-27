# 백준 16118번 : https://www.acmicpc.net/problem/16118

import sys
import heapq as hq

n, m = map(int,input().split())
route = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int,input().split())
    route[a].append((b, c*2))
    route[b].append((a, c*2))

f_cost = [1e12 for _ in range(n + 1)]
w_cost = [[1e12, 1e12] for _ in range(n + 1)]
fox = [(0, 1)]
wolf = [(0, 1, 0)]

while fox:
    cost, now = hq.heappop(fox)
    if f_cost[now] < cost: continue
    for nx, nc in route[now]:
        if f_cost[nx] > cost + nc:
            f_cost[nx] = cost + nc
            hq.heappush(fox, (f_cost[nx], nx))

while wolf:
    cost, now, st = hq.heappop(wolf)
    if w_cost[now][st] < cost: continue
    for nx, nc in route[now]:
        if st == 1: nc *= 2
        else: nc /= 2
        if w_cost[nx][st^1] > cost + nc:
            w_cost[nx][st^1] = cost + nc
            hq.heappush(wolf, (w_cost[nx][st^1], nx, st^1))

cnt = 0
for i in range(2, n + 1):
    if f_cost[i] < min(w_cost[i][0], w_cost[i][1]): cnt += 1
print(cnt)

# 알고리즘 : 다익스트라(Dijkstra)
'''
풀이 : 다익스트라를 이용해 1번 그루터기에서 출발하여 양과 늑대의 최소 cost를 기록한다.
배열에 값을 넣을 때, 오솔길을 x2해서 넣는다.
-> 늑대의 경우 2배의 속도로 이동하는 경우가 있는데, 이때, x2를 해두면 소숫점 계산이 발생하지 않는다.

여우는 단순히 다익스트라로 채우고, 늑대는 달렸다 걸었다 하기 때문에 각 그루터기에 걸으면서 도착했을 경우와 뛰면서 도착했을 경우의 최소 비용을 기록해야 한다.
예를 들어, 10000의 거리를 가진 오솔길이 주어지면, 해당 오솔길을 걸었을 때와 뛰었을 때의 시간차이가 15000이나 발생한다.
이와 같은 케이스의 경우, 나머지 오솔길에서의 달림/걸음의 수치를 무시할 정도로 클 수 있다.

계산이 끝나면, 1번 그루터기를 제외한 나머지 그루터기에서 여우의 비용이 늑대의 최소비용(걸어서 들어온 경우와 뛰면서 들어온 경우 중 작은 값)의 보다 작으면 카운팅한다.
'''
