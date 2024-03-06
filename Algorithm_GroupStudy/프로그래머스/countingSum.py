# 프로그래머스 연속 부분 수열 합의 개수 : https://school.programmers.co.kr/learn/courses/30/lessons/131701

def solution(elements):
    answer = set()
    tmp = [0]
    sz = len(elements)
    for i in range(sz * 2):
        tmp.append(elements[i % sz] + tmp[i])
    for i in range(sz):
        for j in range(i + 1, i + sz + 1):
            answer.add(tmp[j] - tmp[i])
        
    return len(answer)

# 알고리즘 : 구간합
'''
풀이 : 나머지 연산을 이용해 순환하는 숫자에 대한 구간합을 구한다.
미리 elements 배열 두개를 이어붙였을때의 구간합을 구해둔다.
어떤 수(i)를 기준으로 잡고 그 수 부터 j개의 숫자에 대한 구간합을 구해 answer 집합에 추가한다.
집합은 중복을 제거하는 자료구조이기 때문에 answer의 크기를 return 한다.
'''
