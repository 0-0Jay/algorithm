# 백준 2170번 선 긋기 : https://www.acmicpc.net/problem/2170

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
sum, chk, s = 0, 0, 0
for key, val in arr:
    if chk == 0: s = key
    chk += val
    if chk == 0: sum += key - s
    
print(sum)

# 알고리즘 : 스위핑
'''
풀이 : chk가 0이 될때마다 현재좌표 - 시작좌표한 값을 sum에 더한다.
chk가 0이라면 현재 선분이 없다는 뜻이므로 이번에 arr에서 뽑힌 좌표를 s에 저장한다.
시작점(1)과 끝점(-1)을 chk에 계산하다가 chk가 0이되는 순간 s부터 현재 좌표까지의 거리를 sum에 누적한다.
'''
