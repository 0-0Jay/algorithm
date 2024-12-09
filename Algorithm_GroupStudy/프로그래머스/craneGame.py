# 프로그래머스 2019 카카오 개발자 겨울 인턴십 - 크레인 인형뽑기 게임 : https://school.programmers.co.kr/learn/courses/30/lessons/64061#

def solution(board, moves):
    bag = []
    answer = 0
    key = [-1] * len(board)
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] != 0 and key[j] == -1: key[j] = i

    for i in moves:
        if key[i - 1] == len(board): continue
        bag.append(board[key[i - 1]][i - 1])
        key[i - 1] += 1
        if len(bag) > 1:
            if bag[-1] == bag[-2]:
                answer += 2
                bag.pop()
                bag.pop()
            
    return answer

# 알고리즘 : 시뮬레이션 + 스택
'''
풀이 : 인형을 쌓을 스택을 하나 만들고, 인형뽑기를 하며 사라지는 인형의 수를 센다.
겹치는 인형이 생길때마다 인형 2개를 모두 지우고 answer에 2씩 누적하는 문제다.
처음 들어오는 board를 순회하며 key에 각 줄에서 가장 위에 있는 인형의 인덱스를 저장해둔다.
이 때, key의 초기값은 모두 -1로 두어 혹시나 해당 줄에 인형이 꽉차있을 경우 0번 인덱스로 저장될 수 있게 한다.

moves를 하나씩 탐색한다.
뽑은 줄에 인형이 더이상 남아있지 않으면 continue로 넘긴다.
인형이 있다면, bag에 key에 기록된 높이의 인형을 넣고, key에 저장된 높이를 1올려준다.
만약 가방에 인형이 2개이상 있다면, 마지막 두 개의 인형이 서로 같은지 확인한다.
이를 모든 moves를 순회하는 동안 반복한다.

사라진 인형의 개수를 묻는 문제이므로 인형이 사라질때마다 answer에 2를 더하고 마지막에 최종 answer를 반환한다.
'''
