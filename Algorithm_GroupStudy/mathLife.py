# 백준 17265번 나의 인생에는 수학과 함께 : https://www.acmicpc.net/problem/17265

import sys
import math
from collections import deque

n = int(input())
arr = [input().split() for _ in range(n)]
chk = [[[-1e12, 1e12] for _ in range(n)] for _ in range(n)] # 0 : 최대값, 1: 최소값
que = deque()
d = [[1, 0], [0, 1]]

que.append([0, 0, arr[0][0], 0])
while que:
    x, y, now, deep = que.popleft()
    if deep % 2 == 0:
        now = eval(now)
        if now > chk[x][y][0] : chk[x][y][0] = now
        if now < chk[x][y][1] : chk[x][y][1] = now 
        now = str(now)
    for i in range(2):
        nx = x + d[i][0]
        ny = y + d[i][1]
        if 0 <= nx < n and 0 <= ny < n:
            que.append([nx, ny, now + arr[nx][ny], deep + 1])
            
print(chk[-1][-1][0], chk[-1][-1][1])

# 알고리즘 : BFS + 브루트 포스
'''
풀이 : eval 함수를 이용해서 BFS를 수행한다.
0, 0 인덱스부터 시작해서 -1, -1 인덱스 까지 이동하면서 만나는 숫자 또는 연산자를 문자열 덧셈으로 합친다.
이동한 칸수를 카운팅하는 d를 하나 주고, 2칸 이동할 때마다 eval을 통해 값을 계산한다.
계산한 값을 현재칸에 기존에 있던 최대값, 최소값과 비교하여 교체 과정을 수행한다.

주의할 점은, 탐색할 때 값이 더 높은 연산자, 더 높은 숫자로 가는 것이 무조건 옳은 방향일 수 없다는 점이다.
 ex ) 3 - 2
      + 0 *
      1 - 9
따라서 배제 작업 없이 모든 루트를 탐색하는 브루트 포스 방식으로 탐색해야 한다. 
'''
