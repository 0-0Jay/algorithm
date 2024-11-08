# 프로그래머스 - 가장 긴 팰린드롬 : https://school.programmers.co.kr/learn/courses/30/lessons/12904#

def solution(s):
    answer = 1
    dp = [[0 for i in range(len(s))] for j in range(len(s))]
    for i in range(len(s)):
        dp[i][i] = 1
        if i + 1 < len(s) and s[i] == s[i + 1]:
            answer = 2
            dp[i][i + 1] = 1
        
    for i in range(2, len(s)):
        for j in range(len(s)):
            if j + i == len(s): break
            if s[j] == s[j + i]: dp[j][j + i] = dp[j + 1][j + i - 1]
            if dp[j][j + i] == 1:
                answer = max(answer, i + 1)
                
    return answer

# 알고리즘 : DP
'''
풀이 : 문자열에서 a번째 글자와 b번째 글자가 같다면, a + 1번째부터 b - 1번까지가 팰린드롬인지 검사한다.
s의 최소 길이가 1이기 때문에 answer의 초기값을 1로 둔다.
2차원으로 DP 배열을 만든다. 이 때, dp[i][j]는 문자열 s의 i번째 글자부터 j번째 글자까지가 팰린드롬인지 여부를 저장한다.
따라서 부분문자열의 길이가 1인 경우는 무조건 팰린드롬이므로 dp[i][i]의 초기값은 1로 둔다.
추가로 부분문자열의 길이가 2인 경우, s[i]와 s[i + 1]이 같으면 팰린드롬이므로 1로 기록해둔다. 

다음은 2중 반복문을 통해 DP를 채우는데, 일반적인 반복문처럼 굴리면 제대로 체크되지 않는다.
재귀를 사용하는 방법도 좋지만, 위 코드는 반복문을 조금 응용했다.
i는 현재 인덱스부터 몇 글자 뒤인지를 뜻하고, j는 현재 인덱스를 뜻한다.
즉, j + i가 s의 길이보다 크다면, break로 빠져나오는 방식으로 탐색하기 때문에  dp배열의 좌측상단부터 우측하단까지 대각선으로 탐색하게 된다.

j번째 글자부터 j + i번째 글자까지의 부분 문자열이 팰린드롬이려면 다음 두가지 조건을 만족해야 한다.
1. j번째 글자가 j + i번째 글자와 같다.
2. j + 1번째 글자부터 j + i - 1번째 글자까지가 이미 팰린드롬이다.
1번이 만족했을 경우, 2번 조건에 따라 dp[j + 1][j + i - 1]이 1이라면 dp[j][j + i]를 1로 둔다.
dp[j][j + i]가 1이라면, i + 1을 answer와 비교해서 최대값을 갱신해준다.
'''
