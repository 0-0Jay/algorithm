# 프로그래머스 2024 카카오 겨울 인턴쉽 - 주사위 고르기 : https://school.programmers.co.kr/learn/courses/30/lessons/258709#

from itertools import combinations
from collections import defaultdict

def solution(dice):
    answer = []
    comb = tuple(combinations(range(len(dice)), len(dice) // 2))
    combDict = {}
    for c in comb: combDict[c] = defaultdict(int)
    
    def select(c, n, sum):
        if n == len(c):
            combDict[c][sum] += 1
            return
        for i in range(6):
            select(c, n + 1, sum + dice[c[n]][i])
                
    for c in comb:
        select(c, 0, 0)
    win = defaultdict(int)
    for A in comb:
        if A in win: continue
        B = tuple(i for i in range(len(dice)) if i not in A)
        for ak, av in combDict[A].items():
            for bk, bv in combDict[B].items():
                point = av * bv
                if ak > bk: win[A] += point
                elif ak < bk: win[B] += point
                
    result = sorted(win.items(), key = lambda x : x[1])
    answer = []
    for i in result[-1][0]:
        answer.append(i + 1)
    
    return answer

# 알고리즘 : 해시 + 조합론 + 브루트 포스
'''
풀이 : 주사위의 절반을 선택해서 가능한 모든 합의 경우를 구한 후, 나머지 절반과 비교해서 승점을 계산한다.
먼저 고를 수 있는 주사위의 조합을 combinations 함수를 통해 구한다.
각 주사위 조합을 key로 두고, value로 주사위 조합에서 나올 수 있는 합과 그 합의 갯수를 저장한다.
이를 위해 중첩 딕셔너리를 활용해 기록한다.

만약 모든 합을 1차원 리스트로 두면, 주사위가 10개만 되어도 (6 ^ 252(10C5))개의 결과가 나오게 된다.
이 주사위 두 개의 승점 비교를 수행하게 되면 위 결과의 2배나 되는 탐색범위를 가지게 된다.
이를 방지하기 위해 중복되는 합은 하나의 key로 두고 컨트롤할 수 있는 딕셔너리를 사용한다.

모든 주사위 조합과 각 조합에 대한 합의 경우를 구했다면, 딕셔너리에서 주사위 조합 하나를 꺼낸다.
주사위는 반씩 나누기 때문에 한쪽 조합을 알면, 반대쪽 조합을 구할 수 있다.
이를 통해 두 주사위 조합의 승패를 비교해 이긴쪽에 포인트를 추가한다.
마지막으로 모든 조합중에 가장 포인트가 많은 주사위 조합을 반환한다.
'''
