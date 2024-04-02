# 백준 13904번 과제 : https://www.acmicpc.net/problem/13904

import sys
input = sys.stdin.readline

n = int(input())
que = [0]
def up(k):
    global que
    if k // 2 == 0: return
    if que[k][0] > que[k // 2][0] or (que[k][0] == que[k // 2][0] and que[k][1] > que[k // 2][1]): 
        que[k], que[k // 2] = que[k // 2], que[k]
        up(k // 2)
    
def down(k):
    global que
    nx = k * 2
    if nx >= len(que): return
    if nx + 1 < len(que) and (que[nx][0] < que[nx + 1][0] or que[nx][0] == que[nx + 1][0] and que[nx][1] < que[nx + 1][1]):
        nx += 1
    if que[k][0] < que[nx][0] or que[k][0] == que[nx][0] and que[nx][1] > que[k][1]:
        que[k], que[nx] = que[nx], que[k]
        down(nx)
        
for _ in range(n):
    tmp = tuple(map(int, input().split()))
    que.append(tmp)
    up(len(que) - 1)

score = 0
for i in range(n, 0, -1):
    if que[1][0] < i: continue
    else:
        while que[1][0] > i:
            tmp = que[1]
            que[1] = que[-1]
            que.pop()
            down(1)
            que.append((i, tmp[1]))
            up(len(que) - 1)
        score += que[1][1]
        que[1] = que[-1]
        que.pop()
        down(1)
        
print(score)
        
# 알고리즘 : 그리디 + 우선순위 큐
'''
풀이 : 우선순위 큐를 이용해 마감일자가 나중인 것 중 가장 높은 점수인 과제를 순차적으로 뽑는다.
우선순위 큐의 힙 교체 조건은 다음과 같다.
1. 두 요소 중 마감일이 더 나중인 과제를 위로 올린다.
2. 마감일이 같다면, 더 높은 점수인 과제를 위로 올린다.

위 조건으로 우선순위 큐를 구현한 후, n일차부터 역순으로 뽑는다.
그러나 위 조건으로 구현하게 되면, (4, 10) 과 (3, 30)의 경우 마감일자가 3인 것이 4인것보다 우선순위가 밀리게 된다.
이 경우, 3일 차에서 (4, 10)이 (3, 30)보다 먼저 뽑히게 되어 더 좋은 점수를 받을 과제가 밀리게 된다.
이를 방지하기 위해 먼저 우선순위 큐를 top에서부터 순차적으로 탐색하여 더 큰 날짜일 경우 현재날짜로 바꾸어준다.
이러면 자연스럽게 모두 동일한 n일차로 보고 점수를 비교하므로 해당 날짜의 최대 점수를 뽑을 수 있다. 
'''
