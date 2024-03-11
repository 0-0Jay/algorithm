# 백준 1219번 오민식의 고민 : https://www.acmicpc.net/problem/1219

from collections import defaultdict, deque
import sys
input = sys.stdin.readline

INF = -1e9
n, s, e, m = map(int, input().split())
route = [tuple(map(int, input().split())) for _ in range(m)]
income = list(map(int, input().split()))
graph = [[] for _ in range(n)]
route = [(a, b, income[b] - c) for a, b, c in route]
for i in range(m):
    a, b, c = route[i]
    graph[a].append(b)

def go_end(p):  # 현재 도착도시에서 마지막도시까지 연결되어 있는지 확인
    global e
    chk = set({p})
    que = deque([p])
    while que:
        now = que.popleft()
        if now == e:
            return True
        for nx in graph[now]:
            if nx not in chk:
                chk.add(nx)
                que.append(nx)
    return False

cost = [INF] * n
cost[s] = income[s]
def bellman_ford():
    global cost
    for i in range(1, n + 1):
        for a, b, c in route:
            if cost[a] != INF and cost[b] < cost[a] + c:
                cost[b] = cost[a] + c
                if i == n and go_end(b):  # 한 번이라도 사이클이 발생하면 True
                    return True
    return False
                
cycle = bellman_ford()                
if cost[e] == INF:print("gg")
elif cycle: print("Gee")
else: print(cost[e])
   
# 알고리즘 : 벨만_포드 + BFS
'''
풀이 : 벨만 포드를 수행하며 만약 사이클이 존재할 경우 해당 지점이 마지막 도시까지의 경로 상에 있는지 확인한다.
각 도시에 도달할 때마다 이윤이 발생하기 때문에 입력단계에서 받은 route의 가중치를 교통비에서 (수익 - 교통비)로 바꾸어준다.
최대 이윤을 탐색하기 위해 최대값을 찾는 벨만 포드를 수행한다.
이 때, 출발 도시에서 수익은 기본으로 가지고 있기 때문에 income의 값으로 초기화 해준다.
탐색 중에 사이클이 발생했을 경우, 해당 시작-도착 간선에서의 도착도시가 마지막 도시까지 이동할 수 있는지 체크한다.
만약 한 번이라도 이동할 수 있다면 경로 상에서 무한히 돈을 벌 수 있다는 의미이므로 True를 반환한다.
만약 경로상에 있지 않다면 False를 반환하여 해당 사이클이 경로상에 존재하지 않으므로 결과 계산에서 배제시킨다.

모든 벨만 포드 탐색이 끝나면, 시작도시부터 마지막도시까지 연결되어 있는지 확인한다.
cost[e]가 만약 INF라면, 연결 지점이 없어서 가중치 계산이 한 번도 이루어지지 않았다는 의미이므로 "gg"를 출력한다.
cycle이 True라면 무한으로 돈을 벌 수 있으므로 "Gee"를 false라면 cost[e]를 출력해 최대 이윤을 출력한다.
'''
