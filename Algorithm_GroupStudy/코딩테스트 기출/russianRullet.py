# 러시안룰렛

import sys
input = sys.stdin.readline

def solution(bullet, a):
    bang = set([i for i in range(a if len(bullet) > a else len(bullet)) if bullet[i] == 1])
    tmp = len(bullet)
    cnt = 0
    for i in range(len(bullet)):
        if bullet[i] == 1: bang.remove(i)
        if bullet[(i + a) % tmp] == 1: bang.add((i + a) % tmp)
        if not bang: cnt += 1
    x, y = tmp, cnt
    while y != 0:
        x, y = y, y % x
    return [cnt // x, tmp // x] if cnt != 0 else [0, 0]
    
print(solution([1, 1, 0, 0, 0, 0], 2))
print(solution([1, 0, 0, 0, 0, 1], 2))
print(solution([0, 0, 0, 0, 0, 0, 0, 0, 1], 4))

# 알고리즘 : 슬라이딩 윈도우 + GCD(유클리드 호제법)
'''
풀이 : i번째 탄을 빼고 i+a번째 탄을 넣는 방식으로 범위를 오른쪽으로 1씩 옮겨가며 총알이 존재하는지 체크한다.
먼저, a가 총알 배열의 길이보다 작으면 (총알 배열의 앞에서 a개) 만큼을, 길면 (총알배열 전체)를 가져와 총알이 있는지 체크한다.
총알이 있는 인덱스를 집합자료로 저장해둔다.(bang)
0번 인덱스부터 마지막 인덱스까지 i ~ (i + a)의 범위를 한칸씩 오른쪽으로 옮겨가며 총알을 추가하고 제거한다.
현재 인덱스를 확인해 해당 인덱스가 bang에 있으면 제거하고 i + a의 인덱스를 확인해 총알이 있으면 bang에 추가한다.
i + a가 범위를 벗어날 수 있기 때문에 나머지 연산을 통해 처음으로 순환시켜주며, 총알이 없을때만 cnt에 1씩 더한다.
총알이 없는 범위의 개수를 모두 셌다면(cnt), 총알배열 길이(tmp)와의 최대공약수(x)를 구한다.
이 후, cnt // x 와 tmp // x를 반환한다.
만약 cnt가 0이면, a발의 총을 쏠 때, 어떤 경우에도 생존하지 못한다는 뜻이므로 [0, 0]을 반환한다.
'''
