# 프로그래머스 - 체육복 : https://school.programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):
    lost = set(lost)
    reserve = set(reserve)
    reserve, lost = reserve - lost, lost - reserve
    for i in reserve:
        if i - 1 in lost:
            lost.remove(i - 1)
        elif i + 1 in lost:
            lost.remove(i + 1)
    return n - len(lost)

# 알고리즘 : 그리디
'''
풀이 : 더 작은 체육복부터 더 작은 사람에게 빌려준다.
먼저 잃어버린 사람과 여벌을 가져온 사람을 집합 자료구조로 만든다.
차집합을 활용해 겹치는 두 집합의 겹치는 사람을 제거한다. 
여벌을 가지고 온 사람을 하나씩 꺼내어 1 작은 사람에게 빌려줄 수 있는지 확인하고 있으면 빌려준다.
1 작은 사람이 없으면, 1 큰 사람에게 빌려줄 수 있는지 확인하고 있으면 빌려준다.
모든 대여가 끝나면 n에서 lost에 남아있는 번호의 개수를 뺀 수를 반환한다.
'''
