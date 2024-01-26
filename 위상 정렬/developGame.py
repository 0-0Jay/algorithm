# 백준 1516번 게임 개발 : https://www.acmicpc.net/problem/1516

import heapq as hq
import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]
bef = [0] * (n + 1)
cost = [0] * (n + 1)
res = [0] * (n + 1)
for i in range(1, n + 1):
    tmp = list(map(int, input().split()))
    cost[i] = tmp[0]
    for j in range(1, len(tmp) - 1):
        bef[i] += 1
        graph[tmp[j]].append(i)

que = []
for i in range(1, n + 1):
    if bef[i] == 0:
        hq.heappush(que, (cost[i], i))

while que:
    co, now = hq.heappop(que)
    res[now] = co
    
    for nx in graph[now]:
        bef[nx] -= 1
        if bef[nx] == 0:
            hq.heappush(que, (co + cost[nx], nx))
            
for i in range(1, n + 1):
    print(res[i])

# 알고리즘 : 위상 정렬
'''
풀이 : 우선순위 큐를 활용해 위상 정렬한다.
어떤 건물이 지어지면 바로 다음에 지을 수 있는 건물을 지으려면 먼저 지어지는 건물부터 이어서 지어야한다.
따라서 우선순위 큐를 이용해 더 빠른 시간에 완성되는 건물을 계속해서 pop한다.
어떤 건물이 완성되면 다음에 지을 수 있는 건물에 대해 (현재 건물 완성 시간 + 다음 건물 소요 시간)을 큐에 넣는다.
이러면 어떤 건물이든 가장 빨리 지어졌을 때의 시간을 구할 수 있다.
우선순위 큐에서 pop될 때마다 res에 해당 건물의 최종 소요시간을 체크해두고, 마지막에 1번부터 차례대로 출력한다.
'''
