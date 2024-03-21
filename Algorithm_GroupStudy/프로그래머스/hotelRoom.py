# 프로그래머스 2019 카카오 개발자 겨울 인턴십 - 호텔 방 배정 : https://school.programmers.co.kr/learn/courses/30/lessons/64063

import sys
sys.setrecursionlimit(10000)

def solution(k, room_number):
    answer = []
    parent = {}
    def find(parent, x):
        if parent[x] == x:
            parent[x] += 1
            if parent[x] not in parent:
                parent[parent[x]] = parent[x]
            return x
        parent[x] = find(parent, parent[x])
        return parent[x]
    
    for i in room_number:
        if i not in parent: parent[i] = i
        answer.append(find(parent, i))
    
    return answer

# 알고리즘 : union/find + 딕셔너리
'''
풀이 : 고객이 원하는 방을 find 함수를 응용해 찾고, 해당 방을 배정한 뒤, 다음 루트를 만든다.
room_number를 처음부터 탐색한다.
만약 i번을 원하는데, parent 딕셔너리에 i번이 없다면, 해당 방을 만들고, 고객을 배정하여 answer에 추가한다.
방을 배정하면서, i번의 value를 i + 1번 방으로 해주고, i + 1번 방을 딕셔너리에 추가해준다.
만약 i번 방의 value가 i가 아닌 경우, key와 value가 같아질 때까지 재귀를 돌며 다음에 배정할 방을 찾는다.
이렇게 하면 딕셔너리 특성상 모든 배열을 만들고 배정할 필요 없이 필요한 부분만 추가되므로 효율성 높일 수 있다.
'''
