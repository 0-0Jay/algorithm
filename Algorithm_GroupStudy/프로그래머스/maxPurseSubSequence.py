# 프로그래머스 - 연속 펄스 부분 수열의 합 : https://school.programmers.co.kr/learn/courses/30/lessons/161988

def solution(sequence):
    purse1 = []
    purse2 = []
    p = -1
    for i in sequence:
        purse1.append(i * p)
        p *= -1
        purse2.append(i * p)
    dp = [[0, 0] for i in range(len(sequence))]
    dp[0] = [purse1[0], purse2[0]]
    tmp = max(dp[0])
    for i in range(1, len(sequence)):
        dp[i][0] = max(dp[i - 1][0] + purse1[i], purse1[i])
        dp[i][1] = max(dp[i - 1][1] + purse2[i], purse2[i])
        tmp = max(tmp, max(dp[i]))
    return tmp

# 알고리즘 : DP
'''
풀이 : 1로 시작하는 펄스 수열과 -1로 시작하는 펄스 수열을 곱한 두가지 배열을 만들고, 최대합 부분수열을 구한다.
먼저 두 가지 펄스 수열을 적용한 배열(purse1, purse2)을 만든다.
바텀업 다이나믹 프로그래밍을 통해 두 배열 각각 최대합 부분수열을 구한다.
현재 숫자가 지금까지의 최대합보다 크다면 현재 인덱스의 숫자로 교체하고, 그렇지 않다면 계속 최대합을 누적한다.
DP를 수행하면서 구해진 합과 tmp에 저장된 최대합과 비교하면서 tmp를 계속 갱신해준다.
'''
