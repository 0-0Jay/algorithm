# 프로그래머스 2021 카카오 블라인드 채용 - 메뉴 리뉴얼 : https://school.programmers.co.kr/learn/courses/30/lessons/72411

from itertools import combinations

def solution(orders, course):
    answer = []
    set_list = []
    for o in orders:
        set_list.append(set(list(o)))
        
    for co in course:
        custom = {}
        for o in orders:
            tmp = sorted(o)
            comb_list = combinations(tmp, co)
            for i in comb_list:
                if i not in custom: custom[i] = 0
                custom[i] += 1
                
        max_cnt, tmp = 0, []
        for k, v in custom.items():
            if v > max_cnt:
                max_cnt = v
                tmp.clear()
                tmp.append(k)
            elif v == max_cnt:
                tmp.append(k)
                
        if max_cnt >= 2:        
            for i in tmp:
                answer.append(''.join(i))
                
    return sorted(answer)

# 알고리즘 : 조합 + 구현
'''
풀이 : 각 코스를 구성할 단품메뉴 갯수별로 combinations를 활용해 조합을 뽑아 카운팅한다.
코스 구성 단품메뉴 갯수가 2, 3, 5라면 2개, 3개, 5개를 제외한 조합은 구성할 이유가 없기때문에 배제한다.
이를 간편하게 하기 위해 combinations 함수를 사용한다.
주어진 각 주문을 정렬하여 리스트로 만든 뒤, combinations로 조합을 뽑는다.
만들어진 조합은 custom 딕셔너리에 넣어 카운팅한다.

custom에 카운팅한 조합들 중 가장 많이 주문된 조합을 찾는다.
가장많이 주문된 조합이 2번 이상 주문 되었다면, answer에 문자열로 치환하여 추가한다.
이 과정을 모든 구성 갯수 별로 수행한 후 answer를 반환한다.
'''
