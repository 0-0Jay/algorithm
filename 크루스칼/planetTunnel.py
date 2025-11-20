# 백준 2887번 행성 터널 : https://www.acmicpc.net/problem/2887

from collections import defaultdict, deque
from functools import cmp_to_key
import heapq as hq
import math
import sys
input = sys.stdin.readline

def union(parent, a, b, c):
    global sum
    rootA = find(parent, a)
    rootB = find(parent, b)
    if rootA != rootB:
        parent[rootB] = rootA
        sum += c

def find(parent, x):
    if parent[x] == x:
        return x
    parent[x] = find(parent, parent[x])
    return parent[x]

n = int(input())
planet = [[] for _ in range(3)]
parent = [i for i in range(n)]
graph = []
for i in range(n):
    a, b, c = map(int, input().split())
    planet[0].append((a, i))
    planet[1].append((b, i))
    planet[2].append((c, i))
for i in range(3):
    planet[i].sort()
for i in range(1, n):
    for j in range(3):
        a_num, a_point = planet[j][i - 1]
        b_num, b_point = planet[j][i]
        graph.append((abs(a_num - b_num), a_point, b_point))
graph.sort()
    
sum = 0
for c, a, b in graph:
    union(parent, a, b ,c)   
print(sum)

# 알고리즘 : 크루스칼 알고리즘 + 그리디
'''
풀이 : min(|xA-xB|, |yA-yB|, |zA-zB|)가 비용이므로 좌표별로 따로 계산해 최소 신장 트리를 구성한다.
각 x좌표의 차, y좌표의 차, z 좌표의 차 중 가장 작은 것이 비용이기 때문에 각 x, y, z 좌표를 각각 배열에 저장한다.
모든 좌표를 기록했다면 각 좌표별로 정렬한다.
이러면 모든 행성에 대한 모든 간선을 탐색하지 않고, 각 x, y, z별 가장 가까운 행성과 연결된 간선만 탐색할 수 있다.
이 방식을 통해 100000개의 행성에 대한 최소비용루트를 간선을 300000개만 사용해서 해결할 수 있다.

문제의 예제를 예를들면 다음과 같다.
1. [11  14  -1  10  19] 를 정렬한다.
2. [-1  10  11  14  19] 에서 각 인덱스 바로 옆 인덱스와의 거리를 구한다. -> ((10 - -1), 0, 1)
3. 이를 간선정보 배열graph에 넣는다
4. 1 ~ 3 과정을 y, z좌표에 대한 값에도 수행한다.

모든 간선을 넣었다면, graph를 간선 비용을 기준으로 오름차순 정렬하고 union/find로 연결한다.
이때, 연결되었다면 sum에 그 비용을 누적한다.
'''
