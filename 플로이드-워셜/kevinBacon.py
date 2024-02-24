# 백준 1389번 케빈 베이컨의 6단계 법칙 : https://www.acmicpc.net/problem/1389

from collections import defaultdict, deque
import math
import heapq as hq
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
INF = 1e9
bacon = [[1e9] * (n + 1) for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    bacon[a][b] = 1
    bacon[b][a] = 1

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j: bacon[i][j] = 0
            bacon[i][j] = min(bacon[i][j], bacon[i][k] + bacon[k][j])

kevin = INF
ans = 0
for i in range(1, n + 1):
    tmp = 0
    for j in range(1, n + 1):
        tmp += bacon[i][j] if bacon[i][j] < INF else 0
    if kevin > tmp:
        kevin = tmp
        ans = i
        
print(ans)

# 알고리즘 : 플로이드-워셜
'''
풀이 : 각 간선의 가중치를 1로 두고, 플로이드-워셜로 탐색한다.
결과 계산 과정에서 각 번호 별 케빈 베이컨의 수를 계산할 때, 만약 그 수가 INF라면 0으로 치환해줘야한다.
'''
