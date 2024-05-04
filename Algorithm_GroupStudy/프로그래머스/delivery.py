# 프로그래머스 2023 카카오 블라인드 채용 - 택배 배달과 수거하기 : https://school.programmers.co.kr/learn/courses/30/lessons/150369

def solution(cap, n, deliveries, pickups):
    answer = 0
    while deliveries and deliveries[-1] == 0: deliveries.pop(-1)
    while pickups and pickups[-1] == 0: pickups.pop(-1)
    while deliveries or pickups:
        answer += 2 * max(len(deliveries), len(pickups))  # 왕복 거리 추가
        truck = 0
        while deliveries and truck <= cap: truck += deliveries.pop(-1)  # 가장 먼 곳부터 배달
        if truck > cap: deliveries.append(truck - cap)
        truck = 0
        while pickups and truck <= cap: truck += pickups.pop(-1)  # 가장 먼 곳부터 수거
        if truck > cap: pickups.append(truck - cap)
    return answer

# 알고리즘 : 투포인터 + 그리디 (사용 언어가 파이썬이라 리스트 활용으로 해결)
'''
풀이 : 가장 짧은 거리를 왕복하려면 가장 멀리 가는 횟수를 최소화한다.
우선 deliveries와 pickups에서 0이 아닌 수가 나올 때까지 pop해준다.
배달할 택배와 수거할 상자가 모두 없는 집은 계산할 필요가 없기 때문이다.

이 후, deliveries의 길이와 pickups의 길이를 비교하여 더 긴 값을 찾는다.
만약 deliveries의 길이가 7이고 pickups의 길이가 6이라면, 더 긴 값은 7이 된다.
배달해야할 집이 7거리만큼 떨어져있고, 트럭은 반드시 물류창고로 돌아와야 하기때문에 최소 7거리를 1회 왕복해야한다.
따라서 answer에 2 * (둘중 더 긴 길이)를 누적한다.

1회 왕복에 드는 거리를 계산했으니, 다시 최대 왕복 거리를 갱신해야한다.
deliveries와 pickups의 오른쪽 끝에서부터 pop하면서 트럭 적재량(truck)이 트럭 수용량(cap)보다 커질때까지 누적한다.
truck이 cap보다 커졌다면, truck-cap의 값을 마지막 집에 남긴다. (pop 했기 때문에 append로 다시 추가한다.)

위 두 과정을 통해 deliveries와 pickups의 길이는 감소하게 되고, 그에 따른 리스트 길이를 새로 비교해 answer에 누적한다.
이를 두 리스트 모두 길이가 0이 될때까지 반복한다.
'''
