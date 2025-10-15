# 백준 1938번 통나무 옮기기 : https://www.acmicpc.net/problem/1938

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
tree = [list(input().strip()) for _ in range(n)]
que = deque()
chk = set()
dx = [1, -1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, 1, -1, -1, 1, 1, -1]

def treeCheck(a, b): # 3x3 범위에 나무 있는지 체크
    for i in range(8):
        na = a + dx[i]
        nb = b + dy[i]
        if na < 0 or na >= n or nb < 0 or nb >= n or tree[na][nb] == "1": return False
    return True

fin = []
res = 0
for i in range(n):
    for j in range(n):
        if tree[i][j] == 'B':
            if not que and i + 1 < n and tree[i + 1][j] == 'B':  # 가운데 통나무만 생각
                chk.add((i + 1, j, 0))
                que.append((i + 1, j, 0, 0))  # 세로면 0, 가로면 1
                # [x, y, 수직/수평, 동작 횟수]
            elif not que and j + 1 < n and tree[i][j + 1] == 'B':
                chk.add((i, j + 1, 0))
                que.append((i, j + 1, 1, 0))
        elif tree[i][j] == 'E':
            if not fin and i + 1 < n and tree[i + 1][j] == 'E':
                fin = [i + 1, j, 0]
            elif not fin and j + 1 < n and tree[i][j + 1] == 'E':
                fin = [i, j + 1, 1]
           
while que:
    x, y, status, cnt = que.popleft()
    if x == fin[0] and y == fin[1] and status == fin[2]:
        res = cnt
        break

    if status == 0: # 만약 통나무가 세로방향이면
        for i in range(4): # 상하좌우 이동
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 < nx < n - 1 and 0 <= ny < n and (nx, ny, 0) not in chk:  # 세로 일때 가능한 범위 내이고
                if tree[nx][ny] != "1" and tree[nx + 1][ny] != '1' and tree[nx - 1][ny] != '1': # 다른 나무가 없을때 이동
                    chk.add((nx, ny, 0))
                    que.append((nx, ny, 0, cnt + 1))
        if treeCheck(x, y): # 주변에 나무 없으면 회전
            chk.add((x, y, 1))
            que.append((x, y, 1, cnt + 1))
                  
    else: # 만약 통나무가 가로방향이면
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 < ny < n - 1 and (nx, ny, 1) not in chk:  # 세로 일때 가능한 범위 내이고
                if tree[nx][ny] != "1" and tree[nx][ny - 1] != '1' and tree[nx][ny + 1] != '1': # 다른 나무가 없을때 이동
                    chk.add((nx, ny, 1))
                    que.append((nx, ny, 1, cnt + 1))
        if treeCheck(x, y): # 주변에 나무 없으면 회전
            chk.add((x, y, 0))
            que.append((x, y, 0, cnt + 1))
            
print(res)

# 알고리즘 : BFS
'''
풀이 : 통나무를 3개를 움직이지 않고 가로/세로 구분 값을 주어 5개의 동작을 BFS로 탐색한다.
chk는 set() 자료구조를 이용해 중복 방문 체크에 활용했다.
통나무가 가로방향일 경우와 세로방향일 경우 상하좌우 이동의 한계 범위가 달라지므로 두개를 구분해서 수행한다.
매 탐색마다 인접 8칸을 탐색하여 만약 1이 있으면 회전시키지 않는다.
'''
