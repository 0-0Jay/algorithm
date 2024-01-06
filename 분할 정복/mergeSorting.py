# 백준 2751번 수 정렬하기 : https://www.acmicpc.net/problem/2751

from collections import defaultdict, deque
from functools import cmp_to_key
import heapq as hq
import math
import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
    
def mergeSort(l, r):
    if r - l == 1:
        return
    half = (l + r) // 2
    mergeSort(l, half)
    mergeSort(half, r)
    
    lk = l
    rk = half
    now = []
    
    while lk < half and rk < r:
        if arr[lk] < arr[rk]:
            now.append(arr[lk])
            lk += 1
        else:
            now.append(arr[rk])
            rk += 1
        
    if lk == half:
        for i in range(rk, r):
            now.append(arr[i])
    else:
        for i in range(lk, half):
            now.append(arr[i])
        
    for i in range(l, r):
        arr[i] = now[i - l]
    
mergeSort(0, n)
for i in arr:
    print(i)

# 알고리즘 : 분할 정복(merge sorting)
'''
풀이 : 배열을 계속 반 씩 나누어 정렬을 수행한다.
정렬은 2개의 키와 now 배열을 활용한다.
왼쪽 범위의 키와 오른쪽 범위 키의 인덱스를 비교해 더 작은 값을 now에 append하고, 그 키를 1씩 올려준다.
만약 어느 키라도 범위를 벗어나면 반대쪽 범위에 남은 숫자를 전부 now에 순서대로 append한다.
매 정렬마다 왼쪽 범위와 오른쪽 범위가 정렬되어 있음이 보장되어 있기 때문에 정렬할 수 있다.
'''
