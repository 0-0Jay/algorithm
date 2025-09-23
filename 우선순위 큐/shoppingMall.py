# 백준 17612번 - 쇼핑몰 : https://www.acmicpc.net/problem/17612

import sys
input = sys.stdin.readline
import heapq as hq

n, k = map(int, input().split())
cus = [tuple(map(int, input().split())) for _ in range(n)]
in_cus = []
out_cus = []

for i in range(n):
    if len(in_cus) < k:
        hq.heappush(in_cus, (cus[i][1], i, cus[i][0]))
    else:
        now = hq.heappop(in_cus)
        hq.heappush(in_cus, (cus[i][1] + now[0], now[1], cus[i][0]))
        hq.heappush(out_cus, (now[0], -now[1], now[2]))
while in_cus:
    now = hq.heappop(in_cus)
    hq.heappush(out_cus, (now[0], -now[1], now[2]))

ans = 0
for i in range(1, n + 1):
    ans += hq.heappop(out_cus)[2] * i

print(ans)

# 알고리즘 : 우선순위 큐
'''
풀이 : 각 계산대를 우선순위 큐의 원소로 둔다.
처음에는 모든 계산대가 비어있기 때문에 손님 k명을 k개의 계산대에 넣는다(in_cus).
이 때, 각 손님은 (물건 개수, 사용중인 계산대 번호, 손님 ID) 의 형태로 넣는다.
만약 손님 수가 계산대 수보다 적다면, 그만큼만 계산대에 넣는다.

모든 손님을 넣었다면, 가장 먼저 끝나는 계산대부터 하나씩 뽑는다.
해당 계산대의 소요시간에 현재 손님의 계산 소요 시간을 더해서 다시 우선순위 큐에 넣는다.
이 때, 손님 번호를 최신화 해서 넣는다.
계산이 끝난 손님은 나가는 순서 또한 높은 번호의 계산대부터 나가기 때문에 또 다른 우선순위 큐(out_cus)에 넣는다.
이 때, STL 우선순위 큐는 최소힙이 기본이므로 계산대 번호를 음수처리 해서 넣어준다.
모든 손님에 대한 이 과정이 끝났다면, 계산대에 남아있는 손님이 있는지 확인하여 모두 빼서 out_cus에 넣어준다.

마지막으로 out_cus에서 하나씩 pop해서 ans에 누적시켜준다.
이 때, 반복문을 통해 문제에서 요구하듯 i번째 손님은 (i * 손님 ID)로 하여 ans에 누적시킨다.
'''
