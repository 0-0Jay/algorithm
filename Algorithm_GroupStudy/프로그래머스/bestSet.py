# 프로그래머스 최고의 집합 : https://school.programmers.co.kr/learn/courses/30/lessons/12938

def solution(n, s):
    if n > s: return [-1]
    answer = [s // n] * n
    remain = s % n
    for i in range(n - 1, n - remain - 1, -1):
        answer[i] += 1

    return answer

# 알고리즘 : 그리디
'''
풀이 : 최고의 곱을 내려면 최대한 균등하게 수가 분배되어야 한다.
이를 위해 맨처음 answer 배열을 s를 n으로 나눈 몫이 n개 있는 배열로 초기화 한다.
그리고, 그 나머지를 remain에 저장해둔다.
이러면 remain에 저장된 수는 반드시 n보다 작을 수 밖에 없다.
따라서 answer의 마지막 인덱스부터 remain에 저장된 수만큼의 인덱스에 1씩 더해주어 반환한다.
'''
