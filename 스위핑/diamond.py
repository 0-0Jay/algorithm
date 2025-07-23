# 백준 2496번 금강석 : https://www.acmicpc.net/problem/2496

import sys
input = sys.stdin.readline

n, m, t, k = map(int, input().split())
x_point = []
y_point = []
max_cnt = 0
max_point = (0, 0)

def find(x, y):
    global max_cnt, max_point
    cnt = 0
    for i in range(t):  # 전체 보석을 탐색하여 현재 마름모 안에 존재하는 갯수 카운팅
        tx, ty = x_point[i], y_point[i]
        if x <= tx <= x + k and y - k <= ty <= y: cnt += 1
    mx = x + k // 2
    my = (mx + (y - k // 2)) // 2
    mx = mx - my  # 중심점 탐색 및 회전하기 전 좌표 복원
    if 0 <= mx <= n and 0 <= my <= m and max_cnt < cnt:
        max_cnt = cnt
        max_point = (mx, my)

for _ in range(t):
    x, y = tuple(map(int, input().split()))
    x_point.append(x + y)  # 시계방향으로 45도 회전
    y_point.append(y - x)
    
for i in x_point:
    for j in y_point:
        if (i + j) % 2 == 0: find(i, j)  # 오차가 없는 좌표인 경우
        else:  # 오차가 있는 좌표인 경우
            find(i - 1, j)
            find(i + 1, j)
            find(i, j - 1)
            find(i, j + 1)
        find(i - k // 2, j + k // 2)

print(*max_point)
print(max_cnt)

# 알고리즘 : 브루트포스 + 스위핑
'''
풀이 : 주어진 좌표들을 45도 회전시킨 값으로 치환한 후, 2차원 스위핑을 통해 보석을 센다.
입력받은 x좌표와 y좌표들을 시계방향으로 45도 회전시킨다.
좌표평면에서 실제 45도를 회전시키는 것은 어려우므로 x 좌표는 x와 y좌표의 합, y 좌표는 y좌표에서 x좌표를 뺀 값으로 치환한다.
이렇게 하면 구해야 하는 마름모의 크기는 2배가 되며, 오차가 존재하는 채로 45도 회전한다.

두 좌표 값의 합이 홀수인 경우 오차가 존재하는 좌표가 된다.
이 경우 정확한 마름모의 꼭짓점을 특정할 수 없기 때문에, 해당 지점 주변 1칸씩을 모두 탐색한다.
탐색할 좌표는 회전했을 때의 사각형을 기준으로 왼쪽 상단 꼭짓점으로 두고 탐색한다.
전체 보석의 좌표(회전한 상태의 좌표)중 회전한 사각형의 범위 내에 존재하는 좌표의 개수를 카운팅하고, 개수의 최대값을 비교한다.
이 때, 해당 사각형을 반시계방향 45도 회전하여 기존 좌표로 복원했을 때, 그 마름모의 중심좌표가 n*m 범위 내일 때만 비교한다.
이 과정을 모든 좌표에 대해 수행했을 때, 저장된 max_cnt와 max_point를 출력한다.
이 때, 최대값이 저장된 좌표가 여럿 존재할 수 있는데, 계산과정에서 더 큰 cnt가 발생할 때만 교체되기 때문에 자연스럽게 필터링 된다.
'''
