# 프로그래머스 - 대충 만든 자판 : https://school.programmers.co.kr/learn/courses/30/lessons/160586#

def solution(keymap, targets):
    fastkey = {}
    for id in range(len(keymap)):
        key = keymap[id]
        for i in range(len(key)):
            if key[i] not in fastkey or fastkey[key[i]] + 1 > i + 1:
                fastkey[key[i]] = i + 1
                
    answer = [0] * len(targets)
    for i in range(len(targets)):
        for alp in targets[i]:
            if alp not in fastkey:
                answer[i] = -1
                break
            answer[i] += fastkey[alp]
    return answer

# 알고리즘 : 구현
'''
풀이 : 주어진 키를 키, 누른 회수를 값으로 두는 딕셔너리를 만든다.
키를 누르는 최소 횟수를 기록할 딕셔너리를 하나 만든다(fastkey)
keymap에서 키를 하나씩 뽑아 그 키에서 각 알파벳을 얻기위해 눌러야되는 횟수를 fastkey에 저장한다.
이 때, 이미 fasykey에 해당 알파벳의 값이 있다면, 기존의 횟수와 비교해 더 작은 값으로 갱신한다.

answer를 targets의 길이만큼 미리 0으로 채워 선언해둔다.
targets에서 단어 하나를 꺼내고 해당 단어에서 알파벳을 하나씩 뽑아 fastkey에서 찾는다.
fastkey에는 이전 과정으로 인해 이미 최소로 누르는 횟수만 저장되어 있으므로 저장된 횟수를 바로 answer에 누적해준다.
이때, fastkey에 해당 알파벳이 키값으로 존재하지 않으면, 어떤 키를 눌러도 그 알파벳을 적지 못한다는 의미이다.
따라서 answer에 누적된 값을 무시하고 -1로 변환해준 후, break하여 다음 단어로 넘어간다.
'''
