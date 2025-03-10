# 프로그래머스 - 인접한 칸 : https://school.programmers.co.kr/learn/courses/30/lessons/250125

def solution(board, h, w):
    d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    answer = 0
    for dx, dy in d:
        nx = h + dx
        ny = w + dy
        if 0 <= nx < len(board) and 0 <= ny < len(board[0]) and board[h][w] == board[nx][ny]: answer += 1
    return answer

# 알고리즘 : 구현
'''
풀이 : h, w 상하좌우의 칸만 확인한다.
먼저 가로세로로 1씩 인접한 칸들을 보기위한 좌표를 d에 미리 저장해둔다.
반복문을 통해 d에 저장된 좌표를 하나씩꺼내 h, w에 더하기만해도 인접한 칸을 확인 할 수 있다.
이 때, 확인할 인덱스가 board의 범위 안에 포함되어 있는지를 반드시 확인한다.
'''
