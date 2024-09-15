# 프로그래머스 - 무인도 여행 : https://school.programmers.co.kr/learn/courses/30/lessons/154540

from collections import deque

def solution(maps):
    maps = [[j for j in i] for i in maps]
    dt = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    answer = []
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if maps[i][j] != "X":
                sum = int(maps[i][j])
                maps[i][j] = "X"
                que = deque([(i, j)])
                while que:
                    x, y = que.popleft()
                    for dx, dy in dt:
                        nx = x + dx
                        ny = y + dy
                        if 0 <= nx < len(maps) and 0 <= ny < len(maps[i]) and maps[nx][ny] != "X":
                            sum += int(maps[nx][ny])
                            maps[nx][ny] = "X"
                            que.append((nx, ny))
                answer.append(sum)
    if answer: answer.sort()
    else:  answer.append(-1)
    return answer

# 알고리즘 : BFS
'''
풀이 : 숫자 칸을 발견할 때마다 그 숫자칸이 포함된 영역의 합을 구하여 answer에 넣고 해당 구역을 "X"로 바꾼다.
먼저 입력된 maps를 BFS로 탐색하기 쉽게 2차원 배열의 형태로 가공한다.
2중 for문으로 maps의 (0, 0)부터 마지막 칸까지 완전탐색한다.
탐색 중 "X"가 아닌 칸이 나오면, 해당 칸을 시작점으로 하여 BFS를 수행한다.
BFS를 수행하면서 발견하는 모든 숫자는 sum에 누적시키면서 숫자를 "X"로 바꾸어 중복 탐색을 방지한다.
BFS 탐색이 끝나면 해당 숫자를 answer에 쌓는다.
maps의 마지막 칸까지 탐색이 끝난 후, answer에 값이 들어 있다면 answer를 오름차순 정렬하고, 아니라면 -1을 추가한다.
'''
