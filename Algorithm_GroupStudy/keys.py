# 백준 9328번 열쇠 : https://www.acmicpc.net/problem/9328

from collections import deque
import heapq as hq
import sys
input = sys.stdin.readline

dt = [[-1, 0,], [0, -1], [1, 0], [0, 1]]

tc = int(input())
for _ in range(tc):
    h, w = map(int, input().split())
    bd = [['.'] * (w + 2)]
    for i in range(h):
        bd.append(['.'] + list(input().strip()) + ['.'])
    bd.append(['.'] * (w + 2))
    key = set(list(input().strip()))
    doc = 0
    
    bef = -1
    now = 0
    # BFS
    while True:
        chk = set() # 중복 방지
        que = deque()
        que.append((0, 0))
        chk.add((0,0))
        while que:
            nowx, nowy = que.popleft()
        
            for i in range(4):
                nx = nowx + dt[i][0]
                ny = nowy + dt[i][1]
                if 0 <= nx <= h + 1 and 0 <= ny <= w + 1 and (nx, ny) not in chk:
                    if 'A' <= bd[nx][ny] <= 'Z':
                        if bd[nx][ny].lower() in key:
                            bd[nx][ny] = '.'
                            que.append((nx, ny))
                            chk.add((nx, ny))
                            now += 1
                        else:
                            continue
                    elif bd[nx][ny] != '*':
                        que.append((nx, ny))
                        chk.add((nx, ny))
                        now += 1
                        if 'a' <= bd[nx][ny] <= 'z':
                            key.add(bd[nx][ny])
                            bd[nx][ny] = '.'
                        elif bd[nx][ny] == '$':
                            bd[nx][ny] = '.'
                            doc += 1
                    
        if now == bef:  # 탐색 범위가 바뀌지 않았다면 문서 갯수 출력
            print(doc)
            break
        else:
            bef = now
            now = 0

# 알고리즘 : BFS + 구현
'''
풀이 : 열 수 있는 문이 없을 때까지 BFS를 초기화하고 반복한다.

BFS를 1회 탐색할 때마다 다음을 수행한다.
1. 열쇠를 획득하면 열쇠를 key에 넣고, 해당 칸을 '.'로 바꾼다.
2. 문을 마주치면, 열쇠가 있으면 문을 '.'로 바꾼 후 que에 넣고, 없으면 넣지 않는다.
3. 문서를 획득하면 doc에 +1 해준다.
4. 이동했다면 now에 +1 해준다. (총 이동 가능한 칸 수 카운트)

위 과정을 1회 수행하면 현재 가진 열쇠로 갈 수 있는 모든 영역에 위치한 열쇠와 문서를 모두 가져온다.
이를 한 번 더 반복하게 되면, 가진 열쇠가 더 많아졌으므로 이전 탐색에는 가지 못했던 문도 열어서 진행할 수 있다.
이 과정을 계속 반복하다가 이전 탐색에 이동 가능했던 영역과 이번 탐색에 이동 가능했던 영역의 크기가 같으면 doc을 출력한다.
 -> 영역의 크기에 변화가 없다는 것은 아무런 문도 열지 못했다는 의미다.
'''
