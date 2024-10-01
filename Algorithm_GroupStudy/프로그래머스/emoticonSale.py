# 프로그래머스 2023 카카오 블라인드 채용 - 이모티콘 할인행사 : https://school.programmers.co.kr/learn/courses/30/lessons/150368

from copy import deepcopy
from collections import deque

def solution(users, emoticons):
    que = deque([[]])
    plus, money = 0, 0
    while que:
        rate = que.popleft()
        if len(rate) == len(emoticons):
            p, m = 0, 0
            for s, lim in users:
                total = 0
                for i in range(len(rate)):
                    if rate[i] >= s:
                        total += emoticons[i] * (100 - rate[i]) // 100
                    if total >= lim: break
                if total >= lim: 
                    p += 1
                else:
                    m += total
            if p > plus or p == plus and m > money: plus, money = p, m
            continue
            
        for i in range(10, 41, 10):
            que.append(rate + [i])
    
    return [plus, money]

# 알고리즘 : 브루트포스
'''
풀이 : 4개의 할인율이 가능한 모든 조합을 계산하고, 최대이득을 구한다.
주어지는 데이터의 크기가 크지 않으므로 브루트포스를 사용해도 무관하다.
먼저 BFS로 각 이모티콘의 10% ~ 40% 중 하나의 할인율을 고르는 모든 경우를 찾는다.
이를 이 코드에서는 배열(rate)에 한칸씩 채우는 것을 이용했다.

rate의 길이가 emoticons의 길와 같아지면, 모든 이모티콘에 할인율이 적용되었다는 의미다.
따라서 이모티콘의 할인율에 따른 각 인원의 소모 비용을 계산한다.
만약 이모티콘의 할인율(rate[i])이 요구하는 할인율(s) 이상이라면, 할인된 가격을 total에 누적한다.
이 때, total이 그 인원의 한도(lim) 이상이라면, 즉시 탐색을 구만두고 플러스 가입 인원(p)에 1을 더해준다.
조건에 맞는 모든 이모티콘을 결제했음에도 total이 lim보다 작다면, total을 이모티콘 매출액(m)에 더해준다.
모든 인원에 대한 결제 금액 계산이 완료되면 문제 조건에 따라 plus와 money를 p와 m의 값과 비교하여 교체한다.

모든 경우의 수를 계산한 후에 plus와 money를 반환한다.
'''
