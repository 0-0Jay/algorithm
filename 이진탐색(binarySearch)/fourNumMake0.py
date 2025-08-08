# 백준 7453번 합이 0인 네 정수 : https://www.acmicpc.net/problem/7453

import sys
import math
from collections import deque
import heapq as hq

n = int(input())
A, B, C, D = [0 for _ in range(n)], [0 for _ in range(n)], [0 for _ in range(n)], [0 for _ in range(n)]
AB = []
CD = []

for i in range(n):
    A[i], B[i], C[i], D[i] = map(int, input().split(" "))

for i in range(n):
    for j in range(n):
        AB.append(A[i] + B[j])
        CD.append(C[i] + D[j])

AB.sort()
CD.sort()
cnt = 0
n = n * n - 1

for i in AB:
    low, high = None, None
    now = -i
    # 저점 찾기
    l, r = 0, n
    while l < r:
        mid = (l + r) // 2
        if CD[mid] < now: l = mid + 1
        else: r = mid
    low = r
    if CD[low] != now: continue
    # 고점 찾기
    l, r = 0, n
    while l < r:
        mid = (l + r) // 2
        if CD[mid] <= now: l = mid + 1
        else: r = mid
    high = r - 1
    if CD[r] == CD[high]: high += 1
    if CD[high] != now: continue
    # 개수 계산
    cnt += high - low + 1
    
print(cnt);

# 알고리즘 : 이분 탐색 (binary search)
'''
풀이 : A와 B에서 하나씩 뽑아 합한 값, C와 D에서 하나씩 뽑아 합한 값을 구해 두개의 배열로 합쳐서 이분탐색한다.

1. A와 B에서 하나씩 뽑아서 나올 수 있는 모든 경우의 수를 AB 배열에 저장한다.
2. C와 D에서 하나씩 뽑아서 나올 수 있는 모든 경우의 수를 CD 배열에 저장한다.
3. AB배열에서 하나를 뽑아서 CD에서 이분 탐색을 통해 0이 되는 값들 중 가장 왼쪽 인덱스를 low에 저장한다.
4. 3번을 동일하게 한번 더 수행 하되, 이번에는 가장 오른쪽 인덱스를 high에 저장한다.
  4-1. 단, r이 CD의 마지막 인덱스에 위치하는 경우 계산과정에서 마지막 한칸을 빼는 반례가 발생하는데, 이를 체크해준다.
5. cnt에 high와 row의 거리를 누적한다.
'''
