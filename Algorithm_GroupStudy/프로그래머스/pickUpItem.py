# 프로그래머스 - 아이템 줍기 : https://school.programmers.co.kr/learn/courses/30/lessons/87694

from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    max_size = 0
    for i in rectangle:
        for j in i:
            max_size = max(max_size, j)
    max_size *= 2
    field = [[0 for j in range(max_size + 1)] for i in range(max_size + 1)]
    for rec in rectangle:
        for i in range(rec[0] * 2, rec[2] * 2 + 1):
            for j in range(rec[1] * 2, rec[3] * 2 + 1):
                field[i][j] = 1 if field[i][j] != 2 and (i == rec[0] * 2 or i == rec[2] * 2 or j == rec[1] * 2 or j == rec[3] * 2) else 2
        
    que = deque([(characterX * 2, characterY * 2, 0)])
    chk = set({(characterX * 2, characterY * 2)})
    dt = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    answer = 0
    while que:
        x, y, cnt = que.popleft()
        if x == itemX * 2 and y == itemY * 2:
            answer = cnt
            break
        for dx, dy in dt:
            nx = x + dx
            ny = y + dy
            if 0 <= nx <= max_size and 0 <= ny <= max_size and field[nx][ny] == 1 and (nx, ny) not in chk:
                chk.add((nx, ny))
                que.append((nx, ny, cnt + 1))
    return answer // 2

# 알고리즘 : BFS
'''
풀이 : 직사각형의 테두리는 1, 내부는 2로 하여 field 배열에 채워넣고, 1인 좌표만 BFS로 탐색한다.
field에 직사각형을 하나씩 채울 때, 테두리면 1, 내부면 2로 채워넣는다.
이 때, 테두리가 다른 직사각형에 포함된 경우엔 2로 둔다.
모든 직사각형을 채워넣고 나면 characterX와 characterY를 시작점으로 BFS를 수행한다.

그러나 그냥 BFS를 수행하면, ㄷ자 형태로 1칸씩 꺾이는 경우에 그대로 이동하지 않는 문제가 있다.
예제 1번의 경우를 보면 테투리를 따라 (3, 5) -> (4, 5) -> (4, 6) -> (3, 6)으로 ㄷ자로 꺾여야 한다.
그러나 그냥 BFS를 돌면 (3, 5) -> (3, 6)으로 좌표 차이가 1칸밖에 안나기 때문에 일자로 질러가버린다.
이를 해결하기 위해 모든 좌표에 *2를 해주어 사전에 1칸차이가 발생하지 않도록 field를 채워넣는다.

모든 탐색이 끝나면 가장 먼저 도착한 경로의 cnt를 반환한다.
이 때, 모든 좌표에 *2를 했기 때문에 경로의 길이도 *2가 되어있으므로 2로 나누어 반환한다.
'''
