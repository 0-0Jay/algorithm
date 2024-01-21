백준 1043번 거짓말 : https://www.acmicpc.net/problem/1043

from collections import defaultdict, deque
import heapq as hq
import math
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
k = list(map(int, input().split()))
truth = set(k[1:])
party = []
for i in range(m):
    tmp = list(map(int, input().split()))
    party.append(tmp[1:])
    
parent = [i for i in range(n + 1)]
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

for i in range(m):
    for j in range(1, len(party[i])):
        if find(parent, party[i][j - 1]) != find(parent, party[i][j]):
            union(parent, party[i][j - 1], party[i][j])
            
for i in range(1, n + 1):
    tmp = find(parent, i)
    if i in truth:
        truth.add(tmp)

cnt = 0          
for i in range(m):
    flag = 0
    for j in party[i]:
        if find(parent, j) in truth:
            flag = 1
            break
    if flag == 0:
        cnt += 1
print(cnt)

# 알고리즘 : union/find
'''
풀이 : 진실을 아는 사람과 같은 파티에 있던 사람은 모두 진실을 아는 사람이 된다.
파티별로 union/find를 통해 하나의 그룹으로 묶어준다.
이 후, 각 파티별로 진실을 아는 사람이 있는 지 확인한다.
만약 진실을 아는 사람이 있다면 해당 파티는 모두 진실을 아는 사람이므로 그 파티의 루트를 truth에 추가한다.

다시 파티별로 탐색하며 만약 어느 구성원이든 해당 구성원의 루트가 truth에 있다면 flag를 동작시킨다.
왜냐하면 진실을 아는 사람이 있던 그룹에 포함된 적이 있다는 뜻이기 때문이다.
만약 flag가 동작하지 않았다면 카운팅한다.
'''
