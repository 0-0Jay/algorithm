# 정올 - 최소비용신장트리 : https://jungol.co.kr/problem/1060?cursor=MTAsNiwxMQ%3D%3D

import sys
import heapq as hq
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
chk = set()
que = []
hq.heappush(que, (0, 0))
res = 0

while que:
    co, no = hq.heappop(que)
    if no not in chk:
        res += co
        chk.add(no)

        for i in range(n):
            if graph[no][i] != 0:
                hq.heappush(que, (graph[no][i], i))
                    
print(res)

# 알고리즘 : 프림
'''
풀이 : 주어진 그래프에서 연결가능한 다음 간선 중 최소 비용인 간선을 찾아 연결한다.
아무 노드에서나 출발해도 무관하기 때문에 임의로 0번노드에서 시작해 0비용으로 출발한다.
힙은 비용기준 최소힙으로 설정한다.
힙에서 하나를 꺼내면 해당 노드가 현재 연결가능한 간선중 가장 적은 비용으로 갈 수 있는 노드다.
따라서 해당 노드까지의 비용을 res에 누적하고, chk에 해당 노드를 추가한다.
방금 추가한 노드와 연결된 다음 간선들 중 자기 자신을 제외하고 전부 힙에 넣는다.
모든 노드가 chk에 저장될 때까지 반복한 후 res에 누적된 값을 출력한다.
'''
