# 프로그래머스 - 할인행사 : https://school.programmers.co.kr/learn/courses/30/lessons/131127

def solution(want, number, discount):
    need = {}
    for i in range(len(want)): need[want[i]] = number[i]
    chk = {}
    answer = 0
    for i in range(len(discount)):
        if discount[i] not in chk: chk[discount[i]] = 0
        chk[discount[i]] += 1
        if i >= 9:
            tmp = True
            for k, v in need.items():
                if k not in chk or chk[k] != v:
                    tmp = False
                    break
            if tmp: answer += 1
            chk[discount[i - 9]] -= 1
    return answer

# 알고리즘 : 구현(슬라이딩 윈도우)
'''
풀이 : 딕셔너리를 활용해 슬라이딩 윈도우 기법으로 체크한다.
먼저 want와 number를 합쳐서 딕셔너리(need)에 저장한다.
슬라이딩 윈도우 기법으로 10일동안의 할인행사품목을 기록할 chk 딕셔너리를 만들고 discount를 0번인덱스부터 탐색한다.
10일간 물건을 1개씩만 살 수 있기 때문에 chk에 들어간 물품의 총 개수가 10개가 되기전까지는 계속 discount의 물품을 chk에 누적한다.
chk의 물품 개수가 10개가 되었다면, need에 기록되어 있는 필요 물품과 chk에 누적된 필요 물품의 개수가 완전히 일치한지 확인하고, 일치하면 answer에 1 카운팅 해준다.
이 후, 다음 탐색을 위해 chk에서 가장 먼저 누적했던 물품을 빼준다.(discount의 현재 인덱스에서 -9한 인덱스의 물품)
모든 탐색이 끝났다면, answer을 return 한다.
'''
