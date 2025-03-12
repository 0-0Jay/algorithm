# 프로그래머스 2018 카카오 블라인드 채용 - [1차] 프렌즈 4블록

def solution(m, n, board):
    board = [[j for j in i] for i in board]
    answer = 0
    while True:
        bomb = set()
        for i in range(m - 1):
            for j in range(n - 1):
                if board[i][j] != ' ' and board[i][j] == board[i + 1][j] == board[i][j + 1] == board[i + 1][j + 1]:
                    bomb.add((i, j))
                    bomb.add((i + 1, j))
                    bomb.add((i, j + 1))
                    bomb.add((i + 1, j + 1))
        if not bomb: break
        answer += len(bomb)
        for i, j in bomb:
            board[i][j] = ' '
        for i in range(n):
            tmp = []
            for j in range(m):
                if board[j][i] != ' ':
                    tmp.append(board[j][i])
            tmp = [' '] * (m - len(tmp)) + tmp
            for j in range(-1, -m - 1, -1):
                board[j][i] = tmp[j]
    return answer

# 알고리즘 : 구현(시뮬레이션)
'''
풀이 : 파괴되는 영역을 집합으로 저장해 중첩블록을 처리한다.
문제에서 지워지는 조건에 만족하는 2*2가 여러 개 있다면 한번에 지워진다는 조건이 있기 때문에, 배열을 전체적으로 탐색해 2*2를 모두 찾는다.
2*2 모양을 찾을 때 마다 집합(bomb)에 추가한다.
집합 자료형을 사용했기 때문에 겹치는 블록은 자연스럽게 중복처리되어 들어가지 않는다.
bomb에 하나라도 있다면, answer에 bomb의 길이를 추가하고, board에서 bomb에 저장된 좌표들의 값을 공백으로 갱신한다.

이 후, 2*2를 모두 지웠다면, 빈자리를 채워야한다.
위 풀이에서는 빈공간을 줄이기위해 임시로 배열(tmp)을 하나 선언하고, 공백이 아닐때마다 해당 블록을 tmp에 추가했다.
하나의 열을 모두 탐색했다면, tmp의 앞에 열 길이만큼 공백을 추가하고, board에 갈아끼워준다.
< 작동예시 >
ABCD           board[0:4][0] = [A, ' ', ' ', A]
    AB           tmp = [A, A]
    AB    ->    => tmp = [' ', ' ', A, A]
ABCD           board[0:4][0] = tmp

이 과정을 계속 반복하다 이번 탐색에서 bomb에 저장되는 좌표가 하나도 없을 경우 반복을 종료하고, answer를 반환한다.
'''
