# 백준 1600번 말이 되고픈 원숭이 : https://www.acmicpc.net/problem/1600

from collections import deque

k = int(input())
w, h = map(int, input().split())

field = [list(map(int,input().split(" "))) for _ in range(h)]
chk = [[[0 for _ in range(k + 1)]for _ in range(w)] for _ in range(h)]

dh = [[2, 1], [2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2], [-2, 1], [-2, 1]] # 말 달리기
dn = [[1, 0], [-1, 0], [0, 1], [0, -1]] # 원숭이 달리기
answer = -1

que = deque()
que.append([0, 0, 0, 0])

while que:
    x, y, d, cnt = que.popleft()
    if y == w - 1 and x == h - 1:
        answer = cnt
        break
    if d < k:  # 횟수 남았을 경우에만 실행
        for dx, dy in dh:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < h and 0 <= ny < w and field[nx][ny] == 0 and chk[nx][ny][d + 1] == 0:
                que.append([nx, ny, d + 1, cnt + 1])
                chk[nx][ny][d + 1] = 1
    for dx, dy in dn:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < h and 0 <= ny < w and field[nx][ny] == 0 and chk[nx][ny][d] == 0:
            que.append([nx, ny, d, cnt + 1])
            chk[nx][ny][d] = 1
                
print(answer)

# 알고리즘 : BFS
'''
풀이 : BFS로 탐색하며, 중복 방문 체크를 말처럼 이동한 횟수별로 다르게 체크한다.
말처럼 이동하는 경우의 8 방향과 1칸씩 이동하는 경우의 4방향을 미리 dh, dn 배열에 저장한다.
이후 BFS를 총 12방향으로 탐색한다.
이 때, 말로 이동하면 d를 +1하고, chk의 d+1 인덱스에 체크한다.
이는 곧, d+1번 말처럼 이동했을 경우에 가장 먼저 도착했다는 뜻이다.
d가 k와 같아지면 말처럼 이동하는 8방향은 이동할 수 없기 때문에 배제하고, 4방향만 탐색한다.
answer를 -1로 초기값을 주고 map[-1][-1]에 도착했다면, 이동횟수 cnt를 answer에 옮겨준다.
map[-1][-1]에 도착할 수 없다면 자연스럽게 -1이 출력된다.
'''
