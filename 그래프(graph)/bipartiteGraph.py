# 백준 1707번 이분 그래프 : https://www.acmicpc.net/problem/1707

from collections import defaultdict, deque
from functools import cmp_to_key
import heapq as hq
import math
import sys
input = sys.stdin.readline

n = int(input())

for test_case in range(n):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]
    node = [0] * (v + 1)
    que = deque()
    ans = "YES"
    for i in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    for i in range(1, v + 1):
        que.append(i)
        if node[i] == 0: node[i] = 1
        while que:
            now = que.popleft()
            for j in graph[now]:
                if node[j] == 0:
                    node[j] = -node[now]    
                    que.append(j)
                elif node[j] != -node[now]:
                    ans = "NO"
          
    print(ans)

# 알고리즘 : BFS
'''
풀이 : BFS로 돌면서 현재 노드의 값의 부호를 바꾼 값을 다음 노드에 저장한다.
만약 다음 노드에 방문한 적이 있으면 해당 노드와 현재 노드의 부호가 반대인지 체크한다.
만약 두 노드의 부호가 같다면 ans를 NO로 바꾼다.
매 테스트케이스마다 사용할 que, graph, ans, node 등의 배열은 초기화해주어야 다음 테스트에 영향을 주지 않는다.
'''
