# 백준 2141번 우체국 : https://www.acmicpc.net/problem/2141

import sys
import math

dp = []
sum_p = []
ld = rd = 0

n = int(input())
for i in range(n):
    city, people = map(int, input().split(" "))   
    dp.append([city, people, 0, 0])
    sum_p.append(0)
dp = sorted(dp, key=lambda x : x[0])

for i in range(n):
    if i + 1 < n:  # 왼쪽부터 이동
        ld += dp[i][1]
        dp[i + 1][2] = dp[i][2] + ld * (dp[i + 1][0] - dp[i][0])
        sum_p[i + 1] += dp[i + 1][2]  # 사람수 * 이동거리 총합
    if n - i - 2 >= 0:  # 오른쪽 부터 이동
        rd += dp[n - i - 1][1]
        dp[n - i - 2][3] = dp[n - i - 1][3] + rd * (dp[n - i - 1][0] - dp[n - i - 2][0])
        sum_p[n - i - 2] += dp[n - i - 2][3] # 사람수 * 이동거리 총합

min_val = min(sum_p)
for i in range(n):  # 이동거리 총합이 최소가 되는 마을 탐색
    if sum_p[i] == min_val:  
        print(dp[i][0])
        break

# 알고리즘 : DP
'''
풀이 : 마을을 정렬한 후, 이동하면서 증가량을 누적시키고, 누적된 증가량을 마을에 누적시킨다.
일반항을 구하자면 다음과 같다.

i번째 마을을 탐색하는 경우 : 
d = (i - 1) 마을까지의 인구 누적합 + i 마을의 인구
i마을의 총 이동거리 = (i - 1)마을까지의 총 이동거리 + d * (i마을과 i - 1마을의 거리)

위 과정을 정렬된 기준으로 왼쪽에서 접근하는 경우와 우측에서 접근하는 경우로 두번 계산해준다.
모든 계산이 끝났다면 sum_p에 입력된 값이 가장 작은 마을이 우체국을 세울 마을이 된다.
'''
        
