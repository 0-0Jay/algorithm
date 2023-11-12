# 백준 1938번 통나무 옮기기 : https://www.acmicpc.net/problem/1938
# 실패 이유 : TLE - 60%

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
풀이 : 통나무를 3개를 움직이지 않고 가로/세로 구분 값을 주어 BFS를 탐색하는 코드다.
que에는 (x, y, 가로/세로, 동작 횟수)를 사용했다.
chk는 set() 자료구조를 이용해 중복 방문 체크에 활용했다.

구글링을 통해 발견한 반례들이 내 환경에서는 문제없이 통과하기 때문에 로직, 코드상의 문제는 없으나 효율성 테스트용 케이스에서 시간초과가 발생하는 것 같다.
시간초과를 해결하기 위해 사용한 방법은 다음과 같다.
1. 3차원배열로 체크하던 중복 방문 체크를 set() 자료구조와 튜플로 전환
2. que에 리스트형태로 삽입하던 것을 튜플로 전환
3. 처음 B와 E의 위치를 초기값과 목적값으로 정하는 과정에서 len(que) == 0 대신 not que로 전환
4. dt를 2차원 배열로 만들어 각인덱스에 0번은 x, 1번은 y 좌표의 이동값을 주는 대신 dx와 dy로 각각의 일차원 배열로 전환
5. 나무 회전을 위한 인접 8칸 탐색 부분을 2중 for문을 통한 탐색에서 dt에 미리 구해둔 8좌표로 탐색하는 것으로 전환

그러나 근본적인 BFS 탐색 부분에서 문제가 있는 것인지 시간초과를 해결하지는 못했다.
