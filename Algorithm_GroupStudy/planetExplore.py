# 백준 5549번 행성 탐사 : https://www.acmicpc.net/problem/5549

from collections import deque
import heapq as hq
import sys
input = sys.stdin.readline

m, n = map(int, input().split())
k = int(input())
jungle = [[0] * (n + 1) for _ in range(m + 1)]
ocean = [[0] * (n + 1) for _ in range(m + 1)]
ice = [[0] * (n + 1) for _ in range(m + 1)]

for i in range(1, m + 1):
    tmp = [0] + list(input().strip())
    for j in range(1, n + 1):
        if tmp[j] == 'J':
            jungle[i][j] = 1
        elif tmp[j] == 'I':
            ice[i][j] = 1
        else:
            ocean[i][j] = 1

        jungle[i][j] += jungle[i][j - 1]
        ice[i][j] += ice[i][j - 1]
        ocean[i][j] += ocean[i][j - 1]
    for j in range(1, n + 1):
        jungle[i][j] += jungle[i - 1][j]
        ice[i][j] += ice[i - 1][j]
        ocean[i][j] += ocean[i - 1][j]

for i in range(k):
    sx, sy, ex, ey = map(int, input().split())
    j_cnt = jungle[ex][ey] - jungle[ex][sy - 1] - jungle[sx - 1][ey] + jungle[sx - 1][sy - 1]
    i_cnt = ice[ex][ey] - ice[ex][sy - 1] - ice[sx - 1][ey] + ice[sx - 1][sy - 1]
    o_cnt = ocean[ex][ey] - ocean[ex][sy - 1] - ocean[sx - 1][ey] + ocean[sx - 1][sy - 1]
    print(j_cnt, o_cnt, i_cnt)

# 알고리즘 : 2차원 누적합
'''
풀이 : 2차원 누적합을 계산하고, 특정 영역의 누적합을 위해 4개의 영역으로 연산한다.

예를 들어 3,3 부터 5,5까지 영역의 합을 계산하기 위해 다음 4개의 영역이 필요하다.
1. 1,1부터 5,5까지의 합 (전체)
2. 1,1부터 2,5까지의 합 (필요 영역 위쪽)
3. 1,1부터 5,2까지의 합 (필요 영역 왼쪽)
4. 1,1부터 2,2까지의 합 (2번과 3번이 겹치는 영역)

1번 영역에서부터 2번, 3번 영역을 빼면 4번에 해당하는 영역이 두번 빠지므로 마지막에 4번 영역의 값을 더해준다.
'''
