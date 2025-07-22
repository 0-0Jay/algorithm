# 백준 16946번 벽 부수고 이동하기 4 : https://www.acmicpc.net/problem/16946

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(input().rstrip('\n')) for _ in range(n)]
chk = [[0 for _ in range(m)] for _ in range(n)]
key = 0
blank = [0]
d = [[0, 1], [0, -1], [1, 0], [-1, 0]]

def wall(x, y):
    global key
    key += 1
    que = deque()
    cnt = 0
    que.append((x, y))
    chk[x][y] = key
    
    while que:
        a, b = que.popleft()
        for i in range(4):
            nx = a + d[i][0]
            ny = b + d[i][1]
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == '0' and chk[nx][ny] != key:
                chk[nx][ny] = key
                cnt+= 1
                que.append((nx, ny))
    
    return cnt + 1


for i in range(n):
    for j in range(m):
        if arr[i][j] == '0' and chk[i][j] == 0:
            blank.append(wall(i, j))  # 각 빈칸 무리에 번호를 매겨서 크기를 측정해둠

for i in range(n):
    for j in range(m):
        if arr[i][j] == '1':
            arr[i][j] = 1
            s = set()
            for t in d:
                nx = i + t[0]
                ny = j + t[1]
                if 0 <= nx < n and 0 <= ny < m:
                    s.add(chk[i + t[0]][j + t[1]])
            list(s)
            for t in s:
                arr[i][j] += blank[t]
            print(arr[i][j] % 10, end='')
        else:
            print(0, end='')
    print()
     
# 알고리즘 : BFS
'''
풀이 : 벽을 기준으로 BFS를 돌리는게 아닌, 빈칸을 기준으로 BFS를 돌려서 빈칸을 그룹화하고 그룹별 크기를 기록한다.
2중 for문으로 각 빈칸 그룹별 크기를 기록하고, 2중 for문을 한번 더 돌려서 벽을 탐색한다.
벽을 발견하면 벽의 상하 좌우에 인접한 빈칸 그룹의 번호를 가져온다.
-> 이 때, set 자료구조를 활용해 중복된 그룹번호는 제거한다.
빈 칸 그룹 별 크기를 기록해둔 blank 배열에서 가져온 모든 빈칸 크기를 합산하고, 벽이있던 위치를 + 1하여 출력한다.

만약 단순히 벽을 찾아서 BFS를 돌려 빈칸 크기를 측정하는 방식을 사용하면 시간초과가 발생한다.
그 이유를 예를 들면 다음과 같다.
1111
0000
0000
위의 경우가 주어졌다고 했을 때, 벽을 기준으로 BFS를 돌리면 BFS를 총 4번돌려 맨 윗줄이 8888이 된다.
시간복잡도로 나타내면 4 * O(4n^2)인 셈이다
그러나 빈칸을 기준으로 BFS를 돌리고 그룹 라벨링을 하게 되면 다음처럼 계산을 수행한다.
1111        0000
0000   ->  8888
0000        8888
위의 경우 단순히 벽에서 바로 인접한 칸의 숫자인 8만 가져오면 된다.
이를 시간복잡도로 나타내면 O(n^2) + 4로, 꽤 많은 시간격차가 발생한다.
'''
