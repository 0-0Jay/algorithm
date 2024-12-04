# 프로그래머스 2023 카카오 블라인드 채용 - 개인정보 수집 유효기간 : https://school.programmers.co.kr/learn/courses/30/lessons/150370

def solution(today, terms, privacies):
    answer = []
    dict = {}
    today = int(today[:4]) * 12 * 28 + int(today[5:7]) * 28 + int(today[8:])
    for t in terms:
        a, b = t.split(" ")
        dict[a] = int(b) * 28
    for i in range(len(privacies)):
        day, t = privacies[i].split(" ")
        day = int(day[:4]) * 12 * 28 + int(day[5:7]) * 28 + int(day[8:])
        if today - day >= dict[t]:
            answer.append(i + 1)
    return answer

# 알고리즘 : 구현
'''
풀이 : 오늘 날짜와 각 날짜를 숫자값으로 변환후, 차를 계산하여 term과 비교한다.
today와 terms의 값을 일 수로 변환한다.
terms는 월단위이므로 주어신 숫자에 * 28을 해서 딕셔너리로 두고, today는 일 단위로 바꿔둔다.
privacies를 처음부터 탐색한다.
날짜(day)는 today와 마찬가지로 일단위로 바꾸고, today와 차를 계산한다.
만약 today - day의 값이 딕셔너리에 저장된 약관의 유효 일수(t) 이상이라면, 해당 인덱스를 answer에 추가한다.
'''
