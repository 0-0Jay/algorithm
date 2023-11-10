# 프로그래머스 PCCP 기출문제 4번 : https://school.programmers.co.kr/learn/courses/19344/lessons/242261

from collections import deque

answer = 20

def solution(maze):
    r = len(maze)
    c = len(maze[0])
    end = [0, 0, 0, 0]
    start = [0, 0, 0, 0, 0]
    for i in range(r):
        for j in range(c):
            if maze[i][j] == 1: start[0], start[1] = i, j
            elif maze[i][j] == 2: start[2], start[3] = i, j
            elif maze[i][j] == 3: end[0], end[1] = i, j
            elif maze[i][j] == 4: end[2], end[3] = i, j
    
    d = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    rchk = [[0 for _ in range(c)] for _ in range(r)]
    bchk = [[0 for _ in range(c)] for _ in range(r)]
    rchk[start[0]][start[1]] = 1
    bchk[start[2]][start[3]] = 1
    
    def DFS(rx, ry, bx, by, cnt):
        global answer
        if cnt > answer : return
        if rx == end[0] and ry == end[1] and bx == end[2] and by == end[3]:
            if cnt < answer: answer = cnt
            return
        
        for i in range(4):
            for j in range(4):
                nrx = rx + d[i][0]
                nry = ry + d[i][1]
                nbx = bx + d[j][0]
                nby = by + d[j][1]
                if rx == end[0] and ry == end[1]:  # 빨간 공이 도착한 경우
                    if 0 <= nbx < r and 0 <= nby < c and bchk[nbx][nby] == 0 and maze[nbx][nby] != 5:
                        if nbx == rx and nby == ry: continue  # 겹치는 경우 제외
                        bchk[nbx][nby] = 1
                        DFS(rx, ry, nbx, nby, cnt + 1)
                        bchk[nbx][nby] = 0
                elif bx == end[2] and by == end[3]:  # 파란 공이 도착한 경우
                    if 0 <= nrx < r and 0 <= nry < c and rchk[nrx][nry] == 0 and maze[nrx][nry] != 5:
                        if nrx == bx and nry == by: continue  # 겹치는 경우 제외
                        rchk[nrx][nry] = 1
                        DFS(nrx, nry, bx, by, cnt + 1)
                        rchk[nrx][nry] = 0
                else:  # 둘다 도착하지 않은 경우
                    if 0 <= nrx < r and 0 <= nry < c and 0 <= nbx < r and 0 <= nby < c and rchk[nrx][nry] == 0 and bchk[nbx][nby] == 0 and (nrx != nbx or nry != nby) and maze[nrx][nry] != 5 and maze[nbx][nby] != 5:
                        if nrx == bx and nry == by and nbx == rx and nby == ry: continue  # 서로 교차하는 경우 제외
                        rchk[nrx][nry] = 1
                        bchk[nbx][nby] = 1
                        DFS(nrx, nry, nbx, nby, cnt + 1)
                        rchk[nrx][nry] = 0
                        bchk[nbx][nby] = 0
        
    DFS(start[0], start[1], start[2], start[3], 0)

    return 0 if answer == 20 else answer

# 알고리즘 : DFS + 구현
'''
풀이 : DFS로 빨간 수레와 파란 수레를 동시에 움직이는 모든 경우의 수를 탐색한다.
만약 한번이라도 빨간 수레와 파란 수레 모두 도착지점에 도착했다면, 이동횟수를 answer에 저장한다.
불필요한 탐색을 줄이기 위해 탐색깊이가 answer보다 길어지면 return한다.
빨간 수레와 파란 수래 모두 한번 있었던 칸은 다시 갈 수 없지만 서로가 갔던 칸은 가도 상관없으므로
각각 따로 중복 방문 체크를 수행한다.
'''
