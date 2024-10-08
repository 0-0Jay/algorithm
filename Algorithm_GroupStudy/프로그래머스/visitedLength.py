# 프로그래머스 Summer/Winter Coding(~2018) - 방문 길이 : https://school.programmers.co.kr/learn/courses/30/lessons/49994

def solution(dirs):
    answer = 0
    loc = [0, 0]
    chk = set()
    for d in dirs:
        nx = [loc[0], loc[1]]
        if d == 'U' and loc[1] < 5:
            nx[1] += 1
        elif d == 'L' and loc[0] > -5:
            nx[0] -= 1
        elif d == 'D' and loc[1] > -5:
            nx[1] -= 1
        elif d == 'R' and loc[0] < 5:
            nx[0] += 1
        fr = str(loc[0]) + str(loc[1])
        to = str(nx[0]) + str(nx[1])
        print(fr, to)
        if (fr, to) not in chk and fr != to:
            chk.add((fr, to))
            chk.add((to, fr))
            answer += 1
        loc = [nx[0], nx[1]]
    return answer

# 알고리즘 : 브루트포스
'''
풀이 : 단순히 명령대로 좌표를 이동하고, 사용한 길에 대한 중복체크를 수행한다.
좌표 이동은 U, L, D, R에 따라 좌표값에 +1 또는 -1 해준다.
이 때, 좌표를 바로 이동시키면 안되고, 현재좌표(loc)와 이동했을 때의 좌표(nx)를 따로두고 그 간선을 활용해야한다.
loc과 nx를 문자열로 치환하여 하나의 튜플로 만들어 간선에 대한 정보를 저장한다.
단, 문제에서 처음 걸어본 길의 길이를 요구하기 때문에 정방향으로 걷던 역방향으로 걷던 1회만 카운팅해야 한다.
따라서 (loc, nx)를 저장하고, (nx, loc)도 함께 chk에 저장해준다.
만약 chk에 저장되어있지 않은 길이라면, 처음 걷는 길이므로 answer에 1씩 카운팅해주고, 그렇지 않다면 좌표만 이동시킨다.
모든 이동이 끝났다면, answer를 반환한다.
'''
