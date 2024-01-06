# 백준 11779번 최소비용 구하기2 : https://www.acmicpc.net/problem/11779

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[1e12] * (n + 1) for _ in range(n + 1)]
for i in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = min(c, graph[a][b])
for i in range(n + 1):
    graph[i][i] = 0
st, ed = map(int, input().split())
    
dist = [1e12] * (n + 1)
route = [0] * (n + 1)
chk = [0] * (n + 1)
dist[st] = 0
idx = st
for _ in range(n - 1):
    if idx == -1: break
    chk[idx] = 1
    s,min = -1, 1e12
    for i in range(1, n + 1):
        if chk[i] == 1: continue
        now = dist[idx] + graph[idx][i]
        if now < dist[i]:
            dist[i] = now
            route[i] = idx
        if min > dist[i]:
            min = dist[i]
            s = i
    idx = s

print(dist[ed])         
tmp = []
while route[ed] != 0:
    tmp.append(ed)
    ed = route[ed]
tmp.append(st)
t = len(tmp)
print(t)
print(*reversed(tmp))

# 알고리즘 : 다익스트라(n^2)
'''
풀이 : 다익스트라를 활용해 경유하는 루트와 바로가는 루트의 크기를 비교해 더 작은 값으로 갱신한다.
만약 값이 갱신 되었다면 route에 어디를 경유해서 왔는지 기록한다.
최단 경로를 계산하면서 최소값을 갖는 노드를 찾아 그 인덱스를 s에 기록하고, 모든 계산이 끝나면 idx에 갱신해준다.
idx는 자연스럽게 가장 적은 비용을 가진 인덱스가 되어 다음 탐색에 사용된다.
'''
