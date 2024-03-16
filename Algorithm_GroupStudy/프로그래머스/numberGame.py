# 프로그래머스 Summer/Winter Coding(~2018) 숫자 게임 : https://school.programmers.co.kr/learn/courses/30/lessons/12987

def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    Akey, Bkey = 0, 0
    while Bkey < len(B):
        if A[Akey] < B[Bkey]:
            Bkey += 1
            Akey += 1
            answer += 1
        else:
            Bkey += 1
    return answer

# 알고리즘 : 그리디
'''
풀이 : A팀과 B팀의 점수를 오름차순 정렬한다.
각 팀의 첫 인덱스부터 하나씩 비교하여, B가 이길 때마다 각팀에서 다음사람을 뽑으면서 answer에 1을 더한다.
만약 B가 이기지 못했다면, B팀에서만 다음 사람을 뽑는다.
'''
