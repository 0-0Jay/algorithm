# 백준 22944번 죽음의 비 : https://www.acmicpc.net/problem/22944

import sys

n, h, d = map(int, input().split())
map = [0 for _ in range(n)]
chk = [[-1 for _ in range(n)] for _ in range(n)]
point = []
sx, sy, ex, ey = 0, 0, 0, 0
umb = 0

def DFS(x, y, cnt, health):
    global umb
    if health < 0: return
    if cnt < chk[x][y] or chk[x][y] == -1:
        chk[x][y] = cnt
    else: return
    if x == ex and y == ey:
        return
    
    for p in point:
        if p[0] == x and p[1] == y: continue
        distance =  abs(p[0] - x) + abs(p[1] - y)
        nh = health + umb - distance if umb < distance else health
        tumb = umb
        umb = d
        DFS(p[0], p[1], cnt + distance, nh)
        umb = tumb
        
    return

for i in range(n):
        map = list(input())
        for j in range(n):
            if map[j] == "S":
                chk[i][j] = 1
                sx, sy = i, j
            elif map[j] == "U":
                point.append([i, j])
            elif map[j] == "E":
                point.append([i, j])
                ex, ey = i, j
            else: continue

DFS(sx, sy, 0, h)
print(chk[ex][ey])

# 알고리즘 : 백트래킹
'''
풀이 : 체력이 음수가 되지 않는 모든 지점을 순회하며 최종 도착지점의 최단 거리를 계산한다.
입력받을때 E와 U의 좌표를 전부 point에 넣어놓고 S의 좌표를 시작으로 DFS를 수행한다.
만약 다음 좌표(p)에 갔을때 체력이 음수가 되면 return 한다.
1칸씩 이동하지 않고 무조건 우산 또는 안전지대 좌표만 삽입되기 때문에 남은 우산의 내구도를 일일히 계산할 필요가 없다.
이전 이동에서 우산의 내구도보다 이동거리가 길면 그만큼 체력에서 빼주고, 아니면 그냥 초기화 시켜준다.
'''
