# 백준 1613번 역사 : https://www.acmicpc.net/problem/1613

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
hist = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(k):
    a, b = map(int, input().split())
    hist[a][b] = -1
    hist[b][a] = 1

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if hist[i][j] == 0 and hist[i][k] == -1 and hist[k][j] == -1:
                hist[i][j] = -1
                hist[j][i] = 1

s = int(input())
for _ in range(s):
    a, b = map(int, input().split())
    print(hist[a][b])

# 알고리즘 : 플로이드-워셜
'''
풀이 : a가 b보다 먼저 일어났으면 -1, 나중에 일어났으면 1을 가중치로 저장한다.
i사건과 j사건 중 무엇이 우선인지 아직 계산되지 않았을 때, i -> k -> j의 정보가 있다면, i -> j가 된다.
s개의 결과를 출력할 때, hist[a][b]를 바로 출력하면 된다.
'''
