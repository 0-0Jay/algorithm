# 프로그래머스 Summer/Winter Coding(~2018) - 스킬트리 : https://school.programmers.co.kr/learn/courses/30/lessons/49993

def solution(skill, skill_trees):
    answer = len(skill_trees)
    for st in skill_trees:
        tmp = ''
        chk = set(skill)
        for i in st:
            if i in chk:
                tmp += i
        for i in range(len(tmp)):
            if skill[i] != tmp[i]: 
                answer -= 1
                break
    return answer

# 알고리즘 : 구현
'''
풀이 : 유저들이 만든 스킬트리에서 선행 스킬 순서에 포함된 스킬만 남겨서 문자열 비교한다.
문제 조건에서 스킬은 중복해서 주어지지 않기때문에 필요한 스킬만 남기는 것이 효율적이다.
따라서 각 스킬트리를 순서대로 탐색하여 skill에 존재하는 스킬만 tmp에 저장한다.
tmp에 저장된 스킬트리와 선행 스킬 순서를 0번 인덱스부터 비교한다.
만약 한번이라도 다른 스킬이 있다면, 선행 스킬 순서에 위배되는 스킬트리이므로 answer에서 1을 빼준다.
-> 위배되는 스킬트리를 제외하기 위해 answer에 스킬트리의 갯수를 저장하고 시작했다.
'''
