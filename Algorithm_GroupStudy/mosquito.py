# 백준 20440번 니가 싫어 싫어 너무 싫어 싫어 오지 마 내게 찝쩍대지마 : https://www.acmicpc.net/problem/20440

from collections import deque
import heapq as hq
import sys
input = sys.stdin.readline

n = int(input())
mos = [list(map(int, input().split())) for _ in range(n)] # [시작, 끝]
mos.sort(key=lambda x : x[0])
que = [] # [끝, 시작]
time = [0, 0, 0]


for i in range(n):
    if len(que) > 0 and que[0][0] <= mos[i][0]:
        hq.heappop(que)
    hq.heappush(que, [mos[i][1], mos[i][0]])

    # 끝 시간이 없거나 현재 한 마리가 나가고 바로 한 마리가 들어왔다면
    if time[1] == 0 or len(que) == time[2] and time[1] == mos[i][0]:
            time[1] = que[0][0]  # 다음에 나갈 모기의 나가는 시간으로 업데이트
    
    # 만약 현재 모기 수가 저장된 최대 모기 수보다 크다면
    if len(que) > time[2]:
        time[2] = len(que)  # 최대 모기 수 업데이트
        time[0] = mos[i][0]  # 최대 모기 수 시작 시간 업데이트
        time[1] = que[0][0]  # 다음에 나갈 모기의 나가는 시간으로 업데이트

print(time[2])
print(time[0], time[1])

# 알고리즘 : 우선순위 큐
'''
풀이 : 모기 수가 저장된 최대 모기 수보다 클 때만 시작 시간을 업데이트하고, 같을 때는 끝 시간을 업데이트한다.
모기 수는 모기가 나갈 때까지 계속 쌓이기 때문에 모기가 나가는 시간을 기준으로 우선순위 큐를 사용하고,
모기는 들어오는 시간을 기준으로 오름차순 정렬하여 가장 빨리 들어오는 모기부터 탐색한다.
만약 현재 모기가 다음에 나갈 모기(큐의 front)가 나가는 시간보다 앞이라면 큐에서 모기를 뺀다.

저장된 나간 시간이 없거나, 모기 수의 변화가 없고 현재 모기가 들어온 시간이 저장된 나간 시간과 같다면,
다음에 나갈 모기의 나가는 시간으로 업데이트한다.
현재 모기가 들어온 시간이 저장된 나간 시간과 같은 것은 있던 모기 하나가 나가고 현재 모기가 들어왔다는 의미다.
그러므로 다음에 나갈 모기가 나갈 때까지 시간 범위를 늘려주어야 한다.

만약 모기가 더 들어와 저장된 최대 모기 수보다 많아지면, 다음과 같이 업데이트 해준다.
최대 모기 수의 시작 시간 -> 현재 모기 수가 들어온 시간
최대 모기 수의 끝 시간 -> 다음에 나갈 모기가 나가는 시간
'''
