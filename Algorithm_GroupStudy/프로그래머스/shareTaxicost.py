# 2021 KAKAO BLIND RECRUITMENT - 합승 택시 요금 : https://school.programmers.co.kr/learn/courses/30/lessons/72413

import sys
import math
from collections import deque

def solution(n, s, a, b, fares):
    cost = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    route =  [[] for _ in range(n + 1)]

    for i in fares:
        route[i[0]].append(i[1])
        route[i[1]].append(i[0])
        cost[i[0]][i[1]], cost[i[1]][i[0]] = i[2], i[2]

    for x in [s, a, b]: # s, a, b에서의 최소 비용 루트 계산
        que = deque()
        que.append([x, 0])
        while que:
            now = que.popleft()
            for i in route[now[0]]: # now와 연결된 모든 루트 i
                # 현재 노드까지의 금액 + 다음노드의 금액이 다음 노드에 있는 값보다 작을때 or 다음 노드에 금액이 0일때만 전진
                if i != x and (now[1] + cost[now[0]][i] <= cost[x][i] or cost[x][i] == 0):
                    cost[x][i] = now[1] + cost[now[0]][i]
                    cost[i][x] = cost[x][i]
                    que.append([i, cost[x][i]])
                    
    answer = cost[s][a] + cost[s][b]              
    for i in range(1, n + 1):
        if cost[s][i] == 0 and s != i: continue
        if i != a and cost[i][a] == 0: continue
        if i != b and cost[i][b] == 0: continue
        sum_cost = cost[s][i] + cost[i][a] + cost[i][b]
        if answer > sum_cost:
            answer = sum_cost

    return answer

# 알고리즘 : 다익스트라 (Dijkstra)
'''
풀이 : s, a, b지점에서 다른 모든 지점까지의 최소 비용을 구하고, 세 지점까지의 비용의 합이 최소인 지점을 구한다.
s에서 출발해서 a와 b로 이동하는 경로만 있으면 되기 때문에 불필요한 노드에서의 탐색은 수행하지 않고 s, a, b에서 탐색한다.
-> s, a, b와 연결되어 있지 않은 노드가 있을 수 있기 때문에 단순히 모든 노드를 탐색하는 것과 시간차이가 상당히 많이 난다.

탐색은 다음과 같이 진행했다.
1. s, a, b중 한 지점을 선택한다.
2. 1에서 선택한 지점에서 나머지 모든 지점까지의 총 비용의 최소값을 구한다.
  ex)  1 -> 2 : 41원  /  1 -> 3 : (1 -> 2 -> 3) 63
  2-1. 만약 어떤 지점까지 갈 수 있는 루트가 다양하게 존재할 때, 계속 탐색하는 조건은 다음 중 하나다.
     1) 현재 탐색 중인 루트가 이전에 탐색했던 루트보다 비용이 적다.
     2) 현재 탐색 중인 루트는 최초로 발견된 루트다.
3. 세 지점에서의 탐색이 종료되면, 비용합이 최소가 되는 지점을 구한다.
  3-1. 초기값은 처음부터 갈라져서 이동했을 때의 비용으로 설정했다.
  -> 합승할 것이라면 처음부터 갈라지는 것보다 반드시 비용이 적을 것이다.
  -> 합승하는게 손해라면 합승할 이유가 없다.
'''
