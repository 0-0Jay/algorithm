# 백준 14003번 가장 긴 증가하는 부분 수열 5 : https://www.acmicpc.net/problem/14003

from collections import deque
import heapq as hq
import sys
from unittest.util import _MAX_LENGTH
input = sys.stdin.readline
from bisect import bisect_left

n = int(input())
arr = list(map(int, input().split()))
dp = [0] * n
tmp = []
lis = []
ml = 0
idx = 0

for i in range(n):
    if len(lis) == 0 or lis[-1] < arr[i]:  # lis가 비었거나, lis의 마지막 수보다 크면 삽입
        lis.append(arr[i])
        dp[i] = len(lis)
    else:
        k = bisect_left(lis, arr[i])  # 이분탐색으로 lis에서 들어갈 수 있는 위치 탐색
        lis[k] = arr[i]
        dp[i] = k + 1
    if dp[i] > ml: # 최장 길이 및 최장 길이가 된 인덱스 기록
        idx = i
        ml = dp[i]
         
print(ml)
tmp.append(arr[idx])  # tmp에 삽입
for i in range(idx, -1, -1):
    if arr[i] < arr[idx] and dp[i] == dp[idx] - 1:
        tmp.append(arr[i])
        idx = i

while tmp:  # tmp가 빌 때까지 역순으로 출력
    print(tmp.pop(), end = " ")

# 알고리즘 : LIS - O(n*logn)
'''
풀이 : LIS알고리즘을 응용한다.
LIS 탐색을 통해 최장 길이를 구하면서 DP배열에 lis배열에서 현재 수가 위치할 수 있는 인덱스를 기록한다.
최장길이를 갱신하면 갱신한 시점의 인덱스와 길이를 idx와 ml에 저장한다.

위 과정 후 LIS는 단순히 최장 길이 계산이 끝난 수열이 존재하기 때문에 주어진 수열의 부분 수열이 되지 못한다.
이분탐색 후 lis에 숫자를 교체하는 과정에서 lis[k] = arr[i]를 하면 뒤에 있던 숫자가 앞으로 순서가 바뀌기 때문이다.
즉, lis는 최장 길이 계산에만 사용하고 실제 부분수열은 역추적을 통해 접근해야한다.

DP에 lis배열에서의 위치를 기록한 이유가 이것 때문이다.
DP배열은 수열에서 각 수의 최적 위치 인덱스를 기록하고 있다.
따라서 탐색 과정에서 저장해두었던 idx를 시작으로 DP[idx]가 DP[i]보다 1크면서, arr[i]가 arr[idx]보다 작은 시점의 수를 tmp에 추가한다.
이렇게 추가하면 tmp에는 가장 긴 증가하는 부분 수열이 역순으로 들어가게 된다.(append로 삽입했기 때문)
출력할떄는 tmp가 빌 때까지 tmp의 수를 pop으로 꺼내어 출력하면 된다.
'''
