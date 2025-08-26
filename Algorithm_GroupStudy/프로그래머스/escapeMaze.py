# 프로그래머스 - 미로 탈출 : https://school.programmers.co.kr/learn/courses/30/lessons/159993

from collections import deque

def solution(maps):
    start = []
    end = []
    lever = []
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == "S":
                start = [i, j]
            elif maps[i][j] == "L":
                lever = [i, j]
            elif maps[i][j] == "E":
                end = [i, j]
                
    def BFS(x, y, ex, ey) : 
        chk = set()       
        que = deque([(x, y, 0)])
        chk.add((x, y))
        dt = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        while que:
            x, y, t = que.popleft()
            if x == ex and y == ey:
                return t
            for dx, dy in dt:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and (nx, ny) not in chk and maps[nx][ny] != "X":
                    chk.add((nx, ny))
                    que.append((nx, ny, t + 1))
        return -1
    
    a = BFS(start[0], start[1], lever[0], lever[1])
    b = BFS(lever[0], lever[1], end[0], end[1])    
    return a + b if a != -1 and b != -1 else -1

# 알고리즘 : BFS
'''
풀이 : 시작점 -> 레버의 최단 시간과 레버 -> 출구의 최단 시간을 각각 구해 더한다.
시작에서 레버까지의 최단 시간을 구해 a에 저장한다.
레버에서 출구까지의 최단 시간을 구해 b에 저장한다.
이 때, a나 b중 하나라도 -1이라면, BFS를 모든 구역에 수행했음에도 도착하지 못했다는 뜻이기 때문에 -1을 반환한다.
그렇지 않다면 a와 b의 합을 반환한다.
'''
