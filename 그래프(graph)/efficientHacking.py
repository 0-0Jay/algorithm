# 백준 1325번 효율적인 해킹 : https://www.acmicpc.net/problem/1325

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
tmp = [0]
max_cnt = 0

for i in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

for i in range(1, n + 1):
    que = deque()
    que.append(i)
    cnt = 0
    chk = [0] * (n + 1)
    chk[i] = 1
    
    while que:
        now = que.popleft()
        
        for nx in graph[now]:
            if chk[nx] == 0:
                chk[nx] = 1
                que.append(nx)
                cnt += 1
                
    tmp.append(cnt)
    if cnt > max_cnt: max_cnt = cnt
    
for i in range(len(tmp)):
    if max_cnt == tmp[i]:
        print(i, end = " ")

# 알고리즘 : BFS
'''
풀이 : 각 컴퓨터를 시작점으로 BFS를 한번씩 수행하여 가장 많은 컴퓨터와 연결된 pc를 출력한다.
단순 BFS 완전 탐색 문제다.
'''
