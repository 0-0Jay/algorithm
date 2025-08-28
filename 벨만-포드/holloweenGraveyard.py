# 백준 3860번 할로윈 묘지 : https://www.acmicpc.net/problem/3860

from collections import defaultdict, deque
import math
import heapq as hq
import sys
input = sys.stdin.readline

INF = 1e9
dt = [(0, 1), (0, -1), (-1, 0), (1, 0)]
while True:
    cycle = False
    w, h = map(int, input().split())
    if w == 0 and h == 0: break
    route = []
    hole = [[i * h + j for j in range(1, h + 1)] for i in range(w)]
    chk = set()

    g = int(input())  # 묘비 예외처리
    for _ in range(g):
        x, y = map(int, input().split())
        hole[x][y] = "X"

    e = int(input())  # 구멍 예외처리
    for _ in range(e):
        x1, y1, x2, y2, t = map(int, input().split())
        route.append((hole[x1][y1], hole[x2][y2], t))
        chk.add(hole[x1][y1])  # 체크에 구멍을 저장하여 후에 탐색하지 않도록 설정

    for x in range(w):
        for y in range(h):
            if hole[x][y] in chk: continue  # 묘비거나 구멍이거나 출구면 다음 간선을 계산하지 않음
            if hole[x][y] == "X" or (x == w - 1 and y == h - 1): continue
            for i in range(4):
                nx = x + dt[i][0]
                ny = y + dt[i][1]
                if 0 <= nx < w and 0 <= ny < h and hole[nx][ny] != "X":
                    route.append((hole[x][y], hole[nx][ny], 1))
            
    dist = [INF] * (w * h + 1)
    dist[1] = 0
    for i in range(1, w * h + 1):
        for a, b, cost in route:
            if dist[a] != INF and dist[b] > dist[a] + cost:
                dist[b] = dist[a] + cost
                if i == w * h:
                    cycle = True
                    break
    
    if cycle: print("Never")
    elif dist[-1] == INF: print("Impossible")
    else: print(dist[-1])   
        
# 알고리즘 : 벨만-포드
'''
풀이 : 구멍, 묘비, 출구를 예외처리 해주며 모든 정점을 간선연결 한 후, 벨만 포드를 수행한다.
간선 정보가 따로 주어지지 않고, 상하좌우로 움직일 수 있기 때문에 인접칸은 모두 간선이 연결되어 있다고 봐야한다.
단, 입력단계에서 묘비가 주어지면 해당 좌표는 "X"로 치환하여 예외처리 해준다.
구멍이 주어지면 해당 좌표는 인접칸으로가 아닌 구멍이 연결된 반대쪽 좌표로만 이동하기 때문에 이 또한 예외처리한다.
그 외의 모든 칸은 인접칸에 대한 간선을 route에 저장한다.
route에 저장된 간선정보로 벨만-포드를 수행하면 된다.
'''
