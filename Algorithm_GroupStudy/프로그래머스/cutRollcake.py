# 프로그래머스 - 롤케이크 자르기 : https://school.programmers.co.kr/learn/courses/30/lessons/132265

def solution(topping):
    chk = [[0, 0] for _ in range(len(topping))]
    chk[0][0] = 1
    chk[-1][1] = 1
    left,right = set(), set()

    for i in range(len(topping)):
        left.add(topping[i])
        right.add(topping[-i-1])
        chk[i][0] = len(left)
        chk[-i-1][1] = len(right)
        
    answer = 0
    for i in range(len(topping) - 1):
        if chk[i][0] == chk[i + 1][1]: answer += 1
        
    return answer

# 알고리즘 : 완전탐색
'''
풀이 : 왼쪽 끝과 오른쪽 끝에서 출발하여 반대쪽 끝까지 토핑의 종류 수를 기록한다.
2차원 배열을 하나 생성한다.(chk)
chk[0]은 왼쪽에서 출발해서 오른쪽 끝까지 이동했을 때 토핑의 종류 수를 기록한다.
chk[1]은 오른쪽에서 출발해서 왼쪽 끝까지 이동했을 때 토핑의 종류 수를 기록한다.
이 때, 집합자료형(left, right)를 이용해서 집합에 토핑을 넣어서 중복을 배제하는 방법으로 토핑의 종류 수를 구한다.

모든 기록이 완료되었다면 chk배열을 1회 쭉 순회하여 탐색한다.
왼쪽의 토핑 종류 수와 오른쪽의 토핑 종류 수가 같아지는 지점의 수를 카운팅한다.
'''
