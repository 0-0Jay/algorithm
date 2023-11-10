# 프로그래머스 PCCP 기출문제 1번 : https://school.programmers.co.kr/learn/courses/19344/lessons/242258

def solution(bandage, health, attacks):
    answer = health
    time = 0
    con = 0
    for i in range(len(attacks)):
        answer += (attacks[i][0] - time - 1) * bandage[1]
        answer += ((attacks[i][0] - time - 1) // bandage[0]) * bandage[2]
        time = attacks[i][0]
        if answer > health: answer = health
        
        answer -= attacks[i][1]
        if answer <= 0: return -1    
        
    return answer

# 알고리즘 : 구현
'''
풀이 : 공격 배열을 돌면서 체력상태를 조정한다.
'''
