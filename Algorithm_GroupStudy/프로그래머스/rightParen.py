# 프로그래머스 - 올바른 괄호의 갯수 : https://school.programmers.co.kr/learn/courses/30/lessons/12929

def solution(n):
    dp = [0] * (n + 1)
    dp[0], dp[1] = 1, 1
    for i in range(2, n + 1):
        for j in range(i):
            dp[i] += dp[j] * dp[i - 1 - j]
    return dp[n]

# 알고리즘 : DP(카탈란 수열)
'''
풀이 : 이미 구한 괄호쌍 개수에 대한 괄호문자열 수를 활용해 다음 괄호쌍을 계산한다.
가장 먼저 dp 배열에 초기값을 설정한다.
굳이 계산을 하지않아도 괄호쌍이 없는 경우(dp[0])은 빈괄호 문자열 '' 1개이다.
괄호쌍 1개의 경우, 가능한 괄호문자열은 '()' 1개이다.

두 개의 괄호쌍부터, 계산하면 다음과 같은 과정을 거친다.
1. n개의 괄호쌍의 경우, (n - i)개의 괄호쌍과 i개의 괄호쌍을 합친 괄호문자열을 조합한다.
2. 1번에 해당하는 모든 괄호문자열 조합에서 중복되는 조합을 제거한다.
위 계산 과정을 정리하면 카탈란 수열이 생성된다.
카탈란 수열의 일반항은 C(i) * C(n - 1 - i)이므로 이를 dp배열에 그대로 적용한다.
'''
