# 백준 1916번 최소비용 구하기 : https://www.acmicpc.net/problem/1916

import heapq as hq
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
diff = [1e12] * (n + 1)

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    
st, ed = map(int, input().split())
diff[st] = 0
que = [(0, st)] # 가중치, 노드

while que:
    val, now = hq.heappop(que)
    if val > diff[now]: continue
    for nx, w in graph[now]:
        if val + w < diff[nx]:
            diff[nx] = val + w
            hq.heappush(que, (val + w, nx))

print(diff[ed])
        
# 알고리즘 : 다익스트라
'''
풀이 : 일반적인 다익스트라로 st부터 ed까지의 최소비용을 계산한다.
다익스트라 탐색을 효율적으로 하기위해 우선순위 큐로 데이터를 처리한다.
뽑은 값(val)이 diff에 저장된 값보다 크면, 어떤 루트라도 diff로 시작한 것보다 값이 크기 때문에 continue로 배제한다.
'''
            
