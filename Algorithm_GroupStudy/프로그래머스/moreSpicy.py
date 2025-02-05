# 프로그래머스 - 더 맵게 : https://school.programmers.co.kr/learn/courses/30/lessons/42626

import heapq as hq

def solution(scoville, K):
    answer = 0
    hq.heapify(scoville)
    while len(scoville) > 1 and scoville[0] < K:
        a, b = hq.heappop(scoville), hq.heappop(scoville)
        res = a + b * 2
        hq.heappush(scoville, res)
        answer += 1
    if scoville[0] < K : return -1
    return answer

# 알고리즘 : 우선순위 큐(힙)
'''
풀이 : 힙 정렬을 활용해 scoville을 정렬하고, 가장 작은 스코빌 두 개를 뽑아 연산 후, 다시 scoville에 넣는다.
scoville에 남은 요리의 개수가 1개면 더이상 합칠 수 없기때문에 요리의 개수가 2개 이상이고, scoville의 가장 맵지 않은 요리가 K보다 작을 경우 요리를 합친다.
요리를 합칠 때마다 answer에 1씩 카운팅해준다.
만약 scoville에 남은 요리의 개수가 1개인데, 그 요리의 스코빌이 K보다 작다면, 불가능한 경우이므로 -1을 리턴하고, 그외의 경우 answer을 리턴한다.
'''
