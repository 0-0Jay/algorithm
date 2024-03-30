# 백준 15486번 퇴사 2 : https://www.acmicpc.net/problem/15486

import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * (n + 1)
maxp = 0
for i in range(n):
    t, p = map(int, input().split())
    if dp[i] < dp[i - 1]: dp[i] = dp[i - 1]
    if i + t <= n and dp[i + t] < dp[i] + p:
        maxp = max(dp[i] + p, maxp)
        dp[i + t] = dp[i] + p

print(maxp)

# 알고리즘 : DP
'''
풀이 : 1일째 부터 n일째까지 값을 입력받아 오늘까지의 최대 비용 + 오늘 상담비와 현재 상담이 끝나는 날짜의 비용을 비교한다.
예제 1번을 예로 들면, 1일째에 3일동안의 상담과 10원의 수익이 있다.
그러면 1일까지 벌 수 있는 최대 비용(첫날이니 아무 수익이 없다)인 0원에 상담비용인 10원을 더한다.
이 후, 이 상담이 끝나는 날의 다음날인 4일째에 저장된 최대 수익과 10원을 비요해 더 큰 값으로 교체한다.
이 과정을 7일째까지 반복한다.
단, 만약 현재 상담이 끝나는 날이 퇴사일 이후라면, 상담이 중간에 중단되기 때문에 이 경우는 수익에서 배제한다.
'''
