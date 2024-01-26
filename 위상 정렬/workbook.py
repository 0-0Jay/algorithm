백준 1766번 문제집 : https://www.acmicpc.net/problem/1766

import heapq as hq
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
bef = [0 for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    bef[b] += 1
    
que = []
for i in range(1, n + 1):
    if bef[i] == 0:
        hq.heappush(que, i)

while que:
    now = hq.heappop(que)
    print(now, end = " ")
    
    for nx in graph[now]:
        bef[nx] -= 1
        if bef[nx] == 0:
            hq.heappush(que, nx)

# 알고리즘 : 위상 정렬
'''
풀이 : 일반적인 위상정렬 알고리즘으로 풀 되, 큐 대신 우선순위 큐를 활용한다.
bef 배열에 이전에 풀어야하는 문제의 수를 카운팅하며 a, b를 입력받는다.
bef 배열을 돌며 이전에 풀어야하는 문제가 0개인 숫자들을 우선순위 큐에 push한다.
우선순위 큐에서 하나씩 pop하면서 해당 문제를 풀었을 때 다음에 풀 문제를 우선순위 큐에 push한다.
'''
