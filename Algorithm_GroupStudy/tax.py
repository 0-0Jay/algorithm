# 백준 13907번 세금 : https://www.acmicpc.net/problem/13907

import heapq as hq
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
s, d = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))
    graph[b].append((a, w))

dist = [[1e12] * n for _ in range(n + 1)]
dist[s][0] = 0
que = [(0, s, 0)]
while que:
    cost, now, cnt = hq.heappop(que)
    for i in range(cnt + 1):
        if dist[now][i] < cost:
            cost = -1
            break
    if cost == -1: continue
    for nx, co in graph[now]:
        if cnt < n - 1 and dist[nx][cnt + 1] > cost + co:
            dist[nx][cnt + 1] = cost + co
            hq.heappush(que, (dist[nx][cnt + 1], nx, cnt + 1))

tax, limit = 0, 0
min_val = 1e12
for i in range(n):
    if min_val > dist[d][i]:
        min_val = dist[d][i]
        limit = i
print(min_val)
for _ in range(k):
    tax += int(input())
    min_val = 1e12
    for i in range(limit + 1):
        if min_val > dist[d][i] + tax * i:
            min_val = dist[d][i] + tax * i
            limit = i   
    print(min_val)

# 알고리즘 : DP + 다익스트라
'''
풀이 : 각 노드의 방문까지 거친 경로 갯수마다 최소 비용을 기록한다.
이 문제의 가장 큰 문제는 현재의 최소값 경로가 세금 인상 후에도 여전히 최소값 경로는 아니라는 것이다.
따라서 각 도시마다 몇개의 경로를 거쳤는지를 인덱스로 사용하기 위해 dist 배열을 2차원으로 설정해준다.
즉, dist[i][j]는 i번 도시에 j개의 경로를 거쳤을 때의 최소값이 된다.

위에서 만들 dist배열을 사용하지 않고 일반적인 다익스트라로 문제에 접근했을 경우
최대 30000개의 도로에 대한 다익스트라를 30000번 반복하기 때문에 시간이 반드시 초과된다.
따라서 1회의 다익스트라를 통해 dist에 각 도시까지 경로 갯수별 최소 비용을 저장해두고, 이 dist를 k번 탐색하는 방법을 사용한다.

< 최적화 영역(하지않을 경우 파이썬에서는 반드시 시간초과가 발생한다.) >
일반적으로 현재 cost가 dist[now]보다 크다면 더 돌아도 최소값이 될 수 없으므로 continue를 통해 탐색하지 않는다.
그러나 이번 dist는 2차원이기때문에 현재 방문 수에 따른 최소값을 전부 비교해주어야 한다.
어떤 경로던, 지금 도시에 현재 까지 이동한 경로 수보다 작으면서, 비용이 더 작은 경로가 있다면, 추가로 탐색할 필요가 없다.
따라서 for문을 통해 현재도시의 0 ~ cnt 개의 경로 수의 최소값을 비교해서 한번이라도 더 작은 경로가 있다면 탐색을 멈춘다.

마지막으로 인상한 세금별 최소값을 계산하기위해 dist[d]를 탐색한다.
최소비용을 구하면서, 그 최소비용을 얻기 위해 거친 경로 수를 limit에 저장한다.
이 때, limit보다 더 많은 경로 수는 계산할 필요가 없다. 왜냐하면 (경로 수 * tax)값이 더해지기 때문에 더 작은 값이 나올 수 없다.
따라서 limit까지만 탐색하여 최소값을 찾고, 이 때 또한 최소값이 변경되면 limit의 값을 수정해준다.
'''
    
