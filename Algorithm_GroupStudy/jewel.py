# 백준 2492번 보석 : https://www.acmicpc.net/problem/2492

import sys
input = sys.stdin.readline

n, m, t, k = map(int, input().split())
x_point = []
y_point = []
rock = []
for _ in range(t):
    x, y = map(int, input().split())
    rock.append((x, y))
    x_point.append(x)
    y_point.append(y)

max_cnt = 0 
mx, my = 0, 0
for i in range(t):
    for j in range(t):
        x, y = x_point[i], y_point[j]
        cnt = 0
        for rx, ry in rock:
            if x <= rx <= x + k and y <= ry <= y + k:
                cnt += 1
        if cnt > max_cnt:
            max_cnt = cnt
            mx, my = x, y
            
mx = n - k if mx + k > n else mx
my = m if my + k > m else my + k

print(mx, my)        
print(max_cnt)

# 알고리즘 : 브루트포스
'''
풀이 : 모든 보석의 x좌표와 y좌표를 모아놓고, 하나씩 꺼낸 좌표를 기준으로 k크기의 사각형을 그려서 포함된 보석 수를 센다.
단순히 x좌표 집합과 y좌표 집합에서 하나씩 꺼내서 탐색하면 된다.

단, 출력할 때 사각형이 전체 범위에서 벗어나면 안되므로 다음과 같이 좌표를 보정해준다.
mx + 3이 n보다 크면 mx를 n-k로 보정한다.
my +3이 m보다 크면 my를 m으로 보정한다.
x좌표와 y좌표가 보정되는 방식이 다른이유는 왼쪽 위 꼭짓점을 출력하기 때문이다.
'''
