# 프로그래머스 - 덧칠하기 : https://school.programmers.co.kr/learn/courses/30/lessons/161989

from collections import deque

def solution(n, m, section):
    que = deque(section)
    cnt = 0
    now = section[0] + m

    while que:
        cnt += 1
        while que and que[0] < now: que.popleft()
        if que: now = que[0] + m
            
    return cnt

# 알고리즘 : 구현
'''
풀이 : section의 구역들을 큐에 넣고, 범위를 옮겨가며 큐에서 빼낸다.
구역(now)을 section의 벗겨진 첫번째 구역에 m을 더한 값으로 정한다.
que에서 now보다 작은 구역들을 전부 빼내고 cnt에 1씩 추가한다.
이 후, que에 남은 다음 구역에 m을 더한 값으로 now를 갱신한다.
que가 다 비면 cnt를 리턴한다.
'''
