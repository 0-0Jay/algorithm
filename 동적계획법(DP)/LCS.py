# 백준 9251번 - LCS : https://www.acmicpc.net/problem/9251

a = list(input().strip())
b = list(input().strip())

DP = [[0 for _ in range(len(b) + 1)] for _ in range(len(a) + 1)]

for i in range(1, len(a) + 1):
    for j in range(1, len(b) + 1):
        if a[i - 1] == b[j - 1]:
            DP[i][j] = DP[i - 1][j - 1] + 1
        else:
            DP[i][j] = DP[i - 1][j] if DP[i - 1][j] >= DP[i][j - 1] else DP[i][j - 1]
            
print(DP[-1][-1])

# 알고리즘 : DP - (LCS : 최장 공통 부분 수열 알고리즘)
'''
풀이 : 두 문자열을 각각 행, 열로 두고 한 글자씩 비교하며 겹치는 글자가 나올때마다 이전 값에 + 1해준다.
각 문자열에서 한 글자씩 뽑는다.
만약 두 글자가 같으면 두 문자열에서 각 글자의 이전까지의 최장 공통 부분 수열의 길이에 + 1한다.
두 글자가 다르면 두 문자열에서 각 글자의 이전까지의 최장 공통 부분 수열의 길이를 비교한다.
둘 중 더 긴 길이를 가져온다.
두 문자열의 각 마지막 글자까지 탐색했을때, 마지막 칸(DP[-1][-1])에 저장된 길이가 곧 최장 공통 부분 수열의 길이다. 
'''
