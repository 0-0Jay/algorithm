from collections import defaultdict, deque
import heapq as hq
import math
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
word = [list(input().strip()) for _ in range(n)]
target = input().strip()
chk = [[[-1 for _ in range(m)] for _ in range(n)] for _ in range(len(target))]
dt = [[0, 1], [1, 0], [0, -1], [-1, 0]]

def DFS(x, y, d):
    if x < 0 or x >= n or y < 0 or y >= m or word[x][y] != target[d]: return 0
    if d == len(target) -1 and word[x][y] == target[-1]:
        chk[d][x][y] = 1
        return 1
    if chk[d][x][y] >= 0: return chk[d][x][y]
    chk[d][x][y] = 0
    for i in range(4):
        for j in range(1, k + 1): 
            chk[d][x][y] += DFS(x + dt[i][0] * j, y + dt[i][1] * j, d + 1)
    return chk[d][x][y]

ans = 0
for i in range(n):
    for j in range(m):
        if word[i][j] == target[0]:
            ans += DFS(i, j, 0)
            
print(ans)

# 알고리즘 : 메모이제이션(DP)
'''
풀이 : 백트래킹 기법으로 배열의 각 칸을 돌면서 chk배열에 가능한 루트의 개수를 기록한다.
이 문제에서 주의할 점은 이미 사용한 문자의 칸이어도 한번 더 방문할 수 있다는 것이다.
예를 들어 sss라는 문자열을 만들어야 하고, 주어진 보드가 2 * 2에 모든 칸이 's'인 경우가 있다.
s s
s s  ex) 이 경우 (0, 0) -> (0, 1) -> (0, 0) 과 같은 루트도 가능하다.
단순한 메모이제이션을 통한 방문 체크가 아닌 깊이에 따라 다른 메모이제이션을 수행해야 한다.
따라서 문자열의 각 자리에 대해 따로따로 DP를 수행해 체크해서 이전 자리에 전달하는 방식을 사용했다.

백트래킹이 동작하는 조건은 다음과 같다.
1. 현재 깊이(d)에서 탐색할 위치의 문자가 target 문자열의 d번째 문자와 다르면 0을 return 한다.
2. 현재 깊이가 target 문자열의 마지막 문자를 탐색하면서 두 문자가 같으면, chk에 1을 기록하고 1을 return 한다.
3. 만약 해당 위치의 값이 0 이상이면 이미 계산한 영역이므로 저장된 값(chk)을 return한다.
현재위치는 상하좌우 k칸 내에 조건에 맞는 영역의 값을 모두 더한 값을 저장한다.
'''
