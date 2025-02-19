# 프로그래머스 - 추억 점수 : https://school.programmers.co.kr/learn/courses/30/lessons/176963

def solution(name, yearning, photo):
    dict = {}
    for i in range(len(name)):
        dict[name[i]] = yearning[i]
    answer = []
    for pt in photo:
        tmp = 0
        for j in pt:
            if j in dict:
                tmp += dict[j]
        answer.append(tmp)
    return answer

# 알고리즘 : 해시
'''
풀이 : 딕셔너리로 이름과 그리움 점수를 저장해놓고 photo를 탐색한다.
'''
