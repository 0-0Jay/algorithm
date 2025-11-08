# 프로그래머스 - 배달 : https://school.programmers.co.kr/learn/courses/30/lessons/12978?language=python3

import heapq as hq

def solution(N, road, K):
    answer = 0
    route = [[] for _ in range(N + 1)]
    for a, b, c in road:
        route[a].append((b, c))
        route[b].append((a, c))
    dist = [1e9] * (N + 1)
    dist[1] = 0
    que = [(1, 0)]
    while que:
        now, d = hq.heappop(que)
        if dist[now] < d or d > K: continue
        for nx, co in route[now]:
            if dist[nx] > d + co:
                dist[nx] = d + co
                hq.heappush(que, (nx, dist[nx]))
    for i in dist:
        if i <= K: answer += 1

    return answer

# 알고리즘 : 다익스트라
'''
풀이 : 1번 마을을 기준으로 다익스트라를 수행한다.
일반적인 다익스트라 문제다.
단, 문제에서 K 시간 이하로 배달이 가능한 마을에서만 주문을 받는다는 조건이 있기 때문에,
다익스트라를 수행하면서 현재까지 걸린 시간이 K시간 보다 크다면 continue로 탐색을 중단시킨다.
모든 탐색이 끝났다면 dist내에서 K시간 이하인 마을의 개수를 세어 반환한다.
'''
