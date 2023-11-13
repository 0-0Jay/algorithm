# 백준 16928번 뱀과 사다리 게임 : https://www.acmicpc.net/problem/16928

from collections import deque
import sys

n, m = map(int, input().split())
arr = [0] * 101
chk = [100] * 101

for i in range(n + m):
    a, b = map(int, input().split())
    arr[a] = b
    
que = deque()
que.append(1)
chk[1] = 0

while que:
    now = que.popleft()
    
    for i in range(1, 7):
        if now + i <= 100:
            if arr[now + i] == 0:
                if chk[now + i] > chk[now] + 1 or chk[now + i] == 100:
                    que.append(now + i)
                    chk[now + i] = chk[now] + 1
                    if now + i == 100: break
            else:
                if chk[arr[now + i]] > chk[now] + 1  or chk[arr[now + i]] == 100:
                    que.append(arr[now + i])
                    chk[arr[now + i]] = chk[now] + 1
    
print(chk[100])

# 알고리즘 : BFS
'''
풀이 : 주사위 1~6이 나온 경우를 BFS로 돌되, 더 적은 경우로 해당 칸에 도착했을 때만 que에 넣는다.
해당 칸에 더 적은 횟수로 도착할 수 있다면, 그 이상의 경우는 더이상 탐색할 필요가 없다.
한 번이라도 100에 도착했다면, BFS의 특성상 가장 먼저 도착한 경우가 가장 적은 횟수기 때문에 탐색을 중단한다.
'''
