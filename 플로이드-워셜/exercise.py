# 백준 1956번 운동 : https://www.acmicpc.net/problem/1956

import sys
from collections import deque
import heapq as hq

v, e = map(int, input().split())
cycle = 2000000000 
chk = [[cycle for j in range(v + 1)] for i in range(v + 1)]
for i in range(e):
    a, b, c = map(int,input().split())
    chk[a][b] = c

for i in range(1, v + 1):
    for j in range(1, v + 1):
        for k in range(1, v + 1):
            chk[i][j] = min(chk[i][j], chk[i][k] + chk[k][j])
    
for i in range(1, v + 1):
    cycle = chk[i][i] if chk[i][i] < cycle else cycle

print(cycle if cycle < 2000000000 else -1)

# 알고리즘 : 플로이드 워셜
'''
풀이 : a -> b로 가는 경로와 a -> c -> b로 c를 한번 거쳐 가는 경로 중 더 짧은 경로를 찾는다.
만약 둘러가는게 더 짧다면 해당 경로를 교체한다.
사이클을 찾는 문제이므로 1번 부터 v번까지 chk[i][i]의 값이 가장 작은 값을 찾는다.
'''
