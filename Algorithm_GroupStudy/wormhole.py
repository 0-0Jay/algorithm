# 백준 1865번 웜홀 : https://www.acmicpc.net/problem/1865

from collections import deque
import heapq as hq
import sys
input = sys.stdin.readline

t = int(input())
INF = 500000000

def bellman_ford():  #벨만-포드 알고리즘
    dist = [INF for _ in range(n + 1)]
    # dist[1] = 0
    for i in range(1, n + 1): n-1
        for now in range(1, n + 1):
            for nx, cost in route[now]:
                if dist[nx] > dist[now] + cost: # dist[now] != INF
                    dist[nx] = dist[now] + cost
                    if i == n:  # n번째에도 값의 변화가 발생하는지 체크
                        return True
    return False              

for test in range(t):
    n, m, w = map(int, input().split())
    route = [[] for _ in range(n + 1)]
    for i in range(m):
        s, e, t = map(int, input().split())
        route[s].append((e, t))
        route[e].append((s, t))
    for i in range(w):
        s, e, t = map(int, input().split())
        route[s].append((e, -t))
        
    if bellman_ford(): print("YES")
    else: print("NO")

# 알고리즘 : 벨만-포드 알고리즘
'''
풀이 : 벨만-포드 알고리즘으로 음수 사이클을 찾아낸다.
일반적인 벨만-포드 알고리즘 문제와 다른 문제다.
시작 정점이 어떤 노드가 되든 상관없기 때문에 dist[1] = 0과 같은 시작 정점 선정을 할 필요가 없다.
음수 사이클이 생기는지 안생기는 지만 궁금한 문제이므로 dist[now]가 INF인지 아닌지도 고려할 필요 없다.
단순히 최소 비용 루트만 고려했을 때 음수 사이클이 발생하면 True, 안하면 False를 반환하면 된다.
노드가 n개라면 n-1번만 탐색해도 모든 탐색을 할 수 있다.
만약 n-1번 탐색후 다음 탐색인 n번째 탐색을 했을 때 값의 변화가 발생하면, 무한 음수 사이클이 돌고 있다는 뜻이다.

벨만-포드 알고리즘은 다익스트라와 비슷한 알고리즘이다.
매 탐색마다 모든 간선을 탐색하여 더 작은 값이 있으면 교체한다.
교체를 진행하다보면 사이클을 이루는 간선들 사이에서, 음수 간선의 합이 양수 간선의 합보다 커지는 구간이 발생할 수 있는데, 이 것이 음수 사이클이다.
이 경우, 사이클을 한바퀴 돌 때마다 모든 노드의 비용이 무한대로 작아지기 때문에 최저 비용 사이클을 구할 수 없다.
그러나 이 문제는 단순히 원래 자리로 돌아왔을때 이전보다 시간이 줄어든 경우가 있는지를 찾는 문제다.
즉, 음수 사이클의 존재 여부만 확인하면 된다.
'''
