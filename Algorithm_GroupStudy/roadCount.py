# 백준 1577번 도로의 개수 : https://www.acmicpc.net/problem/1577

from collections import defaultdict, deque
from functools import cmp_to_key
import heapq as hq
from copy import deepcopy
import math
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n, m = map(int, input().split())
road = [[0] * (m + 1) for _ in range(n + 1)]
warn = set()
for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    warn.add((a, b, c, d))
    warn.add((c, d, a, b))
 
road[0][0] = 1
dt = [(1, 0), (0, 1)]
que = deque([(0, 0)])
while que:
    x, y = que.popleft()
    
    for dx, dy in dt:
        nx = x + dx
        ny = y + dy
        if 0 <= nx <= n and 0 <= ny <= m and (x, y, nx, ny) not in warn:
            road[nx][ny] += road[x][y]
            warn.add((x, y, nx, ny))
            warn.add((nx, ny, x, y))
            que.append((nx, ny))

print(road[n][m])         
            
# 알고리즘 : DP + BFS
'''
풀이 : 각 지점이 아닌,도로를 방문체크하면서 현재 지점까지 올 수 있는 모든 경우의 수를 다음 지점에 넘겨준다.
BFS를 활용하기 때문에, 같은 깊이가 모두 탐색된 이후에 다음 깊이가 탐색된다.
즉, A 지점에서 B 지점으로 이동하는 경우, A 지점에는 반드시 모든 최단거리 경우의 수가 저장되어 있다.

한 번 지나간 도로를 방문체크 하여 같은 도로를 중복 이동하지 않게 한다.
왜냐하면 A지점에 방문할 수 있는 최단거리 경우의 수가 2개라면, que에도 2개의 경우가 들어가기 때문이다.
-> B지점을 계산할 때 다음지점에 현재 지점의 수를 넘겨주는 절차에 의해 2를 2번 넘겨주어 중복 계산이 이루어진다.

n, m 좌표에 전달된 수를 출력하면 가능한 모든 최단경로의 경우의 수가 된다.
'''
        
