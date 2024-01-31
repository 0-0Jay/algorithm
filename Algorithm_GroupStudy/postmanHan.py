# 백준 2842번 집배원 한상덕 : https://www.acmicpc.net/problem/2842

from collections import defaultdict, deque
import heapq as hq
import math
import sys
input = sys.stdin.readline

n = int(input())
city = []
sx, sy, house = 0, 0, 0
for i in  range(n):
    tmp = list(input().strip())
    for j in range(n):
        if tmp[j] == 'P':  # P면 시작점 좌표 저장
            sx, sy = i, j
        elif tmp[j] == 'K':  # k면 배달할 집 수에 1 추가
            house += 1
    city.append(tmp)
    
high = []
hlist = set()
for i in range(n):
    tmp = list(map(int, input().split()))
    hlist.update(tmp)
    high.append(tmp)
hlist = sorted(hlist)  # 투 포인터 탐색을 위해 모든 높이를 중복을 제거하고 오름차순으로 정렬

dt = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]
def BFS(x, y, left, right):
    que = deque()
    que.append((x, y))
    chk = [[0] * n for _ in range(n)]
    chk[x][y] = 1
    cnt = 0
    while que:
        nowx, nowy = que.popleft()
        for i in range(8):
            nx = nowx + dt[i][0]
            ny = nowy + dt[i][1]
            # 다음 칸이 최저와 최고의 사이일 때만 전진
            if 0 <= nx < n and 0 <= ny < n and chk[nx][ny] == 0 and left <= high[nx][ny] <= right:
                que.append((nx, ny))
                chk[nx][ny] = 1
                if city[nx][ny] == 'K':
                    cnt += 1         
        if cnt == house: break  # 모든 집 방문 했으면 탐색 그만하고 break
    
    return cnt       

ans = 1000000
l, r = 0, 0
while l <= r and r < len(hlist):
    cnt = 0
    if hlist[l] <= high[sx][sy] <= hlist[r]:
        cnt = BFS(sx, sy, hlist[l], hlist[r]) 
    if cnt < house: r += 1
    else:
        ans = min(ans, (hlist[r] - hlist[l]))
        l += 1
        
print(ans)

# 알고리즘 : 투 포인터 + BFS
'''
풀이 : 투포인터를 이용해 최고/최저 높이를 컨트롤하며 BFS를 탐색한다.
입력 단계에서 P의 좌표를 미리 구해둔다.
높이를 입력받을 때, 배열(hlist)에 중복을 제거해서 넣고, 오름차순 정렬한다.

l(최저), r(최고) 두개의 포인터를 인덱스로 사용하여 hlist를 탐색한다.
만약 우체국의 좌표의 높이가 최저/최고 높이 사이에 위치한다면, BFS를 수행하며 배달가능한 집의 개수를 센다.
경로에 상관없이 무조건 최고-최저가 피로도가 되므로 단순 BFS로 탐색해 집을 발견만 할 수 있으면 카운팅 한다.
BFS 탐색이 끝났을 때, 카운팅한 값이 전체 집 수보다 작다면, 최고 높이를 높여서 탐색한다.
만약 접체 집 수와 같다면, ans와 현재 피로도를 비교해 더 작은 값으로 교체하고, 최저 높이를 높여서 탐색해본다.
'''
