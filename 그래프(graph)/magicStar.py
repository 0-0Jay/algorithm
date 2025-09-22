# 백준 3967번 매직 스타 : https://www.acmicpc.net/problem/3967

from collections import deque
import sys
input = sys.stdin.readline

star = []
xy = []
chk = set();

def DFS(depth):
    a = star[0][4] + star[1][3] + star[2][2] + star[3][1]
    if a > 26 or star[0][4] != 0 and star[1][3] != 0 and star[2][2] != 0 and star[3][1] != 0 and a < 26: return
    b = star[1][1] + star[1][3] + star[1][5] + star[1][7]
    if b > 26 or star[1][1] != 0 and star[1][3] != 0 and star[1][5] != 0 and star[1][7] != 0 and b < 26: return
    c = star[0][4] + star[1][5] + star[2][6] + star[3][7]
    if c > 26 or star[0][4] != 0 and star[1][5] != 0 and star[2][6] != 0 and star[3][7] != 0 and c < 26: return
    d = star[3][1] + star[3][3] + star[3][5] + star[3][7]
    if d > 26 or star[3][1] != 0 and star[3][3] != 0 and star[3][5] != 0 and star[3][7] != 0 and d < 26: return
    e = star[1][1] + star[2][2] + star[3][3] + star[4][4]
    if e > 26 or star[1][1] != 0 and star[2][2] != 0 and star[3][3] != 0 and star[4][4] != 0 and e < 26: return
    f = star[1][7] + star[2][6] + star[3][5] + star[4][4]
    if f > 26 or star[1][7] != 0 and star[2][6] != 0 and star[3][5] != 0 and star[4][4] != 0 and f < 26: return
    
    if depth == len(xy):
        for i in range(5):
            for j in range(9):
                if star[i][j] != '.': print(chr(star[i][j] + 64), end='')
                else: print(star[i][j], end='')
            print()
        exit(0)

    x, y = xy[depth]
    for i in range(1, 13):
        if i not in chk:
            chk.add(i)
            star[x][y] = i
            DFS(depth + 1)
            star[x][y] = 0
            chk.remove(i)

for i in range(5):
    arr = list(input().strip())
    for j in range(9):
        if arr[j] == 'x':
            xy.append((i, j))
            arr[j] = 0
        elif arr[j] != '.':
            arr[j] = ord(arr[j]) - 64
            chk.add(arr[j])            
    star.append(arr)
            
DFS(0)

# 알고리즘 : 백트래킹
'''
풀이 : 매직스타의 각 칸을 미리 좌표쌍(튜플)으로 구해두고 인덱스를 활용해 DFS 탐색한다.
다음 경우에는 숫자를 교체하기위해 백트래킹하며 탐색한다.
1. 한 줄이 가득 찼으나, 합이 26보다 작은 경우
2. 한줄에 포함된 숫자들의 합이 26보다 커지는 경우

숫자 계산에 편의성을 위해 사전에 x는 0으로, A~L은 (아스키코드값 - 64)로 1~12의 숫자로 치환한다.
모든 탐색이 끝나면 치환했던 숫자를 다시 알파벳으로 바꿔주며 출력한다.
'''
