# 프로그래머스 - 문자열 나누기 : https://school.programmers.co.kr/learn/courses/30/lessons/140108

def solution(s):
    answer, id, chk = 1, 0, len(s)
    a, b = 0, 0
    while id < chk:
        if s[0] == s[id]: a += 1
        else: b += 1
        id += 1
        if id == chk: break
        if a == b: 
            answer += 1
            s = s[id:]
            a, b, id, chk = 0, 0, 0, len(s)
                 
    return answer

# 알고리즘 : 시뮬레이션
'''
풀이 : 나누기 전에 문자열 1개이므로 answer에 1을 저장해두고, 분할이 발생할때마다 answer에 1씩 추가한다.
인덱스(id)를 하나씩 옮겨가면서 현재 문자열의 첫 글자와 같으면 a에 +1을 다르면 b에 +1을 한다.
만약 a, b가 같아지면 분할이 발생한 것이므로 answer에 1을 추가하고 s를 s[id:]로 갱신한다.
문자열이 갱신되었기 때문에 a, b도 0으로 초기화하고, id도 초기화한다.
'''
