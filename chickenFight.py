# 백준 1765번 닭싸움 팀 정하기 : https://www.acmicpc.net/problem/1765

import sys
input = sys.stdin.readline

def union(parent, a, b):
    rootA = find(parent, a)
    rootB = find(parent, b)
    if rootA != rootB:
        parent[rootB] = rootA
        
def find(parent, x):
    if parent[x] == x:
        return x
    parent[x] = find(parent, parent[x])
    return parent[x]

n = int(input())
m = int(input())
graph = []
hate = [[] for _ in range(n + 1)]
parent = [i for i in range(n + 1)]
for i in range(m):
    c, a, b = input().strip().split(" ")
    a, b = int(a), int(b)
    if c == "F":  # 친구면 간선에 추가
        graph.append((a, b))
    else:  # 원수면 원수 정보로 기록
        hate[a].append(b)
        hate[b].append(a)
        
for i in range(1, n + 1):  # i를 선택
    for j in hate[i]:  # i와 원수인 사람 j선택
        for k in hate[j]:  # j와 원수인 사람 k 선택
            graph.append((i, k))  # i와 k는 원수의 원수이므로 친구
            
for a, b in graph:
    if find(parent, a) != find(parent, b):
        union(parent, a, b)

team = set()
for i in range(1, n + 1):
    if find(parent, i) not in team:
        team.add(parent[i])
print(len(team))

# 알고리즘 : union/find
'''
풀이 : 친구인 조건에 맞는 간선을 모두 구한 후, union/find를 수행한다.
입력 단계에서 친구면 간선정보에 바로 추가하고, 원수면 hate에 원수관계를 인접리스트로 저장해둔다.
3중 for문으로 원수의 원수관계를 찾아 모두 간선으로 추가해준다.
간선정보를 union/find로 순회하며 친구관계인 사람들을 그룹화해준다.
parent 배열을 탐색하며 다른 그룹이 생길때마다 team에 추가하면 team의 길이가 곧 최대 팀 개수가 된다.
'''
