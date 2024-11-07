# 프로그래머스 - 부대복귀 : https://school.programmers.co.kr/learn/courses/30/lessons/132266

import heapq as hq

def solution(n, roads, sources, destination):
    graph = [[] for i in range(n + 1)]
    for i in range(len(roads)):
        a, b = roads[i]
        graph[a].append(b)
        graph[b].append(a)
    
    que = []
    diff = [1e12 for i in range(n + 1)]
    diff[destination] = 0
    que.append((destination, 0))
    while que:
        now, c = hq.heappop(que)
        if c > diff[now]: continue
        for nx in graph[now]:
            if diff[nx] > c + 1:
                diff[nx] = c + 1
                hq.heappush(que, (nx, c + 1))
    
    answer = []
    for i in sources:
        answer.append(diff[i] if diff[i] != 1e12 else -1)
    return answer

# 알고리즘 : 다익스트라
'''
풀이 : destination으로 부터 다익스트라를 돌려 각 sourse까지의 최단시간을 구한다.
sourses의 각 부대원들이 destination에 복귀하는 최단시간은 반대로 생각하면 destination으로 부터 sourse로 가는 최단시간이다.
입력된 roads의 경로는 왕복이 가능하기 때문에 graph에 왕복이 가능하게 저장한다.
diff에 destination에 해당하는 부분은 0으로 초기값을 주고 destination으로 부터 우선순위큐를 활용해 다익스트라를 수행한다.
탐색 후, diff 배열에서 sourse에 해당하는 각 인덱스의 값을 가져오되, 시간이 1e12면 복귀가 불가능하므로 -1을 저장한다.
'''
