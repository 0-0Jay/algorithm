# 프로그래머스 - 지폐 접기 : https://school.programmers.co.kr/learn/courses/30/lessons/340199

def solution(wallet, bill):
    answer = 0
    wallet.sort()
    while True:
        bill.sort()
        if wallet[0] >= bill[0] and wallet[1] >= bill[1]: break
        bill[1] //= 2
        answer += 1
    return answer

# 알고리즘 : 완전탐색
'''
풀이 : 지갑과 지폐를 항상 가로로 두고 크기를 비교한다.
먼저 지갑을 정렬해서 긴 쪽이 1번 인덱스에 가게끔 한다.
지폐의 긴쪽을 1번 인덱스에 두고, 지갑과 지폐의 길이를 비교한다.
만약 지폐의 가로세로가 모두 지갑의 길이 이하면, 반복문을 멈춘다.
그렇지 않다면 지폐를 반으로 접고, answer에 1을 추가한뒤, 위 과정을 반복한다.
'''
