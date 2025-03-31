# 프로그래머스 - 신규 아이디 추천 : https://school.programmers.co.kr/learn/courses/30/lessons/72410

import re

def solution(new_id):
    answer = re.sub(r'[^0-9a-z-_.]', '', new_id.lower())
    answer = re.sub(r'\.{2,}', '.', answer)
    if len(answer) > 0 and answer[0] == '.' : answer = answer[1:]
    if len(answer) > 0 and answer[-1] == '.' : answer = answer[:-1]
    if answer == '' : answer = 'a'
    if len(answer) > 15: 
        answer = answer[:15]
        if answer[-1] == '.' : answer = answer[:-1]
    while len(answer) < 3:
        answer += answer[-1]
    return answer

# 알고리즘 : 구현(정규표현식)
'''
풀이 : re 모듈을 사용해 정규표현식으로 주어진 아이디를 수정한다.
먼저 숫자, 소문자, -, _, .을 제외한 모든 글자를 공백으로 교체하고, 여러개의 점이 중첩되있으면 하나의 점으로 교체한다.
현재 아이디가 빈문자열이 아니면, 첫글자와 마지막 글자가 .인지 확인하고 맞으면 제거한다.
위 과정 이후 만약 아이디가 빈 문자열이면 a를 넣는다.
반대로 아이디가 16자 이상이면, 15자까지 자르고, 잘랐을때 마지막 글자가 .이면 제거한다.
모든 과정이 끝났을때 아이디가 3글자 미만이면, 3글자가 될 때까지 마지막글자를 반복하고 답을 반환한다.
'''
