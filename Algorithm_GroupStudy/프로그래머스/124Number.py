# 프로그래머스 - 124 나라의 숫자 : https://school.programmers.co.kr/learn/courses/30/lessons/12899

def solution(n):
    answer = []
    while n > 0:
        now = n % 3
        if now == 0:
            now = 4
            n -= 1
        answer.append(str(now))
        n //= 3
    return ''.join(answer[::-1])

# 알고리즘 : 구현(진법 변환)
'''
풀이 : 나머지가 0일때마다 0대신 4로 치환후, n에서 1을 빼준다.
3진법 변환의 응용인데, 0을 쓰지 못하는 진법 변환이다.
따라서 3진법 변환 코드에서 나머지(now)가 0일 때마다 강제로 숫자를 4로 치환하고 n에서 1을 빼준다.
answer에 나머지를 차례대로 넣는다.
이 때, answer를 배열대신 문자열로 하게되면 시간초과가 발생한다.
n이 0이 될 때까지 수행했다면, answer에 저장된 내용을 뒤집어서 문자열로 결합후 반환한다. 
'''
