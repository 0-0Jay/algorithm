# 백준 2056번 작업 : https://www.acmicpc.net/problem/2056

from collections import defaultdict, deque
import heapq as hq
import math
import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]
bef = [0] * (n + 1)
time = [0] * (n + 1)
for i in range(1, n + 1):
    tmp = list(map(int, input().split()))
    time[i] = tmp[0]
    for j in range(2, 2 + tmp[1]):
        graph[tmp[j]].append(i)
        bef[i] += 1
        
que = []
for i in range(1, n):
    if bef[i] == 0:
        hq.heappush(que, (time[i], i))
   
res = 0
while que:
    ti, now = hq.heappop(que)
    res = ti
    for nx in graph[now]:
        bef[nx] -= 1
        if bef[nx] == 0:
            hq.heappush(que, (ti + time[nx], nx))

print(res)

# 알고리즘 : 위상 정렬
'''
풀이 : 우선순위 큐를 이용해 먼저 끝나는 작업이 생기면 바로 다음 작업을 수행 시킨다.
res에는 각 작업이 끝난 시점을 계속 갱신한다.
자연스럽게 res에는 마지막 작업이 끝난 시점이 저장되므로, res를 출력한다.
'''
    
