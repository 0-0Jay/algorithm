# 백준 2672번 여러 직사각형의 전체 면적 구하기 : https://www.acmicpc.net/problem/2672

import sys
input = sys.stdin.readline

n = int(input())
x_point = []
y_point = []
square = []
for _ in range(n):
    x, y, dx, dy = map(float, input().split())
    x_point.extend([x, x + dx])
    y_point.extend([y, y + dy])
    square.append([x, y, x + dx, y + dy])
    
x_point.sort()
y_point.sort()
sum = 0

for i in range(0, len(x_point) - 1):
    for j in range(0, len(y_point) - 1):
        a1, b1 = x_point[i], x_point[i + 1]
        a2, b2 = y_point[j], y_point[j + 1]
        tmp = (b2 - a2) * (b1 - a1)
        
        for k in range(n):
            c1, c2, d1, d2 = square[k]  # x, y, x, y
            if c1 <= a1 and b1 <= d1 and c2 <= a2 and b2 <= d2:
                sum += tmp
                break

if sum % 1 == 0: print(int(sum))
else: print('%.2f' %(sum))

# 알고리즘 : 스위핑
'''
풀이 : 2차원 스위핑을 수행한다.
입력과정에서 해당 사각형의 범위와, 사각형의 x좌표 2개와 y좌표 2개를 분리한다.
x좌표는 x좌표끼리, y좌표는 y좌표끼리 모아 오름차순 정렬한다.
이렇게하면 모든 x좌표와 y좌표를 이용해 격자형태로 사각형을 분할한 정보를 알 수 있다.

각 x, y좌표에서 가장 처음 범위부터 순차적으로 탐색한다.
x좌표에서 뽑은 범위와 y좌표에서 뽑은 범위로 만든 사각형이, 입력단계에 주어진 사각형 중 포함된 곳이 있는지 찾는다.
포함되어 있다면 sum에 추가하고, 포함되어 있지 않다면 넘어간다.

마지막 출력단계에서 만약 결과값이 소수점 없이 표현할 수 있다면 int로 정수변환해준다.
아니라면 소수점 둘째 자리까지 포맷팅하여 출력한다.
'''
