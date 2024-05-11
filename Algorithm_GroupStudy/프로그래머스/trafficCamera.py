# 프로그래머스 - 단속카메라 : https://school.programmers.co.kr/learn/courses/30/lessons/42884?language=python3

def solution(routes):
    routes.sort(key = lambda x : x[1])
    answer = 0
    now = -50000
    for st, ed in routes:
        if st > now:
            now = ed
            answer += 1    
    return answer

# 알고리즘 : 그리디
'''
풀이 : 차량이 나간 지점을 기준으로 정렬하고 각 차량의 나간 지점과 진입 지점을 비교한다.
우선 now를 범위 밖의 음수값으로 지정해둔다.
정렬된 차랑 배열에서 하나씩 꺼내어 진입지점(st)을 now와 비교한다.
만약 st가 now보다 크다면, 현재 뽑은 차량은 이전 차량과 겹치지 않는다는 의미다.
따라서 카메라 수를 1 올리고, now를 뽑은 차량의 나간 지점으로 갱신해준다.
작다면 now에 저장된 차량의 경로 범위 안쪽 어딘가에서 겹치기 때문에 카메라 수를 올리지 않는다.
'''
