# 백준 8012번 한동이는 영업사원! : https://www.acmicpc.net/problem/8012

from collections import defaultdict, deque
import heapq as hq
import math
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n = int(input())
logn = math.ceil(math.log2(n))
graph = [[] for _ in range(n + 1)]
parent = [[0] * (n + 1) for _ in range(logn)]
depth = [0] * (n + 1)
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
que = deque()
que.append((1, 0))
chk = set()
chk.add(1)
while que:
    now, d = que.popleft()
    depth[now] = d
    for nx in graph[now]:
        if nx not in chk:
            chk.add(nx)
            parent[0][nx] = now
            que.append((nx, d + 1))
for i in range(logn - 1):
    for j in range(1, n + 1):
        parent[i + 1][j] = parent[i][parent[i][j]]
        
m = int(input())
now = 1
sum = 0
for _ in range(m):
    a = now
    b = int(input())
    now = b
    if depth[a] < depth[b]: a, b = b, a
    diff = depth[a] - depth[b]
    for j in range(logn):
        if diff & (1 << j): 
            a = parent[j][a]
            sum += 2 ** j
        if depth[a] == depth[b]:break
    if a == b: continue
    else:
        for j in range(logn - 1, -1 , -1):
            if parent[j][a] != parent[j][b]:
                a = parent[j][a]
                b = parent[j][b]
                sum += 2 ** (j + 1)  # 2를 곱하는 것은 2의 제곱수에 +1을 하는 것과 같음
        sum += 2
print(sum)

# 알고리즘 : 최소 공통 조상(LCA)
'''
풀이 : 도시마다 이전 도시와의 최소 공통 조상을 찾고, 비용을 계산한다.
입력받으면서 간선 정보를 기록하고, 이를 이용해 부모 정보, 깊이를 BFS로 탐색해 기록한다.
이 후, 기록한 부모 정보를 DP를 사용해서 희소배열로 가공한다.

m만큼의 도시가 입력되는데, now에 초기 도시로 포항시청의 위치인 1을 저장한다.
두 도시의 최소 거리는 두 도시의 최소 공통 조상까지의 거리의 합과 같다.
ex) 3 -> 1 -> 2의 경로라면 3 -> 1의 거리와 2 -> 1의 거리의 합과 같다.
이를 이용하기 위해 now에 현재 도착한 도시(b)를 계속 업데이트 해주면서, 최소 공통 조상을 탐색한다.

거리의 계산은 LCA(logn) 알고리즘에 의해 건너 띄는 값(j)만큼 2를 제곱한 값을 더한다.
둘 중 더 깊은 깊이를 올려 동일한 깊이로 맞춰주는 과정에서는 하나만 이동하기 때문에 1번 만 더한다.
이 후, 최소 공통 조상까지 이동하는 과정에서는 두 개가 함께 이동하기 때문에 2를 곱해 더한다.
마지막으로 두 도시 a, b가 최소 공통 조상 바로 아래에 위치해있기 때문에 각각 1씩 올린다.(+2)
모든 도시를 돌았다면, sum을 촐력한다.
'''
