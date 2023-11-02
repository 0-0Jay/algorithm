# 프로그래머스 2018 KAKAO BLIND RECRUITMENT - [3차] n진수 게임 : https://school.programmers.co.kr/learn/courses/30/lessons/17687

import sys
from collections import deque
import heapq as hq

def solution(n, t, m, p):
    digit = ['A','B','C','D','E','F']
    num = 1
    game = '0'
    while len(game) < t * m :
        tmp = num
        res = ''
        while tmp > 0:
            a = tmp % n
            res = (str(a) if a < 10 else digit[a % 10]) + res
            tmp //= n
        game += res
        num += 1
            
    answer = ''
    for i in range(t*m):
        if i % m == p - 1:
            answer += game[i]
        
    return answer

# 알고리즘 : 구현
'''
풀이 : 10~15까지의 숫자는 A, B, C, D, E, F로 미리 만들어두고, 2~10진수까지는 일반적인 진법변환 코드로, 11~16진수는 나머지 계산을 이용한 인덱싱으로 숫자를 추가한다.
마지막으로 튜브가 말해야하는 숫자도 나머지계산을 활용해 answer에 누적하여 반환한다.
'''
