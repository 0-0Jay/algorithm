# 프로그래머스 - 여행경로 : https://school.programmers.co.kr/learn/courses/30/lessons/43164#

from copy import deepcopy

res = []

def solution(tickets):
    tickets.sort(key = lambda x: (x[0], x[1]))
       
    def DFS(now, tickets, used, order):
        global res
        if res: return
        if len(used) == len(tickets):
            res = deepcopy(order)
            return            
        for i in range(len(tickets)):
            a, b = tickets[i]
            if a != now or (a, b, i) in used: continue
            used.add((a, b, i))
            DFS(b, tickets, used, order + [b])
            used.remove((a, b, i))
    
    DFS("ICN", tickets, set(), ["ICN"])
        
    return res

# 알고리즘 : DFS
'''
풀이 : 간선정보를 기준으로 DFS를 순회한다.
기존 DFS는 연결된 정점을 기준으로 수행하기 때문에 이미 방문한 정점에 대한 방문체크가 필요하다.
따라서 이 문제와 같이 같은 정점을 여러 번 방문하는 케이스가 있는 경우 사용할 수 없다.

이를 해결하기 위해 간선(항공권)의 사용여부를 기준으로 DFS를 순회한다.
이 때, 같은 간선이 여러개 입력으로 주어지는 경우가 있기 때문에 각 간선의 인덱스를 순서쌍에 포함한다.
예를 들어 ICN -> JFK 간선이 존재한다면, (ICN, JFK, 0)과 같이 (출발, 도착, 티켓번호) 순서쌍으로 방문체크를 한다.

문제에서 모든 항공권을 사용할 수 있는 경우가 여럿있을 경우 사전순으로 앞서게 하라는 조건이 있다.
간단하게 tickets를 한번 오름차순 정렬해주면 해결된다.
자연스럽게 사전순으로 앞서는 간선부터 탐색하기 때문에 가장 먼저 도출되는 결과(res)가 정답이 된다.
'''
