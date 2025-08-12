# 백준 2001번 보석 줍기 : https://www.acmicpc.net/problem/2001

from collections import defaultdict, deque
import sys
input = sys.stdin.readline
from decimal import Decimal

n, m, k = map(int, input().split())
jewel = {}
for i in range(k):  # 보석 비트자리수로 맵핑
    jewel[int(input())] = i
    
route = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    route[a].append((b, c))
    route[b].append((a, c))
    
chk = [[0] * (1 << k + 1) for _ in range(n + 1)]
max_cnt = 0
que = deque()
que.append((1, 0, 0))  # 섬, 비트, 보석 수
chk[1][0] = 1
if 1 in jewel: chk[1][1] = 1  # 1번 섬에서 보석을 줍는 경우
while que:
    now, bit, cnt = que.popleft()
    
    if now == 1:
        max_cnt = max(max_cnt, cnt)

    for nx, limit in route[now]:
        if cnt > limit: continue
        if chk[nx][bit] == 0:  # 다음 섬에서 보석을 줍지 않는 경우
            chk[nx][bit] = 1
            que.append((nx, bit, cnt))
        if nx in jewel:  # 다음 섬에 보석이 있으면
            tmp = bit | (1 << jewel[nx])  # 보석을 줍는 경우(이미 주워져 있으면 그냥 넘어감 or연산이기 때문)
            if chk[nx][tmp] == 0:
                chk[nx][tmp] = 1
                que.append((nx, tmp, cnt + 1))
                
print(max_cnt)

# 알고리즘 : BFS + 비트마스킹
'''
풀이 : 보석이 있는 섬을 비트 자릿수로 맵핑한 뒤, 보석 획득 여부에 따라 비트를 컨트롤하며 BFS를 수행한다.
1번 섬에서 출발하기 때문에 1번 섬에서 보석을 줍고 출발하는 경우와 출발하지 않고 출발하는 경우를 큐에 넣는다.
단, 1번 섬에 보석이 존재하는 경우에만 줍고 출발하는 경우를 고려한다.

1번 섬부터 route배열에 저장된 연결된 다른 섬을 순서대로 탐색한다.
이 때, 현재 가진 보석수가 해당 다리의 limit보다 클 경우 해당 섬을 이동할 수 없으므로 continue 한다.
이동할 수 있는 다리라면, 다음 섬에서 보석을 줍는 경우와 줍지 않는 경우를 que에 넣는다.
단, 이 경우에도 다음 섬에 보석이 존재하는 경우에만 줍고 출발하는 경우를 고려한다.
만약 다음 섬에서의 bit에 대한 방문기록이 chk에 존재 한다면, 해당 경우는 더 탐색하지 않는다.
같은 양과 같은 종류의 보석을 가지고 해당 섬에 도착한 기록이 있다면 굳이 한 번 더 탐색하지 않아도 되기 때문이다. 

이 과정을 위해 입력단계에서 주어지는 보석이 존재하는 섬의 정보를 가공할 필요가 있다.
섬의 개수는 최대 n개인데, 이 를 그대로 비트마스킹에 사용해버리면 최대 2^100이라는 숫자를 컨트롤하게 된다.
이 경우, 비트마스킹할 때 반드시 오버플로우가 발생한다. (python에서도 발생하니 다른 언어는 무조건 발생한다.)
따라서 사전작업으로 딕셔너리를 이용해 각 섬을 순차적으로 다음과 같이 맵핑해준다.
1  -> 1
4  -> 2
14 -> 3
28 -> 4
57 -> 5
100-> 6
위와 같이 맵핑을 해두고 비트마스킹 하면 14개의 비트만 가지고 모든 경우를 탐색할 수 있다.
'''
