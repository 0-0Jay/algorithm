# 프로그래머스 2019 카카오 개발자 겨울 인턴십 : https://school.programmers.co.kr/learn/courses/30/lessons/64065?language=python3

def solution(s):
    answer = []
    s = s[1:-1]
    s = s.split("},{")
    sz = len(s)
    for i in range(sz):
        s[i] = s[i].replace("{", '')
        s[i] = s[i].replace("}", '')
        s[i] = s[i].split(',')
    s.sort(key=len)
    chk = set()
    for i in range(sz):
        for j in s[i]:
            if j not in chk:
                answer.append(int(j))
                chk.add(j)
    return answer

# 알고리즘 : 구현
'''
풀이 : 주어진 문자열을 2차원 배열로 가공하고, 각 원소의 길이를 기준으로 오름차순 정렬한다.
각 원소배열을 탐색하면서 이미 선택한 숫자인지 검사한다.
이미 선택한 숫자가 아니면 answer에 추가한다.
가장 짧은 배열부터 선택되기 때문에 반드시 기존 튜플 순서대로 answer에 추가되게 된다.
'''
