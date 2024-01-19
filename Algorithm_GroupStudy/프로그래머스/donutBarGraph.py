# 프로그래머스 2024 KAKAO WINTER INTERNSHIP 도넛과 막대 그래프 : https://school.programmers.co.kr/learn/courses/30/lessons/258711

from collections import defaultdict, deque
import heapq as hq
import math
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def union(parent, a, b):
    rootA = find(parent, a)
    rootB = find(parent, b)
    
    if rootA < rootB:
        parent[rootB] = rootA
    else:
        parent[rootA] = rootB
    
def find(parent, x):
    if x not in parent: parent[x] = x
    if parent[x] == x:
        return x
    parent[x] = find(parent, parent[x])
    return parent[x]

def solution(edges):
    parent = {}
    cnt = {}
    for a, b in edges:
        if a not in cnt: cnt[a] = [1, 0]
        else: cnt[a][0] += 1
        if b not in cnt: cnt[b] = [0, 1]
        else: cnt[b][1] += 1
        
    answer = []
    for a, b in edges:
        if cnt[a][0] >=2 and cnt[a][1] == 0:
            answer = [a, 0, 0, 0]
            break
            
    parent = {}
    for a, b in edges:
        if a == answer[0]:
            cnt[b][1] -= 1
            find(parent, b)
            continue
        if find(parent, a) != find(parent, b):
            union(parent, a, b)
    
    group = {}
    for i in parent.keys():
        find(parent, i)
        if parent[i] not in group:
            group[parent[i]] = [i]
        else:
            group[parent[i]].append(i)
            
    for lst in group.values():
        tmp = 0
        for node in lst:
            if cnt[node][0] > 1:
                answer[3] += 1
                tmp = 1
                break
            if cnt[node][1] == 0 or cnt[node][0] == 0:
                answer[2] += 1
                tmp = 1
                break
        if tmp == 0:
            answer[1] += 1

    return answer

# 알고리즘 : union/find
'''
풀이 : 각 그래프별 규칙을 찾기위해 주고 받는 간선의 갯수를 세어 무관한 정점을 찾은 후, 그래프를 구분한다.
문제에 따른 그래프들의 조건을 정리하면 다음과 같다.
1. 그래프의 갯수가 2개 이상이고, 무관한 정점에서 각 그래프로 임의의 간선이 연결된다
-> 무관한 정점은 주는 간선이 2개 이상이고, 받는 간선은 0개다.
2. 도넛 그래프는 아무 정점에서 출발해 n-1개의 정점들을 한 번씩 방문 한 뒤 출발했던 정점으로 돌아온다.
-> 도넛 그래프에 속하는 정점은 모두 주는 간선 1개, 받는 간선 1개이다.
3. 막대 그래프는 현재 정점에서 출발해 n-1개의 정점을 모두 방문할 수 있는 정점이 단 하나 존재한다.
-> 막대 그래프의 시작 정점은 주는 간선 1개, 받는 간선 0개고 끝 정점은 주는 간선 0개, 받는 간선 1개다.
4. 8자 그래프는 크기가 동일한 2개의 도넛 모양 그래프에서 정점을 하나씩 골라 결합시킨 형태다.
-> 8자 그래프에 어떤 정점 하나는 2개의 주는 간선과 2개의 받는 간선을 가진다.

1번 조건을 통해 무관한 정점을 찾기위해 간선정보 edge를 가공해 cnt배열(간선 주고받음 카운팅)을 만든다.
cnt 배열을 탐색하여 주는 간선이 2개 이상이고, 받는 간선이 없는 정점을 찾아 answer[0]에 넣는다.

무관한 정점 answer[0]을 찾았다면, edges 간선정보를 전부 탐색하며 노드를 연결한다.
만약 a, b 쌍에서 a가 무관한 정점이라면 cnt에서 b의 받는 간선 하나를 줄이고, b의 부모를 find로 다시 지정한다.
즉, 무관한 정점의 간선을 끊어주는 작업을 수행한다.

모든 무관한 정점의 간선을 끊었을 때, 연결되어 있는 노드끼리 그룹화 한다.
이 때, 그룹화된 노드들이 각각 하나의 그래프가 된다.
이를 위해 find함수로 부모 노드 하나로 재정리해주면서 같은 부모 노드와 연결된 노드들을 같은 그룹에 넣는다.

각 그룹을 하나씩 탐색하며 2~4조건에 따라 그래프를 분리한다.
위 코드에서는 불필요한 탐색을 줄이기 위해 3, 4번 조건을 먼저 계산했다.
3번 조건에 따라 한 번이라도 주는 간선 또는 받는 간선이 0개라면 직선 그래프로 체크하고 break한다.
4번 조건에 따라 한 번이라도 주는 간선이 2개 이상이면 8자 그래프로 체크하고 break한다.
3, 4번 조건을 모두 통과했다면 도넛 그래프로 체크한다.
'''
