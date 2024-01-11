# 백준 10282번 해킹 : https://www.acmicpc.net/problem/10282

from collections import defaultdict, deque
from functools import cmp_to_key
import heapq as hq
import math
import sys
input = sys.stdin.readline

test = int(input())
for _ in range(test):
    n, d, c = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    cost = [1e12] * (n + 1)
    for i in range(d):
        a, b, s = map(int, input().split())
        graph[b].append([a, s])
    
    heap = []
    hq.heappush(heap, (0, c))
    while heap:
        co, now = hq.heappop(heap)
        for nx in graph[now]:
            if nx[0] != c and cost[nx[0]] > co + nx[1]:
                cost[nx[0]] = co + nx[1]
                hq.heappush(heap, (cost[nx[0]], nx[0]))
    
    cnt, time = 1, 0           
    for i in range(1, n + 1):
        if i == c: continue
        if cost[i] < 1e12:
            cnt += 1
            time = max(cost[i], time)
            
    print(cnt, time)

# 알고리즘 : 다익스트라
'''
풀이 : 다익스트라로 시작 컴퓨터와 연결된 모든 컴퓨터가 감염되는 최소 시간을 계산한다.
마지막 컴퓨터가 감염되기까지 걸리는 시간은 시작 컴퓨터로 부터 최소 시간으로 마지막 컴퓨터로 이동한 시간이다.
따라서 다익스트라로 연결된 모든 컴퓨터에 대한 최소 접근 시간을 구한다.
모든 계산이 끝났다면 cost 배열을 처음부터 탐색한다.
만약 cost[i]가 임의로 설정한 최대값보다 작다면, 한 번 이상 접근했다는 의미이므로 감염된 컴퓨터로 카운팅한다.

또한, 해당 cost를 time과 최대값 비교하여 감염된 컴퓨터 중에서 가장 늦게 감염되는 시간을 구한다.
이 때, 만약 i번째 컴퓨터가 시작 컴퓨터(c)라면 배제한다. 이를 위해 cnt를 미리 1로 카운팅 해둔다.
왜냐하면, c 컴퓨터는 다익스트라 계산 과정에서 접근하지 않기 때문에 시간이 최대값으로 되어 있기 때문이다.
예외 처리를 하지 않으면 c가 카운팅 되면서 time의 값이 1e12로 고정되버려 제대로 된 계산이 이루어지지 않는다.
'''
