# 백준 11279번 최대 힙 : https://www.acmicpc.net/problem/11279

from collections import defaultdict, deque, OrderedDict
from functools import cmp_to_key
import math
import heapq as hq
import sys
input = sys.stdin.readline

que = [0]
    
def up(k):
    if k // 2 == 0: return
    if que[k] > que[k // 2]:
        que[k], que[k // 2] = que[k // 2], que[k]
        up(k // 2)
        
def down(k):
    nx = k * 2
    if nx >= len(que): return
    if nx + 1 < len(que) and que[nx] < que[nx + 1]: nx += 1
    if que[k] < que[nx]:
        que[k], que[nx] = que[nx], que[k]
        down(nx)
        
n = int(input())
for _ in range(n):
    x = int(input())
    if x == 0:
        if len(que) > 1:
            print(que[1])
            que[1] = que[-1]
            que.pop(-1)
            down(1)
        else: print(0)
    elif x != 0:
        que.append(x)
        up(len(que) - 1)

# 알고리즘 : 우선순위 큐
'''
풀이 : 최대 힙을 구현해본다.
최소 힙의 반대로 구현하면 된다.
'''
