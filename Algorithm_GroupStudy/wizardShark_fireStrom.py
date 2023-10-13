# 백준 20058번 마법사 상어와 파이어스톰 : https://www.acmicpc.net/problem/20058
# !! python3에서 시간 초과 / pypy3로 통과

import sys
import math
from collections import deque
import copy


n, q = map(int, input().split(" "))
A = [list(map(int, input().split(" "))) for _ in range(2 ** n)]
li = map(int, input().split(" "))
d = [[0, 1], [1, 0], [0, -1], [-1, 0]]
n = 2 ** n
ice = 0
max_cnt = 0

Atmp = [[0 for _ in range(n)] for _ in range(n)]
def turn(x, y, s):
    for i in range(0, s):
        for j in range(0, s):
            Atmp[x + j][y + s - i - 1] = A[x + i][y + j]
    return

def BFS(x, y):
    cnt = 0
    global ice, max_cnt
    que = deque()
    que.append([x, y])
    ice += A[x][y]
    A[x][y] = 0
    while que:
        now = que.popleft()
        cnt += 1
        for i in range(4):
            nx = now[0] + d[i][0]
            ny = now[1] + d[i][1]
            if nx >= 0 and nx < n and ny >= 0 and ny < n and A[nx][ny] > 0:
                que.append([nx, ny])
                ice += A[nx][ny]
                A[nx][ny] = 0
    if max_cnt < cnt: max_cnt = cnt
    return

for t in li:
    # 배열 회전
    now = 2 ** t
    for r in range(0, n, now):
        for c in range(0, n, now):
            turn(r, c, now)
    # 얼음 계산
    for r in range(0, n):
        for c in range(0, n):
            A[r][c] = Atmp[r][c]
            if Atmp[r][c] > 0:
                cnt = 4  # 빈공간의 갯수
                for j in range(4):
                    nx = r + d[j][0]
                    ny = c + d[j][1]
                    if nx >= 0 and nx < n and ny >= 0 and ny < n and Atmp[nx][ny] > 0:
                        cnt -= 1  # 만약 얼음이 있으면 -1
                if cnt >= 2: A[r][c] -= 1
    
                    
# 남은 덩어리 계산
for i in range(n):
    for j in range(n):
        if A[i][j] > 0:
            # 얼음 발견하면 BFS 수행
            BFS(i, j)
 
print(ice, max_cnt, sep="\n")

# 알고리즘 : 구현 + BFS(너비 우선 탐색)
'''
풀이 : 배열을 회전 시킨 결과를 Atmp로 따로 만들고, A의 값을 수정한다.
A 배열에서 바로 회전시켜서 얼음을 계산하지 않는 이유는 모든 얼음이 동시에 녹기 때문이다.
만약 2중 for문으로 0,0부터 계산을 하게되면 먼저 계산한 얼음이 다음 얼음에 반드시 영향을 미친다.
따라서 Atmp에 배열 회전 결과를 넣고, A를 Atmp의 얼음 정보를 바탕으로 최신화 시켜주는 방식을 사용한다.

1. now에 회전의 크기를 계산하여 저장한다.
2. 2중 반복문을 통해 배열을 회전시켜 Atmp에 저장한다. -> turn 함수(90도 회전)
3. A에 Atmp에 같은 인덱스의 값을 가져온다.
  3-1. A를 빈 배열이라고 생각하고, Atmp에서 같은 인덱스에 인접한 4칸의 빈공간의 갯수가 2칸 이상이면 방금 가져온 값을 -1 한다.
4. 모든 얼음의 계산이 끝나면 BFS를 통해 남은 얼음과 가장 큰 덩어리를 계산한다.
  4-1. 남은 얼음의 양은 BFS가 해당 지점을 탐색할때마다 그 양을 즉시 누적한다.
  4-2. 가장 큰 얼음 덩어리는 2중 반복문이 얼음을 발견할때마다 카운트를 초기화하고, BFS를 수행하며 카운팅을 새로한다.
  4-3. 카운팅한 얼음 덩어리들의 최대값 비교를 수행한다.
'''
