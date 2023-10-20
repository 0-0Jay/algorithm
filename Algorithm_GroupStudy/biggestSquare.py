# 백준 1915번 가장 큰 정사각형 : https://www.acmicpc.net/problem/1915

import sys
import math
from collections import deque
import heapq as hq

n, m = map(int, input().split())
map = [list(map(int, input())) for _ in range(n)]
max_size = 0

for i in range(0, n):
    for j in range(0, m):
        if i > 0 and j > 0 and map[i][j] > 0:
            map[i][j] = min(map[i - 1][j - 1], map[i - 1][j], map[i][j - 1]) + 1
        max_size = max(max_size, map[i][j])

print(max_size ** 2)

# 알고리즘 : DP(동적계획법)
'''
풀이 : map에 0과 1의 정보를 받고, (1, 1) 인덱스 부터 ↑, ←, ↖칸에 있는 수들 중 최소값 + 1을 현재 칸에 저장한다.
DP를 수행하면서 나오는 숫자중 가장 큰 숫자의 제곱을 출력한다.
'''
