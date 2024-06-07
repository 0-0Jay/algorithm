# 프로그래머스 2018 카카오 블라인드 채용 - [1차] 셔틀버스 : https://school.programmers.co.kr/learn/courses/30/lessons/17678#

def solution(n, t, m, timetable):
    timetable.sort()
    id = 0
    bef = "09:00"
    time = "09:00"
    bus = []
    for i in range(n):
        bus.clear()  # 다음 버스가 왔으므로 버스 배열 초기화
        while id < len(timetable) and len(bus) < m:
            if timetable[id] > time: break
            bus.append(timetable[id])  # 버스에 태움
            id += 1  # 다음 사람으로 이동

        if id < len(timetable):  # 아직 안 탄 사람 있는지 검사
            bef = time
            nx = int(time[:2]) * 60 + int(time[3:]) + t
            time = ("%02d:%02d" % (nx // 60 , nx % 60))
            
    if id < len(timetable): time = bef
    if len(bus) == m:
        nx = int(bus[-1][:2]) * 60 + int(bus[-1][3:]) - 1
        time = ("%02d:%02d" % (nx // 60 , nx % 60))
        
    return time

# 알고리즘 : 구현
'''
풀이 : 마지막 셔틀버스에 타고있는 인원 수에 따라 도착 시간을 계산한다.
문제를 요약하면 다음 두 가지로 요약할 수 있다.
1. 만약 마지막 버스가 가득 찼다면, 버스에 타고 있는 사람들 중 가장 늦게 도착한 사람보다 1분 빨리 도착해야 한다.
2. 만약 마지막 버스가 가득 차지 않았다면, 버스의 도착시간에 맞추어 도착한다.

따라서 n번 반복하면서 모든 버스의 운행을 계산한다.
만약 버스가 가득 차지 않았고, timetable에 사람이 남아 있으며, timetable의 가장 앞 사람이 대기열에 있다면 버스에 태운다.
그 사람이 정류장에 도착한 시간보다 현재 버스가 도착한 시간(time)이 뒤라면, 그 사람은 대기열에 있다는 의미다.
timetable의 가장 앞 사람이 버스 도착 시간보다 뒤라면, 즉시 버스를 출발시키기 위해 break문으로 탐색을 중단한다.

각 버스가 출발할 때마다 timetable에 남은 사람이 있는지 검사한다.
있다면, 방금 도착한 버스의 시간을 bef에 저장해두고, 이 시간에 + t한 값으로 time을 갱신한다.

n개의 버스가 모두 운행했음에도 timetable에 사람이 남아 있다면, bef에 저장된 버스를 다시 time으로 불러온다.
이렇게 구한 마지막버스에 처음 요약했던 두가지 조건에 따라 도착시간을 계산한다.
'''
