# 백준 11438번 LCA2 : https://www.acmicpc.net/problem/11438

import math
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n = int(input())
logn = math.ceil(math.log2(n))
graph = [[] for _ in range(n + 1)]
for i in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

parent = [[0] * (n + 1) for _ in range(logn)]
depth = [0] * (n + 1)
chk = set()
chk.add(1)
def DFS(k, d):  # DFS로 깊이 기록
    depth[k] = d
    for nx in graph[k]:
        if nx not in chk:
            chk.add(nx)
            parent[0][nx] = k
            DFS(nx, d + 1)
DFS(1, 0)

for i in range(logn - 1):
    for j in range(1, n + 1):
        parent[i + 1][j] = parent[i][parent[i][j]]  # 공통 조상 기록(2의 제곱수 만큼 상위)
        
m = int(input())
for i in range(m):
    a, b = map(int, input().split())
    if depth[b] > depth[a]: a, b = b, a
    diff = depth[a] - depth[b]
    for j in range(logn):
        if diff & (1 << j):  # diff를 비트연산하여 해당하는 인덱스만큼 올릴 수 있다.
            a = parent[j][a]
            if depth[a] == depth[b]: break
    if a == b: print(a)
    else:
        for j in range(logn - 1, -1, -1):
            if parent[j][a] != parent[j][b]:
                a = parent[j][a]
                b = parent[j][b]
        print(parent[0][a])

# 알고리즘 : LCA(최소 공통 조상) 알고리즘 + 희소배열(DP)
'''
풀이 : DP로 공통 조상을 기록한 희소배열을 통해 LCA를 최적화한다.
부모를 찾을 때 N만큼 올라가는 방식의 LCA와 값의 저장과 초기값 설정은 동일하다.
입력이 끝나면, DFS로 찾은 부모 정보를 이용해 희소배열을 채워넣는다.

두 정점이 주어지면, 둘중 깊이가 더 깊은 정점을 다른 정점의 깊이까지 올린다.
올릴 때는 희소배열을 통해 건너뛰면서 올린다.
이 후, 최소 공통 조상을 찾을 때는 큰 범위부터 1씩 줄여가며 찾는다.
'''
