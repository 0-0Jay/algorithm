# 프로그래머스 PCCP 기출문제 2번 : https://school.programmers.co.kr/learn/courses/19344/lessons/242259

from collections import deque

d = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def solution(land):
    r = len(land)
    c = len(land[0])
    amount = [0 for _ in range(c)]

    for i in range(r):
        for j in range(c):
            if land[i][j] == 1:
                tmp = {}
                cnt = 1
                que = deque()
                que.append([i, j])
                land[i][j] = 0
                while que:
                    now = que.popleft()
                    if now[1] not in tmp: tmp[now[1]] = 1
                    for t in range(4):
                        nx = now[0] + d[t][0]
                        ny = now[1] + d[t][1]
                        if 0 <= nx < r and 0 <= ny < c and land[nx][ny] == 1:
                            cnt += 1
                            land[nx][ny] = 0
                            que.append([nx, ny])
                for k in tmp:
                    amount[k] += cnt
                                 
    return max(amount)

# 알고리즘 : BFS
''' 풀이 : 각 열에서 뽑을 수 있는 석유 양을 저장할 배열 amount를 만들어서 그 최대값을 구한다.
전체 배열을 돌다가 석유를 발견하면 해당 석유 덩어리의 양을 BFS로 탐색한다.
탐색하면서 amount의 같은 인덱스에 석유 양을 누적시킨다.
'''
