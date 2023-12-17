# 백준 2169번 로봇 조종하기 : https://www.acmicpc.net/problem/2169

from collections import deque
import heapq as hq
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split()))for _ in range(n)]
dt = [[-1, 0], [0, 1], [0, -1]]

for i in range(1, m):
    arr[0][i] += arr[0][i - 1]

for i in range(1, n):
    tmp1 = list(arr[i]) # 왼쪽
    tmp2 = list(arr[i]) # 오른쪽
    for j in range(0, m):
        if j == 0: tmp1[j] += arr[i - 1][j]
        else: tmp1[j] += max(arr[i - 1][j], tmp1[j - 1])
    for j in range(m - 1, -1, -1):
        if j == m - 1: tmp2[j] += arr[i - 1][j]
        else: tmp2[j] += max(arr[i - 1][j], tmp2[j + 1])
    for j in range(0, m):
        arr[i][j] = max(tmp1[j], tmp2[j])
        
print(arr[-1][-1])

# 알고리즘 : DP
'''
풀이 : 왼쪽에서 올 때의 최대값과 오른쪽에서 올 때의 최대값을 계산한 뒤, 최대값끼리 한번 더 최대값 계산한다.
왼쪽에서 오른쪽으로 갈 때는 현재 칸의 왼쪽과 위쪽 칸을 비교해 더 큰 값을 가져와 현재 칸에 합한다.
오른쪽에서 왼쪽으로 갈 때는 현재 칸의 오른쪽과 위쪽 칸을 비교해 더 큰 값을 가져와 현재 칸에 합한다.
이 후, 두 계산 결과 중 더 큰 값이 해당 칸의 최대 값이 된다.

이런 방식으로 위에서부터 아래로 한 줄 씩 계산하고, 마지막 칸을 출력한다.
'''
