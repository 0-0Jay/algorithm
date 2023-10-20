# 프로그래머스 - 명예의 전당(1) : https://school.programmers.co.kr/learn/courses/30/lessons/138477

import sys
import math
import heapq as hq

def solution(k, score):
    answer = []
    heap = []
    for i in score:
        if len(heap) < k: hq.heappush(heap, i)
        else:
            hq.heappush(heap, i)
            hq.heappop(heap)
        answer.append(heap[0])
    return answer

print(solution(3, [10, 100, 20, 150, 1, 100, 200]))

# 알고리즘 : 힙
'''
풀이 : 힙을 사용해서 최대값과 최소값을 날짜별로 계산하여 answer에 append한다.
'''
