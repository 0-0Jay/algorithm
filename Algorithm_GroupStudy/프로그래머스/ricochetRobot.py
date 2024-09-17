# 프로그래머스 - 리코쳇 로봇 : https://school.programmers.co.kr/learn/courses/30/lessons/169199

from collections import deque

def solution(board):
    field = []
    end = []
    dt = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    que = deque()
    chk = set()
    for i in range(len(board)):
        tmp = []
        for j in range(len(board[0])):
            tmp.append(board[i][j])
            if board[i][j] == 'R': 
                que.append((i, j, 0))
                chk.add((i, j))
            if board[i][j] == 'G': end = [i, j]
        field.append(tmp)

    while que:
        x, y, cnt = que.popleft()
        if x == end[0] and y == end[1]:
            return cnt
        
        for dx, dy in dt:
            nx, ny = x, y
            while True:
                nx, ny = nx + dx, ny + dy
                if not (0 <= nx < len(field)) or not (0 <= ny < len(field[0])):
                    if (nx - dx, ny - dy) not in chk:
                        chk.add((nx - dx, ny - dy))
                        que.append((nx - dx, ny - dy, cnt + 1))
                    break
                if field[nx][ny] == 'D':
                    if (nx - dx, ny - dy) not in chk:
                        chk.add((nx - dx, ny - dy))
                        que.append((nx - dx, ny - dy, cnt + 1))
                    break
                                        
    return -1

# 알고리즘 : BFS
'''
풀이 : 장애물이나 벽에 붙은 경우만 큐에 넣어 BFS를 수행한다.
입력에서 주어진 R과 G의 좌표를 따로 저장해주고, 문자열 배열을 2차원 배열로 가공해준다.
매 좌표마다 4방향으로 끝까지 이동시키다가 'D'를 만나거나 끝을 만나면 해당 좌표에 방문체크를 해주고 que에 넣는다.
위 방식으로 R부터 출발하여 G에 도착하기 까지 BFS를 수행한다.
BFS 방식이기때문에 좌표가 end에 저장된 좌표와 같다면 반드시 해당 탐색의 cnt가 최소 이동 수가 된다.
만약 que가 모두 비었음에도 G에 도달하지 못했다면 -1을 리턴한다.
'''
