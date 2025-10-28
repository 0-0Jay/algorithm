# 백준 1238번 파티 : https://www.acmicpc.net/problem/1238

import sys
from collections import deque
import heapq as hq

n, m, x = map(int, input().split())
go_route = [[] for _ in range(n + 1)]
back_route = [[] for _ in range(n + 1)]
go_cost = [[1e12 for _ in range(n + 1)] for _ in range(n + 1)]
back_cost = [[1e12 for _ in range(n + 1)] for _ in range(n + 1)]
res = 0

for i in range(m):
    a, b, c = map(int, input().split())
    go_route[a].append(b)
    back_route[b].append(a)
    go_cost[a][b], back_cost[b][a] = c, c
    
# 출발지에서 X로
que = deque()
que.append([x, 0])
while que:
    now, cost = que.popleft()
    for nx in go_route[now]:
        if cost + go_cost[now][nx] <= go_cost[x][nx]:
            go_cost[x][nx] = cost + go_cost[now][nx]
            que.append([nx, go_cost[x][nx]])
            
# X에서 출발지로
que = deque()
que.append([x, 0])
while que:
    now, cost = que.popleft()
    for nx in back_route[now]:
        if cost + back_cost[now][nx] <= back_cost[x][nx]:
            back_cost[x][nx] = cost + back_cost[now][nx]
            que.append([nx, back_cost[x][nx]])

go_cost[x][x] = back_cost[x][x] = 0  # 자기 마을이 파티를 여는 경우 움직일 필요 없다.

for i in range(1, n + 1):
    res = max(res, go_cost[x][i] + back_cost[x][i])

print(res)

# 알고리즘 : 다익스트라
'''
풀이 : 출발지에서 x로 가는 경우와 x에서 출발지로 가는 경우를 다익스트라로 최소값을 계산하여 두 비용을 합한다.

출발지->X를 체크할 배열과 X->출발지를 체크할 배열을 따로 선언해서 사용한다.
입력되는 부분은 출발지->X배열에 넣고, 방향을 바꿔서 X->출발지 배열에 저장한다.
ex) 1 -> 2에 비용 : 3을 출발지->X에 넣고, 2 -> 1에 비용 : 3으로 X->출발지에 넣는다.
이렇게 하면 플로이드-워셜로 모든 출발지에서 출발해 X로 가는 최단거리를 구하지 않아도 된다.
단순 배열 뒤집기로 다익스트라 1회에 위 결과를 얻을 수 있다.

두번의 다익스트라가 끝나면 출발지->X 배열에서의 cost와 X->출발지 배열에서의 cost를 합하는 것으로 왕복 최소 비용을 구할 수 있다.
'''
