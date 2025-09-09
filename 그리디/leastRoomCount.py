# 백준 19598번 최소 회의실 개수 : https://www.acmicpc.net/problem/19598

import sys
import math
from collections import deque
import heapq as hq

n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
hq.heapify(arr)
que = []
cnt = 0

while arr:
    now = hq.heappop(arr)
    if len(que) == 0: 
        hq.heappush(que, now[1])
    else:
        tmp = hq.heappop(que)
        if tmp > now[0]:
            hq.heappush(que, tmp)
        hq.heappush(que, now[1])
            
print(len(que))

# 알고리즘 : 그리디
'''
풀이 : 매 탐색마다 가장 빨리 끝나는 회의를 교체하거나, 회의실을 추가한다.
두개의 우선순위 큐 A, B를 선언하고, A에는 모든 회의의 정보를 저장한다.
A에서 시작시간이 가장 빠른 회의 하나를 pop해서 그 회의의 종료시간을 B에 넣는다.
B에서 pop하면 종료시간이 가장 빠른 회의가 반환되는데, 이를 A에서 pop한 회의의 시작시간과 비교한다.
만약 A에서 꺼낸 회의가 B에서 꺼낸 회의보다 뒤에 시작한다면 회의실을 이어서 사용하면 된다.
 -> B에서 꺼낸 회의는 버리고, A의 회의를 B에 추가한다.
그러나 반대의 경우는 회의실을 하나 더 배정하기때문에 B에 A의 회의를 추가한다.
최종적으로 B의 크기가 필요한 회의실의 수가 된다.
'''
