# 백준 1967번 트리의 지름 : https://www.acmicpc.net/problem/1967

from collections import defaultdict, deque
import heapq as hq
import math
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n = int(input())
graph = [[] for _ in range(n + 1)]
for i in range(n - 1):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])

diameter = 0
chk = set()
def search(k, cost):
    global diameter
    if len(graph[k]) == 0: return cost
    len_list = []
    for nx, co in graph[k]:
        if nx not in chk:
            chk.add(nx)
            len_list.append(search(nx, co))
            chk.remove(nx)
    len_list.sort()
    if len(len_list) > 1 and len_list[-2] + len_list[-1] > diameter: diameter = len_list[-1] + len_list[-2]
    else: diameter = max(diameter, len_list[-1])
    return len_list[-1] + cost
search(1, 0)

print(diameter)

# 알고리즘 : DFS
'''
풀이 : DFS를 수행하며 가장 긴 루트만 return으로 올려보낸다.
어떤 노드에서 다음 노드로 갈 루트 중 가장 긴 루트 두개를 골라 더하면, 이 값이 곧 트리의 지름이 된다.
따라서 len_list 배열을 하나 두고 하위 노드들로 부터 반환된 루트 길이들을 저장하고, 정렬한다.
정렬된 len_list의 마지막 두 수를 더한 값과 diameter의 값을 비교해 더 큰 값으로 교체한다.
이 때, 하위 노드가 한개밖에 없어 len_list에 수가 1개 밖에 없는 경우 이를 그대로 반환한다.
또한, 이 노드와 이 노드의 상위 노드가 각각 리프와 루트일 수도 있으므로 이 길이도 diameter와 최대값 연산한다.
최종적으로 diameter를 출력하면 이 값이 트리의 지름이다.
'''
