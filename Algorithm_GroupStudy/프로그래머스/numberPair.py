# 프로그래머스 - 숫자 짝꿍 : https://school.programmers.co.kr/learn/courses/30/lessons/131128

def solution(X, Y):
    xcnt = {}
    ycnt = {}
    for i in X:
        if i not in xcnt: xcnt[i] = 0
        xcnt[i] += 1
    for i in Y:
        if i not in ycnt: ycnt[i] = 0
        ycnt[i] += 1
    answer = ''
    for i in range(9, -1, -1):
        tmp = str(i)
        if tmp in xcnt and tmp in ycnt:
            answer += tmp * (min(xcnt[tmp], ycnt[tmp]))
    if answer == "":
        return "-1"
    elif answer[0] == "0":
        return "0"
    return answer

# 알고리즘 : 구현
'''
풀이 : x의 숫자와 y의 숫자를 딕셔너리를 사용해 카운팅하고, 9부터 내림차순으로 1씩 낮춰가며 숫자를 answer에 더한다.
이 문제는 간단해 보이지만, 정렬을 사용하는 순간 시간초과가 발생하는 까다로운 문제다.
이 때문에, 정렬을 사용하지 않아도 큰수부터 차례대로 탐색할 수 있는 해시 자료구조인 딕셔너리를 사용한다.
x의 수(xcnt)와, y의 수(ycnt)의 각 숫자 개수를 기록한 딕셔너리를 만들고, 9부터 탐색한다.
어떤 수(tmp)가 xcnt와 ycnt에 모두 존재한다면, tmp를 더 작은 개수 만큼 answer에 추가한다.

answer가 완성되었으면, 마지막으로 검사한다.
만약 answer가 비어있으면 겹치는 숫자가 하나도 없으므로 -1을 반환한다.
answer의 첫글자가 "0"이라면 그뒤의 숫자가 몇개가 있던 다 0일것이므로 0을 반환한다.
이 때, answer를 int()함수를 사용해 정수화 했다가 다시 문자열로 반환하게되면 굉장한 시간을 소요해 시간초과가 발생하니 이 방법은 사용하지 않는다.
위의 두 경우가 아니라면 answer를 반환한다.
'''
