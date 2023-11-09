# 백준 16954번 움직이는 미로 탈출 : https://www.acmicpc.net/problem/16954

from collections import deque
import heapq as hq
import sys

arr = [list(input()) for _ in range(8)]
d = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, -0], [0, 1], [1, -1], [1, 0], [1, 1]]

que = deque()
que.append([7, 0, 0])
tmp = 0
while que:
    x, y, sec = que.popleft()
    if sec > tmp:
        tmp = sec
        arr.pop()
        arr.insert(0, [".", ".", ".", ".", ".", ".", ".", "."])
    if arr[x][y] == "#": continue
    if x <= tmp:
        print(1)
        exit(0)
    for i in range(9):
        nx = x + d[i][0]
        ny = y + d[i][1]
        if 0 <= nx < 8 and 0 <= ny < 8 and arr[nx][ny] == ".":
            que.append([nx, ny, sec + 1])
            
print(0)

# 알고리즘 : BFS
'''
풀이 : sec를 통해 초를 세고, tmp를 통해 같은 시간은 같은 미로를 사용하게 컨트롤 해준다.
캐릭터가 할 수 있는 행동은 상하좌우 및 대각선 총 8방향과 제자리에 가만히 있는 1가지 총 9가지로, 이를 미리 d배열에 저장해둔다.
중복된 위치로 이동하는 것이 답이 될 수 있으므로 중복체크는 수행하지 않는다.
이동한 위치의 x좌표가 tmp 이하라는 것은 이미 모든 벽을 지나쳤다는 뜻이다.
따라서 즉시 1을 출력하고 불필요한 탐색은 배제한다.

벽의 이동은 list 함수인 pop과 insert(0, )을 활용해 컨트롤 해주고,
벽을 만난 캐릭터는 continue해서 que에서 제거해준다.
