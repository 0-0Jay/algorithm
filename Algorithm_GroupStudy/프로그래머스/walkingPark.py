# 프로그래머스 - 공원 산책 : https://school.programmers.co.kr/learn/courses/30/lessons/172928

def solution(park, routes):
    answer = []
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == 'S':
                answer = [i, j]
                break
        if answer : break
    dt = {'N' : (-1, 0), 'E' : (0, 1), 'W' : (0, -1), 'S' : (1, 0)}
  
    for i in range(len(routes)):
        d, a = routes[i][0], int(routes[i][2])
        nx, ny = answer
        chk = True
        for j in range(1, a + 1):
            nx_tmp = nx + dt[d][0] * j
            ny_tmp = ny + dt[d][1] * j
            if not(0 <= nx_tmp < len(park) and 0 <= ny_tmp < len(park[0])) or park[nx_tmp][ny_tmp] == 'X':
                chk = False
                break
        if chk: answer = [nx + dt[d][0] * a, ny + dt[d][1] * a]
         
    return answer

# 알고리즘 : 시뮬레이션
'''
풀이 : 문제에서 주어진 대로 시뮬레이션 한다.
일단 시작점 'S'의 좌표를 구해 answer에 저장한다.
그 후, 명령어의 NEWS에 맞는 좌표 이동값을 dt에 (x, y) 쌍으로 저장해놓은 딕셔너리를 하나 만들어 방향키로 사용한다.

위의 사전작업 후 routes에서 명령어를 하나씩 꺼낸다.
벽이나 장애물 여부를 판단하는데 사용할 플래그를 하나 만들어준다.(chk)
방향(d)과 거리(a)로 나누어, 현재위치에서 dt[d] 방향으로 a만큼 이동했을 때, 중간에 만나는 외곽 또는 'X'가 있는지 확인하고, 있으면 chk를 False로 바꾼다.
flag가 계속 True 상태면, 장애물 없이 쭉 직진이 가능하다는 의미이므로 answer의 위치를 갱신해준다.
이 과정을 routes의 모든 명령어에 대해 수행한 후 answer를 반환한다.
'''
