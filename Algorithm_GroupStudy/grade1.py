# 백준 5557번 1학년 : https://www.acmicpc.net/problem/5557

import sys
from collections import deque

n = int(input())

lst = list(map(int,input().split()))
dp = [[0 for _ in range(n)] for _ in range(1000)]

dp[lst[0]][0] = 1

def td(num, id):
    if num < 0 or num > 20 or id < 0: return 0
    if dp[num][id] > 0: return dp[num][id]
    dp[num][id] = td(num - lst[id], id - 1) + td(num + lst[id], id - 1)
    return dp[num][id]
    
print(td(lst[-1], len(lst) - 2))

# 알고리즘 : DP
'''
풀이 : 마지막 숫자는 (마지막숫자 + 이전숫자)의 경우와 (마지막 숫자 - 이전숫자)의 경우의 합과 같다.
예를 들어 다음과 같은 경우,
8 3 2 4 8 7 2 4 0 8 = 8
8은 16에서 -8을 하는 경우(16을 만들 수 있는 경우의 수)와 0에서 +8을 하는경우(0을 만들 수 있는 경우의 수)의 합이다.
그러나 중간계산 과정에서 같은 숫자가 발생할 경우 DP계산에서 오류가 발생한다.
따라서 2차원 배열을 두고, 매 탐색마다 인덱스를 옮겨가며 현재 탐색에서 나오는 숫자를 이전 탐색들의 숫자와 분리시켰다.
'''
