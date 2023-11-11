# 백준 1937번 욕심쟁이 판다 : https://www.acmicpc.net/problem/1937

from collections import deque
import sys
sys.setrecursionlimit(250000)

n = int(input())
forest = [list(map(int,input().split())) for _ in range(n)]
chk = [[0 for _ in range(n)] for _ in range(n)]
d = [[0, 1], [1, 0], [0, -1], [-1, 0]]
max_cnt = 0

def DFS(x, y):
    global max_cnt
    if chk[x][y] > 0:
        return chk[x][y]
    chk[x][y] = 1
    for i in range(4):
        nx = x + d[i][0]
        ny = y + d[i][1]
        if 0 <= nx < n and 0 <= ny < n and forest[nx][ny] < forest[x][y] :
            chk[x][y] = max(DFS(nx, ny) + 1, chk[x][y])
    
    max_cnt = max(chk[x][y], max_cnt)
    return chk[x][y]

for i in range(n):
    for j in range(n):
        DFS(i, j)
        
print(max_cnt)

# 알고리즘 : DFS + DP
'''
풀이 : 현재 위치에서 역순으로 이동한다고 생각하고 DFS를 돌린다.
현재위치가 가질 수 있는 최대 값은 이전 위치중 최대값에 +1 한 값과 같다.
예를들면 다음과 같다.
6 2 1의 경우, 6위치의 값은 2위치의 값 + 1, 2위치는 1위치의 값 + 1, 1위치는 갈곳이 없으니 1이다.
따라서 6이 가지는 수는 3이 된다.
위와 같은 방식으로 forest의 각 지점에 대한 최대 값을 구하고, 그 값중 최대 값을 구해서 출력한다.
'''
