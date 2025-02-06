# 프로그래머스 - 땅따먹기 : https://school.programmers.co.kr/learn/courses/30/lessons/12913

def solution(land):
    dp = [[0 for _ in range(4)] for _ in range(len(land))]
    dp[0] = [i for i in land[0]]

    for i in range(1, len(land)):
        for j in range(4):
            tmp = 0
            for k in range(4):
                if k == j: continue
                tmp = max(tmp, dp[i - 1][k])
            dp[i][j] = tmp + land[i][j]

    return max(dp[-1])

# 알고리즘 : DP
'''
풀이 : DP 배열을 활용해 이전 행에서 다른 열들에 누적된 값들 중 가장 큰 값을 가져와 현재 행에 더한다.
dp 배열을 하나 만들고, 0번 행에 land의 0번 행을 가져온다.
마지막 행까지 다음 과정을 반복한다.
1. i행 j열칸을 선택한다.
2. i - 1행에서 j열을 제외한 나머지 열의 값들중 최대값을 구한다.
3. dp[i][j]에 2번에서 구한 최대값과 land[i][j]의 값을 더한 값을 저장한다.
4. 2~3 과정을 모든 열에 반복한다.
마지막 행까지 탐색했다면, 마지막 행의 최대값을 리턴한다.
'''
