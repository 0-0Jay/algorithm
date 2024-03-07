프로그래머스 네트워크 : https://school.programmers.co.kr/learn/courses/30/lessons/43162

import sys
sys.setrecursionlimit(10000)

def union(parent, a, b):
    rootA = find(parent, a)
    rootB = find(parent, b)
    
    if rootA < rootB:
        parent[rootB] = rootA
    else:
        parent[rootA] = rootB
        
def find(parent, x):
    if parent[x] == x:
        return x
    parent[x] = find(parent, parent[x])
    return parent[x]
    
def solution(n, computers):
    answer = set()
    parent = [i for i in range(n)]
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1:
                union(parent, i, j)
    for i in range(n):
        answer.add(find(parent, i))
    return len(answer)

# 알고리즘 : union/find
'''
풀이 : union/find를 이용해 같은 컴퓨터를 같은 네트워크끼리 연결한다.
모든 네트워크를 연결하고 나면, parent 배열을 처음부터 탐색하여 루트 컴퓨터를 answer 집합에 넣는다.
집합으로 인해 중복이 제거되었으므로 answer의 크기를 return 한다.
'''
