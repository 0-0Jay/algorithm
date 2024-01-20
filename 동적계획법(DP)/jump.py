# 백준 1890번 점프 : https://www.acmicpc.net/problem/1890

import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
chk = [[0] * n for _ in range(n)]
def dp(x, y):
    if x < 0 or x >= n or y < 0 or y >= n: return 0
    if chk[x][y] > 0: return chk[x][y]
    if x == y == n - 1: 
        chk[x][y] = 1
        return chk[x][y]
    val = board[x][y]
    if val == 0: return 0
    chk[x][y] = dp(x + val, y) + dp(x, y + val)
    return chk[x][y]

print(dp(0, 0))

# 알고리즘 : 동적계획법
'''
풀이 : 재귀를 사용한 메모이제이션으로 계산한다.
현재 위치의 가능한 루트는 현재 위치에서 x와 y방향으로 board[x][y]의 값 만큼 이동한 위치의 루트 갯수를 더한 값과 같다.
이를 위해 만약 x나 y방향으로 board[x][y]만큼 이동했을 때 해당 좌표가 n-1, n-1이라면 루트 갯수로 1을 반환한다.
만약 이동할 좌표가 범위를 벗어나거나, 이동할 좌표의 board 값이 0인경우는 0을 반환하여 재귀 오류가 발생하지 않도록 한다.
board가 0인 경우는 x나 y방향으로 0만큼 무한히 재귀가 생성되기 때문에 반드시 예외처리를 해주어야 한다.
chk 배열에는 현재 위치의 루트 갯수를 계산해 저장해둔다. (메모이제이션)
만약 현재 위치에 chk값이 있으면 불필요한 재귀탐색을 수행하지 말고 chk값을 리턴한다.
'''
