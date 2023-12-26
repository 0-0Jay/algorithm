# 프로그래머스 등굣길 : https://school.programmers.co.kr/learn/courses/30/lessons/42898

def solution(m, n, puddles):
    answer = 0
    arr = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    
    for i in range(len(puddles)):
        arr[puddles[i][1]][puddles[i][0]] = -1
    arr[1][1] = 1
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if arr[i][j] == -1: continue
            if i - 1 > 0 and arr[i - 1][j] > 0 : arr[i][j] = (arr[i][j] + arr[i - 1][j]) % 1000000007
            if j - 1 > 0 and arr[i][j - 1] > 0 : arr[i][j] = (arr[i][j] + arr[i][j - 1]) % 1000000007
            
    return arr[n][m] % 1000000007

# 알고리즘 : DP
'''
풀이 : 시작점을 1로 두고, 현재칸을 왼칸과 윗칸의 값을 합산하며 학교 좌표까지 이동한다.
웅덩이 좌표는 -1로 저장해둔다.
반복문을 돌면서 -1이 나오면 그 칸을 continue로 스킵하고, 계산 과정에서도 0보다 값이 클 때만 합산한다.
'''
