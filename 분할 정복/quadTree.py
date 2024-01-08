# 백준 1992번 쿼드트리 : https://www.acmicpc.net/problem/1992

from collections import defaultdict, deque
import heapq as hq
import math
import sys
input = sys.stdin.readline

n = int(input())
arr = [list(input().strip()) for _ in range(n)]

def quad_tree(xl, xr, yl, yr):
    if xr - xl == 1: return arr[xl][yl]
    xhalf = (xl + xr) // 2
    yhalf = (yl + yr) // 2

    a = quad_tree(xl, xhalf, yl, yhalf)
    b = quad_tree(xl, xhalf, yhalf, yr)
    c = quad_tree(xhalf, xr, yl, yhalf)
    d = quad_tree(xhalf, xr, yhalf, yr)
    
    if len(a) == 1 and a == b == c == d:
        return a
    else:
        return "(" + a + b + c + d + ")"
    
print(quad_tree(0, n, 0, n))

# 알고리즘 : 분할 정복
'''
풀이 : 2차원 배열을 4 등분하며 검사한다.
1칸이면 더 분해할 수 없으므로 그대로 return한다.
만약 4등분한 결과 a, b, c ,d가 전부 "1"이거나 "0"이면 하나로 합친다.
그렇지 않으면 괄호로 a, b, c, d를 전부 이어붙인 후 괄호로 묶어 반환한다.
'''
