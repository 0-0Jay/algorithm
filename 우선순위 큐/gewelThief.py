# 백준 1202번 보석 도둑 : https://www.acmicpc.net/problem/1202

from collections import defaultdict, deque
from functools import cmp_to_key
import heapq as hq
import math
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
gewel = [list(map(int,input().split())) for _ in range(n)]
bag = [int(input()) for _ in range(k)]
sum = 0

bag.sort()
gewel.sort(key = lambda x : x[0])
tmp = [0]
p = 0

def up(t):
    if t <= 1: return
    if tmp[t] > tmp[t // 2]:
        tmp[t], tmp[t // 2] = tmp[t // 2], tmp[t]
        up(t // 2)
    
def down(t):
    nx = t * 2
    if nx >= len(tmp): return
    if nx + 1 < len(tmp) and tmp[nx] < tmp[nx + 1]: nx += 1
    if tmp[t] < tmp[nx]:
        tmp[t], tmp[nx] = tmp[nx], tmp[t]
        down(nx)
        
for i in range(k):
    while p < n and gewel[p][0] <= bag[i]:
        tmp.append(gewel[p][1])
        up(len(tmp) - 1)
        p += 1
    if len(tmp) > 1:
        sum += tmp[1]
        tmp[1] = tmp[-1]
        tmp.pop(-1)
        down(1)
    
print(sum)

# 알고리즘 : 우선순위 큐
'''
풀이 : 보석을 무게가 작은 것부터 오름차순 정렬 후, 가치가 높은 것을 우선순위 큐로 꺼내 가방에 담는다.
gewel 배열에서 보석을 하나씩 가방의 수용 무게와 비교하며 큐에 삽입한다.
이 때, up 함수를 통해  통해 힙 정렬을 수행하며 삽입한다.
힙에서 빼낼때는 tmp[1]을 출력하고, tmp[1]을 tmp[-1]로 교체한 후, down을 통해 힙 정렬을 수행해준다.

후보 보석들을 모두 힙에 넣었고 힙에 보석이 하나라도 있다면, 힙에서 가장 가치가 비싼 보석을 꺼내어 sum에 누적한다.
이 때, tmp[1]을 꺼내고, tmp[1]을 tmp[-1]로 교체한 후, tmp에서 pop하여 힙에서 제거해준다.
'''
