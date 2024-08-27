# 백준 2841번 외계인의 기타 연주 : https://www.acmicpc.net/problem/2841

import math
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n, p = map(int, input().split())
stk = [[] for i in range(n + 1)]
ans = 0
for i in range(n):
    a, b = map(int, input().split())
    while stk[a] and stk[a][-1] > b:
        ans += 1
        stk[a].pop()
    if not stk[a] or stk[a] and stk[a][-1] != b: 
        stk[a].append(b)
        ans += 1
print(ans)

# 알고리즘 : 스택
'''
풀이 : 각 인덱스별로 스택을 두어, 가장 큰 숫자와 현재 입력된 숫자를 비교한다.
a 줄의 b 프랫을 연주해야 한다면, stk[a]의 마지막 인덱스에 위치한 숫자와 b를 비교한다.
만약 b가 더 작다면, b가 가장 높은 숫자가 될때까지 손가락을 떼면서 ans에 카운팅하고, b를 stk[a]에 추가하면서 ans + 1 한다.
b가 더 크다면, 단순히 b를 연수하면서 ans + 1한다.
'''
