# 프로그래머스 - 성격 유형 검사하기 : https://school.programmers.co.kr/learn/courses/30/lessons/118666

def solution(survey, choices):
    type = {'R' : 0, 'T' : 0, 'C' : 0, 'F' : 0, 'J' : 0, 'M' : 0, 'A' : 0, 'N' : 0}
    order = ["RT", "CF", "JM", "AN"]
    for i in range(len(survey)):
        type[survey[i][0] if choices[i] < 4 else survey[i][1]] += abs(choices[i] - 4)
    answer = ''
    for o in order:
        answer += o[0] if type[o[0]] >= type[o[1]] else o[1]
    return answer

# 알고리즘 : 구현
'''
풀이 : 문제에 제시된 성격유형의 점수를 측정할 딕셔너리와, 성격유형쌍을 사전순으로 짝지어 저장한 배열을 만들고, 점수를 센다.
survey에서 주는 두개의 유형을 받고, choices에서 주어진 점수가 4보다 큰지 아닌지를 판단한다.
4보다 작으면 왼쪽에 있는 유형에 점수를, 4보다 크면 오른족에 있는 유형에 점수를 준다.
점수를 메길때는 abs함수를 이용해 절대값으로 누적한다.
모든 점수 책정이 끝나면, order에서 하나씩 뽑아 2개의 문자를 각각 type에서 찾아 점수를 꺼내온다.
둘중 점수가 높은 type을 answer에 추가한다.
'''
