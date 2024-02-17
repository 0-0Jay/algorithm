# 백준 1689번 겹치는 선분 : https://www.acmicpc.net/problem/1689

from collections import defaultdict, deque
import math
import heapq as hq
import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    a, b = map(int, input().split())
    arr.append((a, 1))
    arr.append((b, -1))
    
arr.sort()
res, cnt = 0, 0
for key, val in arr:
    cnt += val
    res = max(res, cnt)
    
print(res)

# 알고리즘 : 스위핑
'''
풀이 : 각 좌표를 시작점은 1, 끝점은 -1로 저장하고, 좌표 순으로 오름차순 정렬하여 겹치는 선분의 갯수를 센다.
새로운 선분의 시작이면 1, 기존 선분이 끝났으면 -1을 더해주는 방식이다.
arr을 처음부터 탐색하면서 cnt에 val을 더하는데, val이 1이면 선분이 시작, -1이면 끝이므로 cnt의 수가 곧 겹쳐있는 선분의 수가 된다.
'''
