# 프로그래머스 - 유연근무제 : https://school.programmers.co.kr/learn/courses/30/lessons/388351

def solution(schedules, timelogs, startday):
    answer = 0
    for i in range(len(schedules)):
        schedules[i] += 10
        if schedules[i] % 100 >= 60: schedules[i] += 40
        cnt = 0
        sat = 6 - startday if startday != 7 else 6
        sun = 7 - startday
        for j in range(7):
            if j not in {sat, sun} and timelogs[i][j] <= schedules[i]: cnt += 1
        if cnt == 5:
            answer += 1
    return answer

# 알고리즘 : 구현
'''
풀이 : startday만큼 토요일, 일요일을 당겨서 그 요일을 제외하고 검사한다.
먼저 schedule[i]에 10을 더한다. 만약 이 값의 뒷 두자리 수가 60보다 크면, 40을 더해 시간을 올려준다.
토요일과 일요일에서 startday만큼을 빼서 인덱스를 당긴다.
토요일과 일요일은 이벤트를 적용하지 않기 때문에 위에서 구한 인덱스는 무시한다.
각 인덱스에 저장된 시각이 10을 더한 schedule[i] 이하라면 카운팅한다.
이 카운트가 5라면 answer에 1씩 누적한다.
'''
