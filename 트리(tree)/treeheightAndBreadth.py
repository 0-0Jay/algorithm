# 백준 2250번 트리의 높이와 너비 : https://www.acmicpc.net/problem/2250

from collections import defaultdict, deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n = int(input())
graph = [[] for _ in range(n + 1)]
bef = [0] * (n + 1)
for i in range(n):
    node, a, b = map(int, input().split())
    graph[node].append(a)
    graph[node].append(b)
    if a >= 0: bef[a] += 1
    if b >= 0: bef[b] += 1

root = 0
for i in range(1, n + 1):
    if bef[i] == 0:
        root = i
        break

tree = []
breadth = {}
def search(k, d):
    if k == -1: return
    search(graph[k][0], d + 1)
    tree.append(k)
    if d not in breadth:
        breadth[d] = [len(tree), len(tree)]
    else:
        breadth[d][1] = len(tree)
    search(graph[k][1], d + 1)
    
search(root, 1)
max_breadth = 0
depth = 0
for i in range(1, len(breadth) + 1):
    b = breadth[i][1] - breadth[i][0] + 1
    if b > max_breadth:
        depth = i
        max_breadth = b
print(depth, max_breadth)

# 알고리즘 : 중위 탐색
'''
풀이 : 중위탐색을 수행하며 breadth에 최저 인덱스와 최고 인덱스를 기록한 후 차를 비교한다.
tree 배열에 중위 탐색을 통해 값을 삽입하면, 각 값의 인덱스를 찾을 수 있다.
이 인덱스를 breadth에 해당하는 탐색 깊이에 기록한다.
이 때, 최초로 breadth에 입력되는 깊이는 최저 인덱스가 될 것이고, 가장 마지막에 입력되는 깊이는 최고 인덱스가 된다.
모든 노드 탐색 후, 깊이 별로 최고 인덱스 - 최저 인덱스를 수행해 가장 값이 큰 깊이와 그 너비를 출력한다.
'''
    
