# 백준 1194번 달이 차오른다, 가자. : https://www.acmicpc.net/problem/1194

from collections import defaultdict, deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dt = [(0, 1), (1, 0), (0, -1), (-1, 0)]
maze = []
chk = [[0] * m for _ in range(n)]
que = deque()
flag = 0
for i in range(n):
    tmp = list(input().strip())
    maze.append(tmp)
    if flag == 1: continue
    for j in range(m):
        if tmp[j] == '0':
            chk[i][j] = 1
            que.append((i, j, 1, 0))  # x, y, key, cnt
            flag = 1
            break
    
ans = -1           
while que:
    x, y, key, cnt = que.popleft()
    if maze[x][y] == '1':
        ans = cnt
        break
    for i in range(4):
        nx = x + dt[i][0]
        ny = y + dt[i][1]
        if 0 <= nx < n and 0 <= ny < m and chk[nx][ny] & key != key and maze[nx][ny] != '#':
            np = maze[nx][ny]
            if 'A' <= np <= 'F':
                if (1 << (ord(np) - ord('A') + 1)) & key != 0:
                    chk[nx][ny] = key
                    que.append((nx, ny, key, cnt + 1))
            elif 'a' <= np <= 'f':
                k = 1 << (ord(np) - ord('a') + 1)
                if k & key == 0:
                    tmp = key | k
                    chk[nx][ny] = key
                    que.append((nx, ny, tmp, cnt + 1))
                else:
                    chk[nx][ny] = key
                    que.append((nx, ny, key, cnt + 1))
            else:
                chk[nx][ny] = key
                que.append((nx, ny, key, cnt + 1))
                    
print(ans)

# 알고리즘 : 비트마스킹 + BFS
'''
풀이 : 먹은 열쇠를 비트마스킹하여 BFS를 수행한다.
열쇠를 먹을 때 마다 해당 열쇠 알파벳을 아스키 코드로 변환한뒤, key에 비트마스킹한다.
이 때, 이미 먹은 열쇠면 연산하지 않고 지나간다.
비트마스킹을 할 때, 1~6이 아닌 2~7로 하고, 열쇠 없이 지나간 자리를 1, 지나가지 않은 자리를 0으로 둔다.
후에 BFS에서 열쇠없이 지나간 자리를 0, 지나가지 않은 자리를 -1로 할 경우 중복체크 과정에서 오류 발생하기 때문이다.
(-1과 비트 연산하기 때문)

BFS를 수행할 때, 먹은 열쇠가 다르면 이동한다.
단, 내가 지금 먹은 열쇠들이 다음 칸의 chk에 기록된 열쇠들에 완전히 포함된다면, 가지않는다.
이미 내 열쇠를 모두 가진 루트가 지나간 곳이므로 중복 탐색과 다름없기 때문이다.
만약 이 중복체크 과정을 비트마스킹을 사용하지 않는다면, 주어진 메모리를 초과하는 3차원 chk 배열을 사용해야 한다.
'''
