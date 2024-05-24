# 프로그래머스 Summer/Winder Coding(~2018) - 스티커 모으기(2) : https://school.programmers.co.kr/learn/courses/30/lessons/12971#

def solution(sticker):
    answer = sticker[0]
    dp = [[0, 0] for i in sticker]
    dp2 = [[0, 0] for i in sticker]
    dp[0][1] = sticker[0]
    if len(sticker) > 1: dp2[1][1] = sticker[1]

    for i in range(2,len(sticker)):
        if i < len(sticker) - 1:  # 0번 인덱스 선택한 경우
            dp[i][1] = max(dp[i - 1][0], dp[i - 2][1]) + sticker[i]
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1], dp[i - 2][0], dp[i - 2][1]) 
            answer = max(answer, max(dp[i]))
        # 1번 인덱스 선택한 경우
        dp2[i][1] = max(dp2[i - 1][0], dp2[i - 2][1]) + sticker[i]
        dp2[i][0] = max(dp2[i - 1][0], dp2[i - 1][1], dp2[i - 2][0], dp2[i - 2][1]) 
        answer = max(answer, max(dp2[i]))

    return answer

# 알고리즘 : DP
'''
풀이 : 0번 인덱스를 고르는 경우와 1번 인덱스를 고르는 경우를 따로 계산한다.
0번 인덱스를 고르는 경우라면, 마지막 인덱스의 수를 고를 수 없기 때문에 i가 마지막 인덱스인 경우는 계산하면 안된다.
반면, 1번 인덱스를 고르는 경우라면, 마지막 인덱스의 수를 골라도 무관하므로 그대로 계산한다.
이를 위해 dp 배열을 2개 만들어 활용한다.

dp 계산 과정은 현재 인덱스의 숫자를 고르는 경우와 안고르는 경우를 나누어 계산한다.
1. 현재 인덱스 수를 고르는 경우, 이전 인덱스를 고를 수 없기 때문에 다음 두 가지 중 더 큰 값을 가져온다.
-> 이전 인덱스의 수를 고르지 않는 경우
-> -2 인덱스의 수를 고른 경우
2. 현재 인덱스 수를 고르지 않는 경우, 이전까지 존재했던 모든 수 중 큰 값을 가져온다.
-> 이 때, dp 성질에 따라 -2인덱스보다 더 작은 인덱스는 볼 필요가 없다. 무조건 그 이전의 값을 고르고 넘어온 것이 더 크다.
'''
