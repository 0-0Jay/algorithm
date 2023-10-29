# 프로그래머스 2020 카카오 인턴십 - 수식 최대화 : https://school.programmers.co.kr/learn/courses/30/lessons/67257

import re
from itertools import combinations, permutations

def solution(expression):
    answer = 0
    oper = re.findall('[-*+]', expression)
    s = list(set(oper))
    res = re.findall(r'\d+|\D', expression)
    perm = list(permutations(s, len(s)))
    
    for op in perm:
        tmp = res.copy()
        for i in op:
            while i in tmp:
                id = tmp.index(i);    
                tmp[id - 1] = str(eval(tmp[id - 1] + tmp[id] + tmp[id + 1]))
                del tmp[id]
                del tmp[id]
        if abs(int(tmp[0])) > answer: answer = abs(int(tmp[0]))        
    
    return answer

# 알고리즘 : 순열, 브루트 포스
'''
풀이 : 순열을 이용해 *, -, +의 모든 순열을 구해 연산자 우선순위를 정하고, 수식을 배열화하여 인덱스를 활용해 계산한다.

1. 수식(expression)을 정규표현식을 활용해서 배열화 하고, 사용된 연산자도 oper 배열로 따로 뺀다.
2. oper를 한번 set화 했다가 다시 리스트로 바꾸어 중복 연산자를 제거한다.
3. 중복이 제거된 연산자들로 순열을 만든다.
4. 만들어진 순열에서 하나를 뽑고, 수식 배열을 복사한 후, 순열에 맞게 연산한다.
  4-1 : eval 함수를 통해 문자열 수식 연산한다.
  4-2 : 연산이 끝나면 결과를 id - 1에 저장하고 연산자와 id + 1에 있던 숫자를 제거한다.
5. 모든 연산이 끝났을 때의 결과에 절댓값을 취하여 answer와 최대값 비교한다.
6. 4~5의 과정을 모든 순열을 완전 탐색할 때까지 반복한다.
