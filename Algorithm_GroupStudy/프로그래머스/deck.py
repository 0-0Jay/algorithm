# 프로그래머스 - 카드 뭉치 : https://school.programmers.co.kr/learn/courses/30/lessons/159994

def solution(cards1, cards2, goal):
    c1, c2, key = 0, 0, 0
    while key < len(goal):
        if c1 < len(cards1) and cards1[c1] == goal[key]:
            key += 1
            c1 += 1
            continue
        if c2 < len(cards2) and cards2[c2] == goal[key]:
            key += 1
            c2 += 1
            continue
        return "No"
    return "Yes"

# 알고리즘 : 구현
'''
풀이 : 각 배열을 탐색할 키값을 두고 한칸씩 이동하며 goal과 비교한다.
cards1과 cards2에서 순서대로 뽑을 수 있기 때문에 가장 위에 있는 카드 두 개 중 하나를 골라 goal에 채우면 된다.
배열에서 가장 왼쪽에 있는 수를 pop하는 것은 비효율이기 때문에 c1, c2, key로 3개의 키값을 두고, 하나를 사용할 때마다 1씩 올려주는 방법을 사용한다.
key가 goal의 끝까지 이동했다면, 가능하다는 뜻이므로 Yes를 리턴한다. 만약 한번이라도 두 카드 모두 사용할 수 없을 경우 No를 리턴한다.
'''
