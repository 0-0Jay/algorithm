# 프로그래머스 - 게임 맵 최단거리 : https://school.programmers.co.kr/learn/courses/30/lessons/1844

from collections import deque

def solution(maps):
    que = deque([(0, 0, 0)])
    chk = set()
    chk.add((0, 0))
    while que:
        x, y, cnt = que.popleft()
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and maps[nx][ny] == 1 and (nx, ny) not in chk:
                chk.add((nx, ny))
                que.append((nx, ny, cnt + 1))
                if nx == len(maps) - 1 and ny == len(maps[0]) - 1: return cnt + 2
    return -1

# 알고리즘 : BFS
'''
풀이 : BFS로 맵 전체를 탐색한다.
지나갈 수 있는 길이 1이므로 maps[nx][ny]가 1인 곳 중에서 예전에 방문하지 않았던 칸인 경우만 전진한다.
우측하단 끝칸에 도착했다면, 시작점을 포함한 이동한 칸 갯수를 반환한다.
만약 BFS 탐색이 끝났음에도 우측하단 끝칸에 도착하지 못했다면 -1을 반환한다.
'''
