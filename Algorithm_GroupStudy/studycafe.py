# 백준 28284번 스터디 카페 : https://www.acmicpc.net/problem/28284

from collections import defaultdict, deque
import heapq as hq
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
cost = list(map(int, input().split()))
cost.sort()
left = [0]
right = [0]
for i in range(len(cost)):
    left.append(cost[i] + left[i])
    right.append(cost[-i - 1] + right[i])

dict = defaultdict(int)
for i in range(m):
    a, b = map(int, input().split())
    dict[a] += 1
    dict[b + 1] -= 1

tmp = 0
key = sorted(dict.keys())
answer = [0, 0]
for i in range(len(key) - 1):
    tmp += dict[key[i]]
    if tmp <= 0: continue
    answer[0] += (key[i + 1] - key[i]) * left[tmp]
    answer[1] += (key[i + 1] - key[i]) * right[tmp]
    
print(*answer)

# 알고리즘 : 좌표 압축 + 누적합
'''
풀이 : 미리 좌석 요금의 최대 누적합과 최소 누적합을 구해놓고, 딕셔너리를 활용한 좌표 압축으로 계산한다.
left와 right에 각각 최소 누적합과 최대 누적합을 계산해둔다.
딕셔너리에 값을 받을때마다 이용 시작 일자에 +1, 이용 종료일자 다음날에 -1을 누적시킨다.
이를 통해 실제 이용자 수가 변하는 일자만 딕셔너리에 저장되므로 좌표 압축이 이루어진다.

이 후, 딕셔너리의 키값(이용자 수가 변하는 일자)을 오름차순 정렬한뒤 순서대로 tmp에 누적해준다.
만약 해당 일자에 사람이 더 들어왔다면 tmp의 값이 증가할 것이고, 사람이 나갔다면 tmp의 값이 감소할 것이다.
이 tmp를 인덱서로 사용해 left와 right에 미리 저장해둔 누적합을 가져와 다음일자 - 현재일자 만큼 곱한다.
left의 값을 곱하여 누적한 값은 최소 수익, right의 값을 곱하여 누적한 값은 최대 수익이 된다.
'''
