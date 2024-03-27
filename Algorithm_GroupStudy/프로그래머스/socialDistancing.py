# 프로그래머스 2021 카카오 채용연계형 인턴십 - 거리두기 확인하기 : https://school.programmers.co.kr/learn/courses/30/lessons/81302

from collections import deque

def BFS(x, y, room):
    dt = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    que = deque()
    que.append((x, y, 0))
    chk = set({(x, y)})
    while que:
        x, y, cnt = que.popleft();
        if cnt == 2: continue
        for i in range(4):
            nx = x + dt[i][0]
            ny = y + dt[i][1]
            if 0 <= nx < 5 and 0 <= ny < 5 and room[nx][ny] != 'X' and (nx, ny) not in chk:
                if room[nx][ny] == 'P': return 0
                que.append((nx, ny, cnt + 1))
                chk.add((nx, ny))
    return 1

def solution(places):
    answer = [1, 1, 1, 1, 1]
    for k in range(5):
        room, flag = places[k], 0
        for i in range(5):
            for j in range(5):
                if room[i][j] == 'P' and BFS(i, j, room) == 0:
                    answer[k], flag = 0, 1
                    break
            if flag == 1: break
        if flag == 1: continue
        
    return answer

# 알고리즘 : BFS
'''
풀이 : 응시자가 존재하는 자리에서 BFS를 돌려 2회 이내로 다른 응시자를 만나면 0으로 바꿔준다.
다른 응시자가 만약 2칸 범위 내에 존재하지만, 파티션이 존재한다면 무관하기 때문에 파티션이면 추가 탐색하지 않는다.
한번이라도 BFS에서 0이 반환된다면, 불가능한 경우기 때문에 flag를 사용하여 모든 반복문에서 탈출시켜 불필요한 탐색을 막는다.
'''
