# 백준 17472번 다리 만들기2 : https://www.acmicpc.net/problem/17472

from collections import defaultdict, deque
from functools import cmp_to_key
import heapq as hq
import math
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
land = [list(map(int, input().split())) for _ in range(n)]
dt = [[1, 0], [0, 1], [-1, 0], [0, -1]]
land_num = 1  # 영역 별 구분을 위한 번호

for i in range(n):
    for j in range(m):
        if land[i][j] == 1:
            land_num += 1
            que = deque()
            que.append((i, j))
            land[i][j] = land_num
            
            while que:  # BFS를 통해 하나의 영역에 동일한 번호 부여
                nowx, nowy = que.popleft()
                
                for k in range(4):
                    nx = nowx + dt[k][0]
                    ny = nowy + dt[k][1]
                    if 0 <= nx < n and 0 <= ny < m:
                        if land[nx][ny] == 1:
                            land[nx][ny] = land_num
                            que.append((nx, ny))

bridge = []
def check_other(x, y):  # 해당 땅을 기준으로 상하좌우 방향에 다른 섬이 있는지 체크
    now = land[x][y]
    for i in range(x - 1, -1, -1):  # 위 방향
        if land[i][y] == now: break  # 만약 그 방향에 현재 영토와 같은 숫자가 있으면 더이상 탐색하지 않음
        elif land[i][y] != now and land[i][y] > 0:  # 다른 영토가 있으면 간선 정보로 가공하여 bridge에 저장
            bridge.append([now, land[i][y], x - i - 1])
            break
            
    for i in range(x + 1, n):  # 아래 방향
        if land[i][y] == now : break
        elif land[i][y] != now and land[i][y] > 0:
            bridge.append([now, land[i][y], i - x - 1])
            break
            
    for i in range(y - 1, -1, -1):  # 왼쪽 방향
        if land[x][i] == now: break
        elif land[x][i] != now and land[x][i] > 0:
            bridge.append([now, land[x][i], y - i - 1])
            break
            
    for i in range(y + 1, m):  # 오른쪽 방향
        if land[x][i] == now : break
        elif land[x][i] != now and land[x][i] > 0:
            bridge.append([now, land[x][i], i - y - 1])
            break
 
parent = [i for i in range(land_num + 1)]  # 연결 여부를 확인하기 위한 노드 정보 배열
parent[1] = 0  # land_num이 2부터 시작하므로 parent[1]은 임의로 0으로 지정
def union(parent, a, b):
    rootA = find(parent, a)
    rootB = find(parent, b)
    
    if rootA < rootB:
        parent[rootB] = rootA
    else:
        parent[rootA] = rootB
        
def find(parent, x):
    if parent[x] == x:
        return x
    parent[x] = find(parent, parent[x])
    return parent[x]
            
for i in range(n):
    for j in range(m):
        if land[i][j] > 0:
            check_other(i, j)
            
bridge.sort(key = lambda x : x[2])  # 최소길이부터 연결하는 것이 유리하므로 간선 길이 오름차순 정렬
sum = 0
for bd in bridge:
    if bd[2] < 2: continue
    if find(parent, bd[0]) != find(parent, bd[1]):
        union(parent, bd[0], bd[1])
        sum += bd[2]
        
for i in range(2, land_num + 1):  # 모든 섬이 연결되어 있는지 확인하기 위해 부모 노드 정리
    find(parent, i)

chk_connect = set(parent)  # set에 넣었을 때 0, 2 외에 다른 숫자가 있다면 연결 실패
if len(chk_connect) > 2:
    print(-1)
else:
    print(sum)

# 알고리즘 : BFS + 최소 스패닝 트리
'''
풀이 : BFS로 모든 섬의 정보를 구하고, 최소 스패닝 트리로 섬을 연결한다.
BFS를 통해 각 섬의 영역에 고유한 섬 번호를 부여해 노드로 사용할 수 있게 한다.

land의 모든 인덱스를 탐색하면서 해당 인덱스가 땅이라면 상하좌우 방향으로 다른 섬이 있는지 확인한다.
만약 해당 방향에 자신의 영토가 있다면 그 영토에서 탐색하는 것이 더 유리하므로 더이상 탐색하지 않는다.
다른 영토의 번호가 탐색되었다면 [영토A, 영토B, 거리] 형태의 간선 정보로 bridge에 저장한다.
모든 간선 정보 탐색이 끝나면 bridge를 거리 기준 오름차순으로 정렬한다. 

정렬이 끝난 bridge의 정보를 처음부터 탐색하면서 union/find를 통해 연결한다.
연결하면서 해당 간선의 길이를 sum에 누적시킨다.
모든 연결이 끝났을 때, 모든 섬이 연결되어 있는지 확인하기 위해 find를 한번 더 수행한다.
만약 parent에 저장된 루트 노드가 2개 이상이라면, 모든 섬이 연결되지 않았으므로 -1을 출력한다.
'''
