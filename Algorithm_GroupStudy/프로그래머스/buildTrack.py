# 2020 카카오 인턴십 - 경주로 건설 : https://school.programmers.co.kr/learn/courses/30/lessons/67259

import sys
import math
from collections import deque
import heapq as hq

d = [[1, 0], [0, 1], [-1, 0], [0, -1]]

def solution(board):
    s = len(board[0])
    que = deque()
    dp = [[0 for _ in range(s)] for _ in range(s)]
    min_cost = 1000000
    que.append([0, 0, 0, -1]) # x, y, cost, 방향
    while que:
        now = que.popleft()
        if now[0] == s - 1 and now[1] == s - 1 and now[2] < min_cost: 
            min_cost = now[2]
        for i in range(4):
            nx = now[0] + d[i][0]
            ny = now[1] + d[i][1]
            cost = 100
            if now[3] != i and now[3] >= 0: cost = 600
            if 0 <= nx < s and 0 <= ny < s and board[nx][ny] == 0:
                if dp[nx][ny] == 0 or dp[nx][ny] >= now[2] + cost - 400:
                    dp[nx][ny] = now[2] + cost
                    que.append([nx, ny, dp[nx][ny], i])
    return min_cost

# 알고리즘 : dp + BFS
'''
풀이 : dp를 활용해 매 탐색마다 더 작은 비용을 저장하면서 BFS 수행
시작점의 방향은 0,0에서 회전으로 인식하지 않게 -1로 지정한다
방향이 0~3으로 que에 같이 저장되므로, 이번 탐색에 나온 방향과 다음 방향이 다르면 가격이 500을 더한다.

주의할 점이 있다.
 ㅓ, ㅗ, ㅏ, ㅜ 형태의 경주로에서 교차점에서는 회전이 더 작았으나,
직진 2번(100 * 2)과 회전(600)을 수행한 이후에  대소가 역전되는 경우가 있다.
600 - 200인 400만큼을 추가로 고려해서 dp에 저장한다.

도착지점에 도달할때마다 min_cost를 계산하고, 모든 탐색이 끝나면 min_cost를 리턴한다
'''
