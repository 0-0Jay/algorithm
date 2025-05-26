# 백준 12015번 가장 긴 증가하는 부분 수열 2 : https://www.acmicpc.net/problem/12015

import sys
input = sys.stdin.readline
from bisect import bisect_left

n = int(input())
arr = list(map(int, input().split()))
max_len = 0
lis = []

for i in range(n):
    if len(lis) == 0 or lis[-1] < arr[i]:
        lis.append(arr[i])
    else:
        k = bisect_left(lis, arr[i])
        lis[k] = arr[i]
        
print(len(lis))

# 알고리즘 : LIS - O(n*logn)
'''
풀이 : 현재 숫자가 lis의 마지막 숫자보다 높으면 쌓고, 낮으면 lis에서 들어갈 수 있는 가장 왼쪽 위치와 교체한다.
lis가 비어있거나, 마지막 숫자보다 높으면 lis에 arr[i]를 append 하는 방식으로 진행하기 때문에
lis의 길이가 곧 최장 부분 수열의 길이가 된다.
'''
