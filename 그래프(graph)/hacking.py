# 백준 28283번 해킹 : https://www.acmicpc.net/problem/28283

from collections import deque
import sys
input = sys.stdin.readline

n, m, x, y = map(int, input().split())
money = [0] + list(map(int, input().split()))
com = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int,input().split())
    com[a].append(b)
    com[b].append(a)
protect = list(map(int, input().split()))

chk = [-1] * n

que = deque()
for i in protect:
    chk[i - 1] = 0
    que.append((i, 1))

while que:
    now, cnt = que.popleft()
    
    for j in com[now]:
        if chk[j - 1] == -1:
            que.append((j, cnt + 1))
            chk[j - 1] = money[j] * cnt
            
for i in range(1, n + 1):  # 보안 프로그램이 설치되지 않았어도 얻을 수 있는 돈이 0원이면 무한대가 아님
    if money[i] == 0:
        chk[i - 1] = 0
    
chk.sort()
if chk[0] == -1: print(-1)
else:
    sum = 0
    for i in range(1,x+1):
        sum += chk[-i]
        
    print(sum)

# 알고리즘 : BFS + 그리디
'''
풀이 : BFS를 수행하며 각 컴퓨터에 방문 체크를 (깊이 * 컴퓨터의 돈)으로 하고, 가장 많은 금액의 컴퓨터 X개를 뽑는다.
que에 초기값으로 백신프로그램이 초기에 설치되는 컴퓨터 y개를 넣는다.
cnt로 깊이를 체크하면서 BFS를 수행하면 각 컴퓨터에 방문한 시점의 cnt가 곧 돈을 얻을 수 있는 시간이 된다.
따라서 cnt와 해당 컴퓨터에서 얻을 수 있는 돈을 곱한 값이 해당 컴퓨터에서 최대한 얻을 수 있는 돈이다.
chk에 이 계산 값을 저장해두고, 오름차순 정렬 후, x개만큼 끝에서 뽑아 sum에 합산한다.

만약 정렬 후에 chk에 -1이 존재하면 방문한적이 없는 곳이라는 뜻으로, 무한대로 돈을 얻을 수 있는 컴퓨터라는 의미다.
그러나, 방문한 적이 없는 컴퓨터라 해도 해당 컴퓨터에서 얻을 수 있는 돈이 0원이라면 
무한대로 시간이 주어져도 돈을 얻을 수 없으므로 chk를 임의로 0으로 변경시켜 주었다.
'''
