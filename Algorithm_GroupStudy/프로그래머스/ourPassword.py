# 프로그래머스 - 둘만의 암호 : https://school.programmers.co.kr/learn/courses/30/lessons/155652

def solution(s, skip, index):
    alp = []
    id = {}
    skip = set(skip)
    for i in range(97, 123):
        if chr(i) not in skip:
            id[chr(i)] = len(alp)
            alp.append(chr(i))
    answer = ''
    for sp in s:
        answer += alp[(id[sp] + index) % len(alp)]
    return answer

# 알고리즘 : 구현
'''
풀이 : skip의 알파벳을 제외한 알파벳과 해당 알파벳의 인덱스를 기록한 딕셔너리를 만든다.
아스키코드로 97부터 122까지 소문자 알파벳이므로 for문을 통해 알파벳을 하나씩 배열 하나에 담아준다(alp)
이때 미리 skip의 알파벳들을 집합자료구조로 바꾸어 두고, 해당 알파벳이 skip에 포함된 알파벳인지 검사한다.
포함되어 있지 않은 알파벳이라면 alp배열에 담고 해당 인덱스를 딕셔너리(id)에 기록해준다.

skip을 제외한 알파벳 사전이 완성되었다면, s에서 한글자씩 때어 id에서 해당 알파벳의 인덱스를 가져온다.
해당 알파벳의 인덱스에 index만큼 더하고 alp 배열의 길이로 나눈 나머지 인덱스를 구한 후, alp 배열에서 해당 인덱스의 알파벳을 가져와 answer에 추가한다.
모든 철자에 대해 answer에 추가한다.
'''
