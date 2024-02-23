# 백준 1562번 계단 수 : https://www.acmicpc.net/problem/1562

import sys
input = sys.stdin.readline

n = int(input())
arr = [[[0] * (1 << 10) for _ in range(10)] for _ in range(n + 1)]
div = 1000000000

for i in range(1, 10):
    arr[1][i][1 << i] = 1

for i in range(1, n):
    for j in range(10):
        for k in range(1 << 10):
            if j > 0:
                tmp = k | (1 << (j - 1))
                arr[i + 1][j - 1][tmp] += arr[i][j][k]
                arr[i + 1][j - 1][tmp] %= div
            if j < 9:
                tmp = k | (1 << (j + 1))
                arr[i + 1][j + 1][tmp] += arr[i][j][k]
                arr[i + 1][j + 1][tmp] %= div
                
ans = 0
for i in range(10):
    ans += arr[n][i][(1 << 10) - 1]
    ans %= div
print(ans)

# 알고리즘 : 비트마스킹 + DP
'''
풀이 : 사용한 숫자를 비트마스킹하고, 그 결과 값을 인덱스로 하여 DP 배열에 저장한다.
먼저, 0을 제외한 각 숫자 1개씩을 사용한 경우를 1번 행에 1씩 기록한다.

이 후, DP 계산 과정은 다음과 같다.
1. i번 행을 선택한다.
2. i+1번 행에서 현재 수가 j라면, j-1과 j+1에 현재 값을 더한다.
3. 이 때, 사용한 숫자 종류(비트마스킹한 결과)가 같은 칸에 저장한다. 이를 위해 3차원 배열을 사용한다.
  3-1. 예를 들어 345와 545는 모두 같은 길이고 5로 끝나지만, 사용한 숫자가 다르므로 연산을 따로 해주어야 한다.
위 1~3 과정을 n자리 까지 반복한다.

모든 DP 계산이 끝났다면 n행에 0~9열의 (1111111111) 인덱스에 기록된 모든 숫자의 합을 출력한다.
'''
