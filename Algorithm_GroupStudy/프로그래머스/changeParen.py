# 프로그래머스 2020 KAKAO BLIND RECRUITMENT - 괄호 변환 : https://school.programmers.co.kr/learn/courses/30/lessons/60058

import sys
sys.setrecursionlimit(100000)

def solution(p):
    if p == '': return ''
    u, v = '', ''
    
    l, r, flag = 0, 0, 0
    for i in range(len(p)):  # 현재 들어온 문자열이 올바른 문자열인지 확인
        if p[i] == '(': l += 1
        else: r += 1
        if l >= r : flag += 1
        if l == r:  # 한번이라도 균형잡힌 상태가 되면 u, v로 분리시키고 break
            u = p[:i + 1]
            v = p[i + 1:]
            break
    if flag == len(p): return p

    chk = 0
    for i in u:  # u가 올바른 문자열인지 확인
        if i == '(': chk += 1
        else: chk -= 1
        if chk < 0: break

    answer = ''
    if chk == 0: answer += u + solution(v)  # u가 올바른 문자열인 경우
    else:   # 올바른 문자열이 아닌 경우
        answer += '('+ solution(v) +')'
        for j in u[1 : -1]:
            if j == '(' : answer += ')'
            else: answer +='('
    return answer

# 알고리즘 : 재귀
'''
풀이 : 문제에서 제시한 내용을 그대로 만들면 된다.
l과 r에 각각 '(', ')'의 갯수를 카운팅해서 한 번이라도 r이 l의 갯수를 역전하면 올바르지 않다고 판단한다.
l과 r이 한 번이라도 같아지면 균형잡힌 상태로 u, v로 분리할 수 있다.
chk에  '('면 +1, ')'면 -1 해서 한번이라도 음수가 되면 올바르지 않다.
'''
