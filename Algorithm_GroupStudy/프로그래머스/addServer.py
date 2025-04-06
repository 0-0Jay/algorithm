# 프로그래머스 2025 코드챌린지 2차 예선 - 서버 증설 횟수 : https://school.programmers.co.kr/learn/courses/30/lessons/389479

def solution(players, m, k):
    answer = 0
    server = [0] * (len(players) + 1)
    for i in range(len(players)):
        server[i] += server[i - 1]
        while players[i] >= (server[i] + 1) * m:
            server[i] += 1
            server[i + k if i + k < len(players) + 1 else len(players)] -= 1
            answer += 1
    return answer

# 알고리즘 : 스위핑
'''
풀이 : 시간의 이동에 따라 서버 증설을 체크할 배열을 활용해 스위핑한다.
우선 서버의 수를 체크할 배열(server)를 선언한다.
players를 왼쪽부터 1개씩 탐색한다.
일단 이전에 증설되어 있는 서버 정보를 가져오기 위해 server[i - 1]의 값을 server[i]에 더한다.
현재 증설된 서버가 players를 감당할 수 있을 때 까지 server[i]에 +1 한다.
이 때, 증설된 서버는 k시간 후에 반납하기때문에 같은 수만큼 server[i + k]에 -1 해준다.
서버가 증설된 수를 원하기 때문에 answer에도 +1한다.
이를 마지막 시간까지 반복하면 answer의 값이 곧 증설한 서버 수가된다.
'''
