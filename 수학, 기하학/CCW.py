# 백준 11758번 CCW : https://www.acmicpc.net/problem/11758

import sys
input = sys.stdin.readline

a1, a2 = map(int, input().split())
b1, b2 = map(int, input().split())
c1, c2 = map(int, input().split())
res = (a1 * b2 + b1 * c2 + c1 * a2) - (a2 * b1 + b2 * c1 + c2 * a1)

if res > 0: print(1)
elif res < 0: print(-1)
else: print(0)

알고리즘 : CCW 알고리즘
'''
풀이 : CCW를 구현해본다.
x좌표와 y좌표를 나란히 나열한 후, 다음과 같이 곱한 값을 합한다.
-> 1번 정점의 x 좌표 * 2번 정점의 y좌표 +....
이를 y좌표도 똑같이 수행한 후 두 결과의 차를 구한다.
res가 0이면 일직선 상에 존재한다.
'''
