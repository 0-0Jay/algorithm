# 백준 1068번 트리 : https://www.acmicpc.net/problem/1068

from collections import defaultdict, deque
import heapq as hq
import math
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n = int(input())
graph = [[] for _ in range(n)]
arr = list(map(int, input().split()))
root = -1
for i in range(n):
    if arr[i] >= 0:
        graph[arr[i]].append(i)
    else: root = i
erase = int(input())

cnt = 0
def search(k):
    global cnt
    tmp = 0
    for nx in graph[k]:
        if nx == erase: continue
        tmp += 1
        search(nx)
    if tmp == 0: cnt += 1

if erase != root: search(root)
print(cnt)

# 알고리즘 : 트리
'''
풀이 : 입력되는 부모 노드 정보에 따라 graph에 인접리스트로 기록 후, 탐색한다.
각 노드별로 tmp에 다음 노드로 이동한 횟수를 기록한다.
이 때, 지워진 노드라면 continue를 통해 tmp에 카운팅하지 않는다.
이렇게 하면 최종적으로 tmp의 수가 해당 노드의 하위 노드 수가 된다.
따라서 tmp가 0인 노드의 수를 cnt에 카운팅하여 출력한다.

단, 지울 노드가 root 노드가 되면, 탐색할 필요가 없다.
'''
