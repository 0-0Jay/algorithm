# 백준 2623번 음악프로그램 : https://www.acmicpc.net/problem/2623

from collections import deque
import heapq as hq
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
que = deque()
res = []

for i in range(m):
    pd = list(map(int, input().split()))
    for j in range(1, pd[0]):
        graph[pd[j]].append(pd[j + 1])
        arr[pd[j + 1]] += 1
        
for i in range(1, n + 1):
    if arr[i] == 0:
        que.append(i)
        
while que:
    now = que.popleft()
    res.append(now)
    n -= 1
    
    for singer in graph[now]:
        arr[singer] -= 1
        if arr[singer] == 0:
            que.append(singer)
            
if n > 0:
    print(0)
else:
    for i in res:
        print(i, end="\n")

# 알고리즘 : 위상 정렬
'''
풀이 : 각 PD의 출연순서를 graph로 연결시키면서 해당 가수전에 출연할 가수의 수를 arr에 체크한다.
2차원 배열 graph에 다음에 출연해야 하는 가수를 append 한다.
그 후, arr배열의 다음에 출연해야 하는 가수의 인덱스에 +1 해서 먼저 출연할 가수가 존재함을 기록한다.

arr 배열을 돌면서 먼저 출연할 가수가 0명인 가수들을 큐에 넣는다.
큐에서 가수를 꺼내면서 res에 넣고, 해당 가수 다음에 출연할 가수들의 arr 카운트를 하나씩 뺀다.
만약 arr카운트가 0이된 가수가 있으면 먼저 출연할 가수들이 모두 출연했다는 의미이므로 큐에 넣는다.

모든 탐색이 끝났을 때, 어떤 이유든 arr에 0이 아닌 숫자가 남아있다는 것은 순서를 정할 수 없는 부분이 발생했다는 의미이므로 0을 출력한다.
'''
