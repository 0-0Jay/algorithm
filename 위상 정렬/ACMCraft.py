# 백준 1005번 ACM Craft : https://www.acmicpc.net/problem/1005

from collections import deque
import heapq as hq
import sys
input = sys.stdin.readline

t = int(input())

for case in range(t):
    n, k = map(int, input().split())
    cost = [0] + list(map(int, input().split()))
    req = [[] for _ in range(n + 1)]
    chk = [0] * (n + 1)
    
    for i in range(k): # 연결 순서
        a, b = map(int, input().split())
        chk[b] += 1
        req[a].append(b)
    w = int(input())
    
    # 요구 건물 없는 것 heap에 삽입
    que = []
    for i in range(1, n + 1):
        if chk[i] == 0:
            hq.heappush(que, (cost[i], i))
            
    while(que):
        time, now = hq.heappop(que)
        
        if now == w:
            print(time)
            break

        for i in req[now]:
            chk[i] -= 1
            if chk[i] == 0:
                hq.heappush(que, (time + cost[i], i))

# 알고리즘 : 위상 정렬 + 우선순위 큐
'''
풀이 : 힙을 사용해 건설시간이 빠른 것부터 지으면서 건물을 위상 정렬한다.
만약 그냥 queue를 사용해 접근한다면 다음 과정이 필요하다.
1. 현재 건물이 요구하는 건물 중 가장 건설 시간이 긴 건물을 찾는다.
2. 그 건물의 건설시간을 가져와 현재 건물의 건설시간을 합한다.

그러나 heap을 사용하면 자동으로 건설시간이 빠른 건물부터 건설되기 때문에 마지막에 남은 건물이 가장 건설시간이 긴 건물이 된다.
또한, 요구 건물들 간 깊이와 건설 시간을 모두 고려하지 않아도 된다.

건물 건설 순서는 기본적인 위상 정렬 알고리즘으로 해결했다.
1. chk배열에 남은 요구 건물의 수, req 배열에 다음에 건설해야하는 건물을 저장한다.
2. 탐색과정에서 현재 건물 다음으로 건설할 건물의 남은 요구 건물을 1 감소시키며 진행한다.
3. 만약 다음 건물의 남은 요구 건물 수가 0이되면 건설할 수 있다는 뜻이므로 heap에 넣는다.
'''
