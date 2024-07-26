# 프로그래머스 - 다리를 지나는 트럭 : https://school.programmers.co.kr/learn/courses/30/lessons/42583

from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    que = deque()
    total = 0
    key = 0
    while key < len(truck_weights):
        if len(que) == bridge_length or que and key < len(truck_weights) and total + truck_weights[key] > weight:
            out, time = que.popleft()
            total -= out
            time += bridge_length - 1
            if answer < time: answer = time

        if key < len(truck_weights) and len(que) < bridge_length and total + truck_weights[key] <= weight:
            total += truck_weights[key]
            answer += 1
            que.append((truck_weights[key], answer))
            key += 1

    out, answer = que.pop()
    return answer + bridge_length

# 알고리즘 : 큐 + 구현
'''
풀이 : 대기 트럭을 순서대로 que에 넣으면서, 무게를 계산한다.
반복문을 통해 다음을 수행한다.
1. 다음 트럭이 올라갈 무게가 확보될 때까지 que에서 트럭을 꺼낸다.
-> 이 때, (트럭 입장 시간(time) + 다리 길이 -1)과 answer에 저장된 시간을 비교해서 answer를 더 많은 시간으로 교체한다.
2. 트럭이 올라갈 무게가 확보되어 있다면 que에 (트럭 무게, 입장 시간) 쌍을 삽입한다.
-> 트럭을 삽입할 때마다 key를 1칸씩 옮긴다. (key가 대기 트럭만큼 이동하면 while문을 종료하기 위함)

1시간씩 계산하지 않고, 계산 과정을 축소하기 위해 que에 넣고 빼는 값을 이용하기 때문에 시간 계산을 섬세하게 해야한다.
꺼낸 트럭의 시간과 마지막으로 들어간 트럭의 입장시간을 비교하는 과정이 필요하다.
만약 마지막 트럭의 입장시간이 방금 트럭이 나온 시간보다 나중이라면, 당연히 마지막 트럭의 입장시간보다 뒤에 트럭이 입장해야한다.
그러나 마지막 트럭의 입장시간에 방금 트럭이 나온 시간보다 전이라면, 다음 트럭은 처음 트럭이 나옴과 동시에 입장해야 한다.

while문이 종료되었다면, que에 남아있는 마지막 트럭을 꺼내고, 그 트럭의 입장 시간에 다리 길이를 더한 값을 return 한다.
'''
