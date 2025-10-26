# 백준 1509번 팰린드롬 분할 : https://www.acmicpc.net/problem/1509

from collections import deque
import heapq as hq
import sys
input = sys.stdin.readline

arr = [0] + list(input().strip())
n = len(arr)
DP = [[0 for _ in range(n)] for _ in range(n)]
cnt = [0, 1] * n

for i in range(1, n):  # DP 초기값 설정
    DP[i][i] = 1  # 길이가 1
    if i < n - 1 and arr[i] == arr[i + 1]:  # 길이가 2
        DP[i][i + 1] = 1
        
for k in range(3, n):  # 부분 문자열 중 팰린드롬 판별 DP
    i = 1
    for j in range(k, n):
        if arr[i] == arr[j]: DP[i][j] = DP[i + 1][j - 1]
        else: DP[i][j] = 0
        i += 1
        
for i in range(1, n):  # 최소 팰린드롬 분할 계산 DP
    cnt[i] = i
    for j in range(1, i + 1):
        if DP[j][i] == 1:
            cnt[i] = min(cnt[j - 1] + 1, cnt[i])
            
print(cnt[n - 1])

# 알고리즘 : DP
'''
풀이 : 팰린드롬을 판별하는 DP배열과 최소 팰린드롬 분할을 계산할 DP 배열 두개를 활용한다.

팰린드롬 판별 DP는 다음과 같다.
1. 1자리의 경우는 무조건 팰림드롬이니 1이고, 2자리는 두 문자가 같으면 팰린드롬이니 1, 다르면 0이다.
2. 3자리 부터는 양 끝의 문자가 같을때, 양 끝을 한자리씩 줄였을 때가 팰린드롬이면 현재 문자열도 팰린드롬이다.
  2-1. 인덱스 i ~ j의 부분문자열이 팰린드롬이려면 인덱스 (i + 1) ~ (j - 1)의 부분문자열이 팰린드롬이어야 한다.
3. 그 외의 경우는 팰린드롬이 아니므로 0으로 체크한다.

최소 팰린드롬 분할 계산과정은 다음과 같다.
1. 현재 자릿수(i)를 초기값으로 한다. (cnt[i] = i)
  1-1. 현재 자릿수까지의 부분문자열을 전부 한자리씩 분할한 갯수가 가능한 최대 분할 개수다.
2. DP의 i열의 행(j)을 탐색하면서 만약 DP[i][j]가 1이라면 cnt[i]의 값과 cnt[j]의 값을 비교하여 최소값으로 교체한다.
  2-1. 예를 들어 5번째 문자까지의 부분문자열 중, 3번째에서 팰린드롬이 발생했다면, 3번째까지를 팰린드롬 분할 1개로 두는 것이 더 적은 분할을 만들 수 있다.
    ex)  a b a d e -> 5개의 분할
         aba d e -> 3개의 분할
  2-2.  이 방식으로 이전에 발생한 모든 팰린드롬 분할 위치를 탐색해 최소 분할 수를 가져온다.
3. 만약 이전 부분문자열에서 팰린드롬이 한 번도 발생하지 않았다면 모두 한자리씩 분할하는 방법 뿐이다.

최종적으로 cnt에서 마지막 문자열 위치의 값을 출력한다.
'''
