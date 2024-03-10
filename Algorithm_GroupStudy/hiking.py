# 백준 1486번 등산 : https://www.acmicpc.net/problem/1486

from collections import defaultdict, deque
import math
import heapq as hq
import sys
input = sys.stdin.readline

n, m, t, d = map(int, input().split())
sz = n * m
INF = 1e9
mountain = []
for i in range(n):
    tmp = list(input().strip())
    for j in range(m):
        if 'A' <= tmp[j] <= 'Z': tmp[j] = ord(tmp[j]) - ord('A')
        else: tmp[j] = ord(tmp[j]) - ord('a') + 26
    mountain.append(tmp)
graph = [[INF] * (sz) for _ in range(sz)]   

que = deque()
que.append((0, 0, mountain[0][0]))
dt = [(1, 0), (0, 1), (-1, 0), (0, -1)]
chk = set()
while que:
    x, y, cost = que.popleft()
    
    if (x, y) in chk: continue
    chk.add((x, y))
    
    now = mountain[x][y]
    for i in range(4):
        nx = x + dt[i][0]
        ny = y + dt[i][1]
        if 0 <= nx < n and 0 <= ny < m and abs(now - mountain[nx][ny]) <= t:
            next = mountain[nx][ny]
            que.append((nx, ny, next))
            a = x * m + y
            b = nx * m + ny
            if next - now > 0:  # 다음이 더 높으면 
                graph[a][b] = (next - now) ** 2
            else:  # 낮거나 같으면
                graph[a][b] = 1

for k in range(sz):
    for i in range(sz):
        for j in range(sz):
            if i == j: 
                graph[i][j] = 0
                continue  #  <-- continue..
            graph[i][j] = min(graph[i][k] + graph[k][j], graph[i][j])

ans = 0
for i in range(sz):
    if graph[0][i] == INF or graph[i][0] == INF: continue
    if graph[0][i] + graph[i][0] <= d and mountain[i // m][i % m] > ans:
        ans = mountain[i // m][i % m]
        
print(ans)

# 알고리즘 : 플로이드-워셜
'''
풀이 : 인접한 좌표끼리 높이를 계산해 간선을 연결하여 모든 좌표를 graph화 하고, 플로이드 워셜을 수행한다.
인접한 칸으로만 이동할 수 있기 때문에 인접 칸들의 높이를 비교한다.
입력단계에서 높이 비교의 편의성을 위해 알파벳을 전부 숫자값으로 치환해서 저장한다.
인접한 칸의 높이차이가 주어진 조건 내라면 일단 간선을 연결하고, 이동 시간을 가중치로 저장한다.
모든 좌표에 대한 간선을 연결한 후, 플로이드-워셜을 수행하여 모든 좌표에 대한 최소 가중치를 기록한다.
이 후, 모든 좌표에 대해 (0,0) 좌표와의 왕복 가중치를 계산하여 시간 제한 내라면 ans와 최대값 비교한다.
'''
