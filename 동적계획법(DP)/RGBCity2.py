# 백준 17404번 RGB거리 2 : https://www.acmicpc.net/problem/17404

from collections import deque
import sys
input = sys.stdin.readline
import copy

n = int(input())
house = [list(map(int, input().split())) for _ in range(n)]
min_cost = 1e12

for i in range(3): # 색깔 선택
    DP = [[0] * 3 for _ in range(n)]
    DP[0] = copy.deepcopy(house[0])
    for j in range(3):
        if j == i: continue  # 선택한 색을 제외하고 모두 최대값 이상 처리
        DP[0][j] = 1e12
    for j in range(1, n):
        DP[j][0] = min(DP[j - 1][1], DP[j - 1][2]) + house[j][0]
        DP[j][1] = min(DP[j - 1][0], DP[j - 1][2]) + house[j][1]
        DP[j][2] = min(DP[j - 1][0], DP[j - 1][1]) + house[j][2]
    DP[-1][i] = 1e12
    min_cost = min(min(DP[-1]), min_cost)
    
print(min_cost)

# 알고리즘 : DP
'''
풀이 : 3가지 색에 대해, n번 집이 1번 집과 다른 색인 2가지경우를 모두 구해서 최소값 비교한다.
현재 집의 색은 이전 집이 선택하지 않은 두 색의 가격을 비교하여 더 작은 값을 가져오는 방식으로 진행한다.

그러나 단순히 이렇게 진행하면 1번 집과 n번 집의 색이 같은 경우도 함께 계산되기 때문에 DP 진행 전 후로 예외처리를 해주어야 한다.
예외처리를 포함한 순서는 다음과 같다.
1. 색을 하나 정한다
2. 정한 색을 제외한 나머지색은 2번집을 탐색할때 최소값 계산에서 반드시 걸러지도록 1e12(임의의 거대한 값)로 설정한다.
3. 이전 집에서 자신의 열을 제외한 나머지 두 열의 값들 중 더 작은 값을 가져오고 자신의 비용을 더한다.
4. 모든 탐색이 끝나면 1번에서 선택한 색은 최소값 계산에서 걸러지도록 1e12로 설정한다.
5. 1번이 선택한 색으로 칠했을 경우에 최소 비용을 min_cost과 최소값 비교 한다.
6. 1-5번과정을 3번(R, G, B) 반복한다.
''' 
