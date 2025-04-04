# 백준 14517번 팰린드롬 개수 구하기 (Large) : https://www.acmicpc.net/problem/14517

import sys
input = sys.stdin.readline

s = input().strip()
dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
for i in range(len(s)):
    dp[i][i] = 1
    if i + 1 < len(s):
        dp[i][i + 1] = 2
        if s[i] == s[i + 1]: dp[i][i + 1] += 1
    
for i in range(2, len(s)):
    for j in range(len(s)):
        if j + i == len(s): break
        if s[j] != s[j + i]: dp[j][j + i] = (dp[j][j + i - 1] + dp[j + 1][j + i] - dp[j + 1][j + i - 1]) % 10007
        else: dp[j][j + i] = (dp[j][j + i - 1] + dp[j + 1][j + i] + 1) % 10007
        
print(dp[0][len(s) - 1] % 10007)

# 알고리즘 : DP + 포함 배제의 원리
'''
풀이 : DP를 이용해 각 범위에 따른 팰린드롬 개수를 포함 배제의 원리로 계산하며 누적시킨다.
전체적인 틀은 부분문자열 팰린드롬 검사 알고리즘과 유사하다.
처음 초기값을 줄 때는 다음과 같다.
1. 1글자의 경우, 팰린드롬은 자기자신밖에 없기때문에 dp[i][i]는 1로 고정한다.
2. 2글자의 경우도 역시 1글자 + 1글자로 2로 고정한다. 단, 2개의 문자가 서로 같은 경우, 2글자 자체로 팰린드롬이니 +1 해준다.

초기값 입력이 끝났으면 DP 배열을 우측 상단으로 대각선 방향으로 채운다.
점화식은 현재칸이 x, y일 때, x + 1 칸과 y - 1칸의 값을 더하고, x+1, y-1칸의 값을 빼주는 것이다.
예를 들어서 5글자 문자열에서 1~4번 인덱스 까지의 부분문자열에 대한 팰린드롬 갯수는 다음과같다.
1~4의 부분문자열의 팰린드롬 수 = 1~3의 팰린드롬 수 + 2~4의 팰린드롬 수 - 2~3의 팰린드롬 수
위 과정이 포함 배제의 원리이며, 이를 2차원 DP배열에서 보면 방금 언급한 점화식을 구할 수 있다.

이 때, 모듈러 연산에서 음수 연산이 발생할 수 있기 때문에 항상 점화식의 덧셈, 뺄셈을 모두 계산하고 모듈러 연산을 수행한다.
최종적으로 DP[0][문자열 마지막 인덱스]를 반환하면 전체 문자열에 포함된 팰린드롬 수를 구할 수 있다.
'''
        
