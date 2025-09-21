# 백준 2252번 줄 세우기 : https://www.acmicpc.net/problem/2252

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
route = [0] * (n + 1)  # 간선 개수 배열
graph = [[] for _ in range(n + 1)]  # 간선 방향 배열

for i in range(m):
    st, ed = map(int, input().split())
    graph[st].append(ed)
    route[ed] += 1
 
que = deque()
for i in range(1, n + 1):
    if route[i] == 0:
        que.append(i)
        
while que:
    now = que.popleft()
    print(now, end=" ")
    
    for i in graph[now]:
        route[i] -= 1
        if route[i] == 0:
            que.append(i)

# 알고리즘 : 방향성 비순환 그래프 + 위상 정렬
'''
풀이 : 매 탐색마다 자신에게 연결된 간선의 개수가 0인 노드를 큐에 넣는다.
매 입력 당 a -> b가 주어지면 b를 향하는 간선이 하나 있다는 뜻으로 route[b]에 1을 카운팅한다.
최초로 1회 탐색해서 자신에게 연결된 간선이 하나도 없는 노드를 큐에 넣는다. (route[i] == 0)

BFS처럼 탐색하는데, now를 출력하면서 연결된 노드의 간선 수를 1씩 빼준다.
이 때, 해당 노드의 간선 수가 0이되면 큐에 넣는다.
매 탐색마다 자신에게 연결된 간선 수가 0이되면 큐에 넣고, 순서대로 빼주기 때문에 자연스럽게 위상 정렬이 수행된다.
'''
