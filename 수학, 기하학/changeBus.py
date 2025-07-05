# 백준 2536번 버스 갈아타기 : https://www.acmicpc.net/problem/2536

from collections import defaultdict, deque
import math
import heapq as hq
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
k = int(input())
bus = [list(map(int, input().split())) for _ in range(k)]
stx, sty, edx, edy = map(int, input().split())
que = deque()
chk = set()
fin_bus = set()
for i in range(k):
    num, a1, a2, b1, b2 = bus[i]
    if a1 > b1 : a1, b1 = b1, a1
    if a2 > b2 : a2, b2 = b2, a2
    if a1 <= stx <= b1 and a2 <= sty <= b2:
        chk.add(num)
        que.append((num, 1))
    if a1 <= edx <= b1 and a2 <= edy <= b2:
        fin_bus.add(num)

def CCW(a1, a2, b1, b2, c1, c2):
    return (a1 * b2 + b1 * c2 + c1 * a2) - (a2 * b1 + b2 * c1 + c2 * a1)

def intersect(a1, a2, b1, b2, c1, c2, d1, d2):
    l1 = CCW(a1, a2, b1, b2, c1, c2) * CCW(a1, a2, b1, b2, d1, d2)
    l2 = CCW(c1, c2, d1, d2, a1, a2) * CCW(c1, c2, d1, d2, b1, b2)
    
    if l1 == 0 and l2 == 0:
        if min(a1, b1) <= max(c1, d1) and min(c1, d1) <= max(a1, b1) and min(a2, b2) <= max(c2, d2) and min(c2, d2) <= max(a2, b2): return True
        else: return False
    elif l1 <= 0 and l2 <= 0: return True
    else: return False
    
graph = [[] for _ in range(k + 1)]
for i in range(k):
    for j in range(i + 1, k):
        a, a1, a2, b1, b2 = bus[i]
        b, c1, c2, d1, d2 = bus[j]
        if intersect(a1, a2, b1, b2, c1, c2, d1, d2):
            graph[a].append(b)
            graph[b].append(a)

while que:
    now, cnt = que.popleft()
    if now in fin_bus:
        print(cnt)
        break
    for nx in graph[now]:
        if nx not in chk:
            chk.add(nx)
            que.append((nx, cnt + 1))

# 알고리즘 : CCW + BFS
'''
풀이 : 입력받은 노선끼리 교차 여부를 판단하고, 교차가 발생하면 두 노선를 연결하여 graph에 기록한다.
입력단계에서 모든 노선에 대해 출발점과 도착점이 포함되어 있는지 검사한다.
출발점이 포함된 노선는 큐에 넣고, 도착점이 포함된 노선는 fin_bus에 기록해둔다.

모든 노선를 가지고 교차 여부를 검사한다.
교차가 발생한 두 노선은 각 노선을 정점, 교차점을 간선으로 취급하여 graph에 인접리스트로 기록한다.
이 후, 기록된 graph를 이용해 입력때 받은 출발 노선을 기준으로 BFS를 수행한다.
'''
