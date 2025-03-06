# 프로그래머스 - 택배상자 : https://school.programmers.co.kr/learn/courses/30/lessons/131704#

def solution(order):
    sub = []
    answer = 0
    for i in range(len(order)):
        if i + 1 == order[answer]:
            answer += 1
        else:
            sub.append(i + 1)
        while sub and sub[-1] == order[answer]:
            answer += 1
            sub.pop()
    return answer

# 알고리즘 : 스택
'''
풀이 : 주어진 order가 스택으로 처리할 수 있는 순서인지 확인한다.
택배를 임시로 담아둘 보조 컨테이너 벨트(sub)를 만든다.
answer를 인덱스로 사용하여 order를 0번 인덱스부터 탐색한다.
만약 방금 나온 택배(i + 1)가 order[answer]와 같다면, 트럭에 바로 담는다(answer + 1)
그렇지 않다면, 이 택배를 sub에 쌓는다.
sub에 택배가 있는 경우, sub의 맨 위에 쌓여있는 택배가 order[answer]와 같지 않을 때까지, sub에서 택배를 꺼내 트럭에 담는다.
answer를 인덱스로 사용했기 때문에 모든 탐색이 끝나고 answer의 값이 트럭에 실은 택배 수다.
'''
