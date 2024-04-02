# 프로그래머스 2024 KAKAO WINTER INTERNSHIP - 가장 많이 받은 선물 : https://school.programmers.co.kr/learn/courses/30/lessons/258712

def solution(friends, gifts):
    dict = {}
    for a in friends:
        dict[a] = {'sum' : 0, 'cnt' : 0}
        for b in friends:
            if a == b: continue
            dict[a][b] = 0
                            
    for gi in gifts:
        a, b = gi.split(' ')
        dict[a][b] += 1
        dict[a]['sum'] += 1
        dict[b]['sum'] -= 1
    sz = len(friends)
    max_cnt = 0
    for i in range(sz):
        for j in range(i + 1, sz):
            a = friends[i]
            b = friends[j]
            if dict[a][b] > dict[b][a]: dict[a]['cnt'] += 1
            elif dict[a][b] < dict[b][a]: dict[b]['cnt'] += 1
            elif dict[a]['sum'] > dict[b]['sum']: dict[a]['cnt'] += 1
            elif dict[a]['sum'] < dict[b]['sum']: dict[b]['cnt'] += 1
            max_cnt = max(max_cnt, dict[a]['cnt'], dict[b]['cnt'])
    
    return max_cnt

# 알고리즘 : 해싱
'''
풀이 : a가 b에게 선물을 주었다면, a-b쌍에 카운팅 하고, a의 선물지수는 +1, b의 선물지수는 -1해준다.
모든 인원 쌍을 비교해서 주고받을 선물을 카운팅하고, 선물 숫자를 최대값 비교해준다.
'''
