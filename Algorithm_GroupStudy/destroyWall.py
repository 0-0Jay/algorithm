# 백준 2206번 벽 부수고 이동하기 : 

from collections import deque
import sys
input = sys.stdin.readline

n, m= map(int, input().split())
arr = [list(input().rstrip('\n')) for _ in range(n)]
chk = [[[0, 0] for _ in range(m)] for _ in range(n)]
d = [[0, 1], [0, -1], [1, 0], [-1, 0]]
answer = -1

que = deque()
que.append((0, 0, 1, 0)) # 0이면 안부숨, 1이면 부숨

while que:
    x, y, cnt, br = que.popleft()
    if x == n - 1 and y == m - 1:
        answer = cnt
        break
    
    if br == 0:
        for i in range(4):
            nx = x + d[i][0]
            ny = y + d[i][1]
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == '1' and chk[nx][ny][1] == 0:
                chk[nx][ny][1] = 1
                que.append((nx, ny, cnt + 1, 1))
        
    for i in range(4):
        nx = x + d[i][0]
        ny = y + d[i][1]
        if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == '0' and chk[nx][ny][br] == 0:
            chk[nx][ny][br] = 1
            que.append((nx, ny, cnt + 1, br))
       
print(answer)

# 알고리즘 : BFS
'''
풀이 : 벽을 부수든 부수지 않든 길이면 갈 수 있지만, 벽이라면 부수지 않은 경우만 부수고 지나갈 수 있다.
따라서 기본적으로 que에 길이면 삽입하고, 한 번도 벽을 부수지 않았다면 벽을 부수는 탐색을 추가로 수행한다.
각 칸은 벽을 부수고 도착한 경우와 벽을 부수지 않고 도착한 경우를 모두 고려한다.
'''
