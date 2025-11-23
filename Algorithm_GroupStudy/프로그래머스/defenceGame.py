# 프로그래머스 - 디펜스 게임 : https://school.programmers.co.kr/learn/courses/30/lessons/142085

import heapq as hq

def solution(n, k, enemy):
    que = []
    for i in range(len(enemy)):
        hq.heappush(que, enemy[i])
        if len(que) > k:
            n -= hq.heappop(que)
            if n < 0: return i
    
    return len(enemy)

# 알고리즘 : 힙
'''
풀이 : 우선순위 큐를 활용해 적 병력이 가장 적을 때만 병력을 소모한다.
우선순위 큐에 1라운드의 병력부터 하나씩 넣는다.
만약 우선순위 큐의 길이가 사용할 수 있는 무적권(k)의 개수보다 크다면, 
pop하여 가장 적은 적 병력을 꺼내 현재 병력(n)에서 빼준다.
이렇게 하면 현재까지 진행한 라운드 중에서 k개의 가장 많은 병력에는 전부 무적권을 사용한 것과 같다.
n이 음수가 되면, 현재 라운드에서 게임이 종료된것이기 때문에 이전 라운드를 반환한다.
만약 마지막 라운드까지 진행했음에도 n이 음수가 아니라면, enemy의 길이를 반환한다.
'''
