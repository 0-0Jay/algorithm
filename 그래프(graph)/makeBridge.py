# 백준 2146번 다리 만들기 : https://www.acmicpc.net/problem/2146

from collections import defaultdict, deque
from functools import cmp_to_key
import heapq as hq
import math
import sys
input = sys.stdin.readline

n = int(input())
land = [list(map(int, input().split())) for _ in range(n)]
dt = [[1, 0], [0, 1], [-1, 0], [0, -1]]
min_length = 2 * n
land_num = 1
for i in range(n):
    for j in range(n):
        if land[i][j] == 1:
            land_num += 1
            que = deque()
            que.append((i, j))
            land[i][j] = land_num
            
            while que:
                nowx, nowy = que.popleft()
                for k in range(4):
                    nx = nowx + dt[k][0]
                    ny = nowy + dt[k][1]
                    if 0 <= nx < n and 0 <= ny < n and land[nx][ny] == 1:
                        land[nx][ny] = land_num
                        que.append((nx, ny))

for i in range(n):
    for j in range(n):
        if land[i][j] != 0:
            que = deque()
            que.append((i, j, 0))
            target = land[i][j]
            chk = set()
            chk.add((i, j))
            while que:
                nowx, nowy, cost = que.popleft()
                if cost > min_length: continue
                for k in range(4):
                    nx = nowx + dt[k][0]
                    ny = nowy + dt[k][1]
                    if 0 <= nx < n and 0 <= ny < n and land[nx][ny] != target and (nx, ny) not in chk:
                        if land[nx][ny] != 0:
                            min_length = min(min_length, cost)
                        chk.add((nx, ny))
                        que.append((nx, ny, cost + 1))
                        
print(min_length)

# 알고리즘 : BFS
'''
풀이 : 각 섬마다 고유 번호를 부여하고 모든 땅에서 BFS를 돈다. 다른 섬을 만나면 거리를 최소값 비교 한다.
처음 전체 지도에 BFS를 탐색하여 섬마다 고유 번호를 설정한다.
다음으로 BFS를 돌때는 해당 지역에서 다음 칸이 0일 경우에만 루트를 늘려가며 다른 섬을 찾는다.
다른 섬에 도착하면 바로 해당 거리(cost)를 min_length와 비교해 더작은 값으로 교체한다.
만약 현재 설정된 min_length보다 cost가 커지면 더 이상 탐색해도 의미 없으므로 continue로 처리한다.
'''
