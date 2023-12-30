# 백준 1414번 불우이웃돕기 : https://www.acmicpc.net/problem/1414

from collections import defaultdict, deque
from functools import cmp_to_key
import heapq as hq
import math
import sys
input = sys.stdin.readline

n = int(input())
lst = []
res = 0
for i in range(n):
    tmp = list(input().strip())
    for j in range(n):
        if tmp[j] =='0': continue
        cost = ord(tmp[j]) - ord('a') + 1 if 'a' <= tmp[j] <= 'z' else ord(tmp[j]) - ord('A') + 27
        res += cost
        if i != j : lst.append([i, j, cost])
lst.sort(key=lambda x: x[2])  # 문자열 정렬되지 않게 정수 비용으로 전환하여 삽입 및 정렬
parent = [i for i in range(n)]

def union(parent, a, b):
    rootA = find(parent, a)
    rootB = find(parent, b)
    
    if rootA < rootB:
        parent[rootB] = rootA
    else:
        parent[rootA] = rootB
    
def find(parent, a):
    if parent[a] == a:
        return a
    parent[a] = find(parent, parent[a])
    return parent[a]

for i in lst:
    if i[0] == i[1]: continue
    if find(parent, i[0]) != find(parent, i[1]):
        union(parent, i[0], i[1])
        res -= i[2]
        
for i in range(n):  # 루트 노드 최종 정리
    find(parent, i)
    
if len(set(parent)) > 1: res = -1

print(res)

# 알고리즘 : 크루스칼 알고리즘
'''
풀이 : union/find를 통해 최소 신장 트리를 만들어 사용한 최소 길이를 구한 후, 전체 길이에서 빼준다.
처음 2차원 값을 연결받을 때, 이를 1차원으로 정제한다.
만약 자기 자신과 연결된 노드가 있다면, 그 노드의 값은 전체 길이에 포함시키되, 리스트(lst)에는 넣지 않는다.
사용할 최소 길이를 구하기 위해 가장 짧은 길이의 선부터 연결해야 하므로 lst를 길이 기준으로 오름차순 정렬한다.
이 때, 문자열 정렬을 그대로 정렬하면 문자열 정렬 규칙으로 정렬되기 때문에 정수값으로 치환하여 정렬한다.

union/find를 통해 모든 간선을 연결하면 사용한 최소 길이가 구해진다.
이 값을 전체 길이에서 뺀 나머지가 기부할 수 있는 최대 길이다.

단, 모든 컴퓨터가 연결되어 있지 않으면 -1을 출력해야 한다.
이는 모든 컴퓨터의 루트 컴퓨터가 동일하지 않으면 -1을 출력하라는 말과 같다.
그러나 union/find 통해 모든 간선이 연결했더라도, 연결 순서에 따라 가르키고 있는 부모 컴퓨터가 다를 수 있다.
따라서 모든 탐색이 끝난 후, find를 전체 컴퓨터에 한 번 더 수행하여 모든 부모를 루트로 모아준다.
'''
