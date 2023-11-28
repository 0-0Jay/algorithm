# 백준 15971번 두 로봇 : https://www.acmicpc.net/problem/15971

from collections import deque
import sys
input = sys.stdin.readline

n, a, b = map(int, input().split())
cave = [[] for _ in range(n + 1)]
chk = set()
for i in range(n - 1):
    st, ed, co = map(int, input().split())
    cave[st].append([ed, co])
    cave[ed].append([st, co])
    
que = deque()
que.append((a, 0, 0))
chk.add(a)

while que:
    now, fin_cost, max_cost = que.popleft()
    
    if now == b: 
        print(fin_cost - max_cost)
        break
    
    for nx in cave[now]:
        if nx[0] not in chk:
            que.append((nx[0], fin_cost + nx[1], max(max_cost, nx[1])))
            chk.add(nx[0])

# 알고리즘 : BFS
'''
풀이 : a로봇이 b로봇으로 이동하는 최단거리까지의 비용을 계산한 후, 가장 높은 비용이 든 통로의 값을 빼준다.
a로봇과 b로봇이 서로 통신을 하게 되면 a로봇과 b로봇 사이에 위치한 통로에 드는 거리는 이동하지 않는다.
따라서 a로봇과 b로봇의 최단거리 이동 방법은 a로봇에서 b로봇까지의 최단거리에서 가장 긴 통로의 길이를 뺀 것과 같다.
이는 곧, a로봇만 b로봇으로 최단거리로 이동한 후, 가장 긴 통로를 빼주는 것과도 동일하다.
따라서 a를 초기값으로, b를 목적지로 두고 BFS를 수행한다.
BFS 탐색을 수행하면서 전체 이동 거리와 이동 중에 만난 가장 긴 통로의 길이를 기록해준다.
목적지에 도착하면 전체 이동 거리에서 가장 긴 통로의 길이를 빼준 값을 출력한다.
'''
