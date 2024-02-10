# 백준 14942번 개미 : https://www.acmicpc.net/problem/14942

from collections import defaultdict, deque
import heapq as hq
import math
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n = int(input())
graph = [[] for _ in range(n + 1)]
logn = math.ceil(math.log2(n))
parent = [[0] * (n + 1) for _ in range(logn)]
cost = [[0] * (n + 1) for _ in range(logn)]
ant = [0]
for i in range(n):
    ant.append(int(input()))
for i in range(n - 1):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

chk = set()
chk.add(1)
def DFS(k):
    for nx, val in graph[k]:
        if nx not in chk:
            chk.add(nx)
            parent[0][nx] = k
            cost[0][nx] = val
            DFS(nx)
DFS(1)       
for i in range(logn - 1):
    for j in range(1, n + 1):
        parent[i + 1][j] = parent[i][parent[i][j]]
        cost[i + 1][j] = cost[i][j] + cost[i][parent[i][j]]
        
for i in range(1, n + 1):
    id, fatigue = i, ant[i]
    for j in range(logn - 1, -1, -1):
        if fatigue >= cost[j][id] and parent[j][id] != 0:
            fatigue -= cost[j][id]
            id = parent[j][id]
        if id == 1: break
    print(id)

# 알고리즘 : 희소배열
'''
풀이 : 희소배열을 이용해 각 개미의 방으로 시작해 남은 에너지보다 작은 칸으로 한번에 건너뛰면서 계산한다.
부모노드에 대한 정보와 비용에 대한정보를 저장할 희소배열을 두개 만든다.
DFS를 돌면서 두 배열의 0번 인덱스에 초기 배열과 비용 정보를 저장한다.
초기값으로 부터 시작해 2중 for문을 사용해 2^i만큼 건너뛰었을 때의 정보를 기록한다.
이 후, 가장 큰 것부터 사용해 피로도를 빼가면서 더이상 이동할 수 없을때까지 이동한다.

희소 배열의 동작 과정을 예를 들어 설명하면 다음과 같다.
1 - 2 - 3 - 4 - 5 라는 개미굴이 있고
  5   9   7    2   라는 비용이 있다.
이를 이용해 희소배열을 만든다면, ceil(log2(5))의 길이 만큼 희소 배열을 만들어야 한다.
완성된 희소 배열은 다음과 같다.
0 0 1 2 3 4
0 0 0 1 2 3
0 0 0 0 0 1 <-1이 기록되어 있음
이 때, 5번 방의 개미가 1번 방까지 가려면, 희소배열에 따라 5 -> 1로 바로 건너 띌 수 있다.
비용을 기록한 희소배열을 표현하면 다음과 같다.
0 0 5   9  7  2
0 0 5 14 16  9
0 0 5 14 21 23 <- 같은 위치에 총 에너지가 기록
즉, 1번방까지 가려면 23의 에너지가 필요하다는 결과가 바로 도출된다.
'''
