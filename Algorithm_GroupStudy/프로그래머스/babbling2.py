# 프로그래머스 - 올알이(2) : https://school.programmers.co.kr/learn/courses/30/lessons/133499

def solution(babbling):
    chk = set({'aya', 'ye', 'woo', 'ma'})
    answer = 0
    for bab in babbling:
        con = ''
        while bab:
            if bab[:3] == 'aya' and con != 'aya':
                con = 'aya'
                bab = bab[3:]
            elif bab[:2] == 'ye' and con != 'ye':
                con = 'ye'
                bab = bab[2:]
            elif bab[:3] == 'woo' and con != 'woo':
                con = 'woo'
                bab = bab[3:]
            elif bab[:2] == 'ma' and con != 'ma':
                con = 'ma'
                bab = bab[2:]
            else:
                break
        if bab == '': answer += 1        
    
    return answer

# 알고리즘 : 구현
'''
풀이 : 앞에서부터 가능한 발음을 빼가며 탐색한다.
만약 불가능한 발음이 발견되면 즉시 break로 멈춘다.
변수(con)를 하나 두어 이전에 발음한 발음을 기억시킨다.
발음을 잘라냈을 때, 그 발음이 가능한 발음이고, con과 다른 발음이면 해당 발음을 지우고 나머지 단어로 bab을 갱신한다.
단어의 모든 발음이 지워졌다면, 가능한 단어기때문에 answer에 1을 올리고, 그렇지 않다면 다음 단어로 넘어간다.
'''
