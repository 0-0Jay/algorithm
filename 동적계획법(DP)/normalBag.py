# 백준 12865번 평범한 배낭 : https://www.acmicpc.net/problem/12865

# 상향식 DP(재귀 사용)
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = [0] + [list(map(int, input().split())) for _ in range(n)]
chk = [[0] * (k + 1) for _ in range(n + 1)]

def dp(x, sum):
    if x > n: return 0
    if chk[x][sum] > 0: return chk[x][sum]
    tmp1 = 0
    if sum + arr[x][0] <= k:
        tmp1 = dp(x + 1, sum + arr[x][0]) + arr[x][1]
    tmp2 = dp(x + 1, sum)
    chk[x][sum] = max(tmp1, tmp2)
    return chk[x][sum]

print(dp(1, 0))
##################################################################
# 하향식 DP(2중 for문 사용)
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = [0] + [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, k + 1):
        dp[i][j] = dp[i - 1][j]
        if j - arr[i][0] >= 0:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - arr[i][0]] + arr[i][1])
            
print(dp[n][k])

# 알고리즘 : 동적계획법
'''
풀이 : 두 가지 방법으로 동적계획법을 사용해본다.
재귀를 활용한 DP에서는 현재 사용한 무게를 통해 DP를 수행한다.
같은 양의 보석을 탐색했고, 같은 무게를 채웠다면 동일한 탐색을 수행한다는 점을 이용해 메모이제이션 한다.
다음 보석을 넣는 경우와 넣지 않는 경우에서 가치를 가져와 비교하여 더 높은 것을 현재 보석 위치에 기록한다.

for문을 이용한 DP에서도 마찬가지지만 방향만 바뀐다.
현재 보석까지의 최적 가치는 현재 보석을 넣는 경우와 넣지 않는 경우를 비교해 더 높은 것을 기록한다.
'''
