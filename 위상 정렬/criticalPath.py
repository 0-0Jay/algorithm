# 백준 1948번 임계경로 : https://www.acmicpc.net/problem/1948

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
bef = [0] * (n + 1)
cost = [0] * (n + 1)
for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    bef[b] += 1
st, ed = map(int, input().split())
    
que = deque()
que.append((0, st))

route = [[] for _ in range(n + 1)]     
def back(k):  # 루트 역추적
    cnt = 0
    chk = set()
    que = deque()
    que.append(k)
    while que:
        now = que.popleft()
        for bef in route[now]:
            cnt += 1  # 사용된 도로 카운팅
            if bef not in chk:  # 이미 카운팅 된 도로가 중복 카운팅 되지 않게 처리
                chk.add(bef)
                que.append(bef)
    print(cnt)
           
while que:
    time, now = que.popleft()
    if now == ed:
        print(time)
        back(now)
        break
    
    for nx, co in graph[now]:
        bef[nx] -= 1
        if time + co > cost[nx]:  # 1분도 쉬지 않았음에도 cost에 기록된 시간보다 오래걸리면 교체
            route[nx].clear()
            route[nx].append(now)
            cost[nx] = time + co
        elif time + co == cost[nx]:  # cost에 기록된 시간과 같으면 경로에 추가
            route[nx].append(now)
            
        if bef[nx] == 0:
            que.append((cost[nx], nx))

# 알고리즘 : 위상 정렬 + BFS
'''
풀이 : 가장 오래 걸리는 인원들의 소요 시간을 구하고, 각 인원들의 이동 경로를 역추적하여 사용한 도로를 구한다.
일반적인 위상정렬과 같이 입력받으면서 이전 노드의 개수를 bef를 카운팅한다.
중간 과정에 관계없이 도착한 시간이 가장 오래 걸리는 인원이 1분도 쉬지 않은 인원이 된다.
따라서 각 노드별로 가장 오래 걸려서 도착하는 인원들과 그 인원들이 어디서 왔는지를 route에 기록한다.
이를 위해 cost에 더 오래 걸린 인원이 생길 때마다 소요 시간과 기록된 경로를 갱신한다.

모든 탐색이 끝나면, 마지막으로 도착한 인원의 시간을 출력한다.
이 후, route에 마지막 노드에서 출발해서 BFS로 경로를 역추적하여 사용된 도로의 개수를 세어 출력한다.
'''
