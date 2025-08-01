# 백준 1826번 연료 채우기 : https://www.acmicpc.net/problem/1826

import sys
import math
import heapq as hq

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]  # 0 : 위치 / 1 : 연료
l, p = map(int, input().split())
arr.append([l, 0])
arr.sort()
cnt = 0
heap = []

for i in arr:
    if p < i[0]:
        while heap:
            p += -hq.heappop(heap)
            cnt += 1
            if p >= i[0]:
                break
    if len(heap) == 0 and p < i[0]:
        cnt = -1
        break
    else:
        hq.heappush(heap, -i[1])

print(cnt)

# 알고리즘 : 그리디
'''
풀이 : heap을 사용해 가장 멀리 가는 경우만 고려해서 횟수를 카운트한다.

1. 매 탐색마다 현재 남은 연료양으로 갈 수 있는 범위 내에서 받을 수 있는 연료 량을 heap에 넣는다.
2. heap에서 가장 많은 연료를 주는 지점의 연료를 pop해서 연료에 추가한다.
3. 도착지점 이상으로 움직일 수 있으면 cnt를 출력하고, 못가면 -1을 출력한다.
'''
