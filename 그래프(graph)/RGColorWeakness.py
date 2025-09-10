# 백준 10026번 - 적록색약 : https://www.acmicpc.net/problem/10026

import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
field = [list(input().strip()) for _ in range(n)]
dt = [(1, 0), (0, 1), (-1, 0), (0, -1)]
RGB = {'R' : 0, 'G' : 0, 'B' : 0}
RG = 0
chk = set()
RGchk = set()

def RGB_BFS(i, j, now):
    que = deque([(i, j)])
    chk.add((i, j))
    while que:
        x, y = que.popleft()
        for dx, dy in dt:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in chk and field[nx][ny] == now:
                que.append((nx, ny))
                chk.add((nx, ny))
    RGB[now] += 1

def RG_BFS(i, j):
    global RG
    que = deque([(i, j)])
    RGchk.add((i, j))
    while que:
        x, y = que.popleft()
        for dx, dy in dt:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in RGchk and field[nx][ny] != 'B':
                que.append((nx, ny))
                RGchk.add((nx, ny))
    RG += 1

for i in range(n):
    for j in range(n):
        if (i, j) not in chk:
            RGB_BFS(i, j, field[i][j])
        if (i, j) not in RGchk and (field[i][j] == 'R' or field[i][j] == 'G'):
            RG_BFS(i, j)

print(sum(RGB.values()), RG + RGB['B'])

# 알고리즘 : BFS
'''
풀이 : 적록색약의 경우와 정상인 경우를 각각 BFS 탐색한다.
정상인 경우는 각 색 영역을 BFS 탐색한 후, 중복 체크(chk)하여 다른 색 영역에 포함되지 않도록 한다.
적록색약의 경우는 색 영역이 B가 아닌 경우와 B인 경우 두가지로 나누어 BFS 탐색한다.
이 때도 마찬가지로 중복체크하여 다른 영역에 포함되지 않도록 한다.
'''
