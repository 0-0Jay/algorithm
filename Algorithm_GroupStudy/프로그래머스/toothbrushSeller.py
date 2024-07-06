# 프로그래머스 2021 Dev-Matching - 다단계 칫솔 판매 : https://school.programmers.co.kr/learn/courses/30/lessons/77486

from collections import deque

def solution(enroll, referral, seller, amount):
    answer = [0] * len(enroll)
    mapping = {}
    parent = {}
    for i in range(len(enroll)):
        mapping[enroll[i]] = i
        parent[enroll[i]] = referral[i]
        
    for i in range(len(seller)):
        cost = amount[i] * 100
        now = seller[i]
        while True:
            tax = cost // 10
            if now == '-': break
            answer[mapping[now]] += cost - tax
            if tax == 0: break
            cost = tax
            now = parent[now]
        
    return answer

# 알고리즘 : 구현 + 해싱(딕셔너리)
'''
풀이 : 부모를 기록한 배열을 활용해 매 seller마다 부모에게 10%를 전달한다.
문제를 풀기에 앞서, 매 seller마다 부모에게 10%를 전달하는 조건이 중요하다.
모든 seller를 종합하여 10%를 매기는 것이 아니다.
따라서 복잡하게 위상 정렬이나 그래프 탐색을 사용하지 않는다.

enroll과 referral을 통해 parent에 (해당 인원 : 추천인) 쌍을 딕셔너리로 저장한다.
seller 배열을 탐색하여 수익의 10%를 계산한다(tax)
수익 - tax한 값을 현재 seller에 누적시킨다.
cost를 tax로 업데이트 해주고, 현재 인원의 부모에서 위 과정을 반복한다.
만약 tax가 0이라면 추가 탐색하지 않기 위해 break로 while문을 종료한다.

모든 계산을 끝낸 후에 answer를 반환한다
'''
