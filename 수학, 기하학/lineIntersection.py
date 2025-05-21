# 백준 17387번 선분 교차 : https://www.acmicpc.net/problem/17387

from collections import defaultdict, deque
import math
import heapq as hq
import sys
input = sys.stdin.readline

a1, a2, b1, b2 = map(int, input().split())
c1, c2, d1, d2 = map(int, input().split())

def CCW(a1, a2, b1, b2, c1, c2):
    return (a1 * b2 + b1 * c2 + c1 * a2) - (a2 * b1 + b2 * c1 + c2 * a1)

l1 = CCW(a1, a2, b1, b2, c1, c2) * CCW(a1, a2, b1, b2, d1, d2)
l2 = CCW(c1, c2, d1, d2, a1, a2) * CCW(c1, c2, d1, d2, b1, b2)

if l1 == 0 and l2 == 0:
    if min(a1, b1) <= max(c1, d1) and min(c1, d1) <= max(a1, b1) and min(a2, b2) <= max(c2, d2) and min(c2, d2) <= max(a2, b2) : print(1)
    else: print(0)
elif l1 <= 0 and l2 <= 0: print(1)
else: print(0)

# 알고리즘 : CCW
'''
풀이 : CCW를 응용해 선분 교차를 판별한다.
두 직선 a, b가 있을 때, 선분이 교차하는 조건을 구하면 다음과 같다.
1. a 직선을 기준으로 b1에 대한 CCW와 b2에 대한 CCW를 구했을 때, 두 CCW의 곱이 0 이하이다.
2. b 직선을 기준으로 a1에 대한 CCW와 a2에 대한 CCW를 구했을 때, 두 CCW의 곱이 0 이하이다.

그러나, 단순히 위 조건을 가지고 교차를 판별할 수는 없는데, 그 경우가 두 직선이 일직선 상에 위치한 경우다.
두 직선이 겹쳐있는 경우와 겹쳐있지 않을 경우 모두 CCW의 곱이 0이 나오기 때문에 이를 판별해주어야 한다.
이를 위해 만약 a 직선과 b 직선이 일직선 상에 위치한 경우, a의 좌표 간격 사이에 b의 좌표가 포함되는지를 검사해준다.
만약 포함되어 있다면 교차, 포함되어 있지 않다면 교차하지 않는다고 판정한다.
'''
