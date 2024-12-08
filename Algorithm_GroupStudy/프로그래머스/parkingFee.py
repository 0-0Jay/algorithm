# 프로그래머스 2022 카카오 블라인드 채용 - 주차 요금 계산 : https://school.programmers.co.kr/learn/courses/30/lessons/92341

import math

def solution(fees, records):
    park = {}
    final = {}
    result = {}
    for rec in records:
        car_num = rec[6:10]
        if car_num not in result: result[car_num] = fees[1]
        if car_num not in final: final[car_num] = 0
        time = int(rec[:2]) * 60 + int(rec[3:5])
        if car_num not in park:
            park[car_num] = time
        else:
            final[car_num] += time - park[car_num]
            del park[car_num]
    for k, v in park.items():
        final[k] += 1439 - v
    for k, v in final.items():
        if v > fees[0]:
            result[k] += math.ceil((v-fees[0]) / fees[2]) * fees[3]
    return [v for k, v in sorted(result.items(), key=lambda x : x[0])]

# 알고리즘 : 구현, 해싱
'''
풀이 : 현재 주차 정보, 최종 주차시간, 비용을 계산할 딕셔너리를 만들고 records를 차례대로 탐색한다.
records를 순서대로 꺼내서 park에 이미 주차된 차인지 확인한다.
주차된 차가 아니라면 시간을 분단위로 기록하고, 주차된 차라면 꺼내서 주차시간을 계산하여 final에 기록한다.
records를 모두 계산했다면, final에 기록된 시간(분단위)과 fees에 기록된 정보를 계산해서 최종 비용을 계산해 result에 저장한다.
마지막으로 result를 key값을 기준으로 오름차순 정렬했을 때의 value 값을 리스트로 반환한다.
'''
