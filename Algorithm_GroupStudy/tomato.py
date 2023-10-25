# 백준 7569번 토마토 : https://www.acmicpc.net/problem/7569

import sys
import math
import heapq as hq
from collections import deque

m, n, h = map(int, input().split())
box = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(h)]
que = deque()
date = 0
cnt = 0
d = [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]]

for k in range(h):
    for i in range(n):
        box[k][i] = list(map(int, input().split()))
        for j in range(m):
            if box[k][i][j] == 1:
                que.append([k, i, j, 0])
            elif (box[k][i][j] == 0): cnt += 1
        
while que:
    now = que.popleft()
    date = now[3]

    for lst in d:
        nh = now[0] + lst[0]
        nx = now[1] + lst[1]
        ny = now[2] + lst[2]
        if 0 <= nx < n and 0 <= ny < m and 0 <= nh < h and box[nh][nx][ny] == 0:
            cnt -= 1
            box[nh][nx][ny] = 1
            que.append([nh, nx, ny, now[3] + 1])
    
print(-1 if cnt > 0 else date)

# 알고리즘 : BFS
'''
풀이 : 단순히 2차원에서 수행하던 BFS를 3차원으로 확장시켜서 수행한다.
방향을 전, 후, 좌, 우, 상, 하로 6개 방향으로 두고 반복문을 돈다.
해당 방향의 칸이 범위 내고, 토마토가 있으며, 아직 익지 않았다면 큐에 삽입한다.
'''
