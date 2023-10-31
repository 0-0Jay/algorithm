# 프로그래머스 - 이중우선순위큐 : https://school.programmers.co.kr/learn/courses/30/lessons/42628

import heapq as hq

def solution(operations):
    answer = []
    for com in operations:
        if com[0] == "I":
            hq.heappush(answer, int(com[2:]))
        elif com == 'D -1':
            if len(answer) > 0 : hq.heappop(answer)
        else:
            if len(answer) > 0 : del answer[answer.index(max(answer))]
    return [max(answer), min(answer)] if len(answer) > 0 else [0, 0]

# 알고리즘 : 힙
'''
풀이 : 최소값 제거는 heap 자료구조의 기능을, 최대값 제거는 list의 메소드를 활용하여 제거한다.
'''
