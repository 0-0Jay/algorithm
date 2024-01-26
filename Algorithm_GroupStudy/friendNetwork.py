# 백준 4195번 친구 네트워크 : https://www.acmicpc.net/problem/4195

from collections import defaultdict, deque
import sys
input = sys.stdin.readline

def union(parent, count, a, b):
    rootA = find(parent, a)
    rootB = find(parent, b)
    
    if rootA != rootB:
        parent[rootB] = rootA
        count[rootA] += count[rootB]
    print(count[rootA])
        
def find(parent, x):
    if parent[x] == x:
        return x
    parent[x] = find(parent, parent[x])
    return parent[x]

test_case = int(input())
for _ in range(test_case):
    f = int(input())
    parent = {}
    count = {}
    for i in range(f):
        a, b = input().strip().split(" ")
        if a not in parent:
            parent[a] = a
            count[a] = 1
        if b not in parent:
            parent[b] = b
            count[b] = 1
        union(parent, count, a, b)

# 알고리즘 : 해싱 + union/find
'''
풀이 : 친구관계가 입력될 때마다 해당 인원은 해시배열(딕셔너리)에 넣고, union/find를 수행한다.
두 사람 a, b가 각각 parent에 있는지 확인하고 없으면 새로 추가한다.
parent에는 union/find에 사용할 부모 노드를 저장하기 위해 자기 자신을 부모 노드로 추가한다.
count에는 해당 사람의 친구 수를 1로 하여 추가한다.
추가 후, union함수를 통해 두 사람 a, b를 연결해 b의 부모 노드를 a로 바꾸고 , a에 b의 친구 수를 모두 합산한다.
친구 관계가 생길 때마다 두 사람의 친구 네트워크의 인원 수를 출력해야 하므로 a의 친구 수를 출력한다.
'''
