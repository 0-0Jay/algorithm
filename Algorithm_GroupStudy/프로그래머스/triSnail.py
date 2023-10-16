# 월간 코드 챌린지 시즌 1 - 삼각 달팽이 : https://school.programmers.co.kr/learn/courses/30/lessons/68645

def solution(n):
    answer = []
    arr = [[0 for _ in range(n)] for _ in range(n)]
    d = [[1, 0], [0, 1], [-1, -1]]
    x, y, idx = -1, 0, 0
    num = 1
    tmp = n
    while tmp > 0:
        for i in range(tmp):
            x += d[idx][0]
            y += d[idx][1]
            arr[x][y] = num
            num += 1
        tmp -= 1
        idx = (idx + 1) % 3

    for i in arr:
        for j in i:
            if j != 0: answer.append(j)
    return answer

# 알고리즘 : x
'''
풀이 : 세개의 변수 num(입력할 수), idx(이동방향 컨트롤), tmp(이동 횟수)를 컨트롤하여 배열을 채운다.
삼각 달팽이 특성상 갈수록 num은 증가하지만 방향을 전환하기까지 이동횟수는 줄어든다.
ex)
   | ↖   3
5  |    ＼
   V ----->
       4
'''
