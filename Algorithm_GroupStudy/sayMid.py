# 백준 1655번 가운데를 말해요 : https://www.acmicpc.net/problem/1655

from collections import deque
import heapq as hq
import sys
input = sys.stdin.readline

left = []
right = []
n = int(input())
mid = int(input())
print(mid)
for i in range(n - 1):
    tmp = int(input())
    lm, rm = min(tmp, mid), max(tmp, mid)
    hq.heappush(left, -lm)
    hq.heappush(right, rm)

    if len(left) >= len(right):
        mid = -hq.heappop(left)
    else:
        mid = hq.heappop(right)
    print(mid)

# 알고리즘 : 우선순위 큐
'''
풀이 : 왼쪽과 오른쪽에 우선순위 큐를 사용해서 삽입하고, 가운데값을 최신화 해주면서 진행한다.
left는 최대값을 뽑는 heap, right는 최소값을 뽑는 heap으로 둔다.
매번 값을 받으면, 현재 mid값과 비교하여 lm과 rm을 교체하고, 각각 left와 right에 삽입한다.
만약 left의 길이가 right의 길이보다 크거나 같으면 left에서 꺼낸 값을, 작으면 right에서 꺼낸 값을 mid와 교체한다.

input = sys.stdin.readline을 반드시 사용해야 하는 문제다.
한줄씩 여러번 입력을 받는 문제에서 그냥 input을 사용하면 같은 로직이어도 시간초과가 발생한다.
'''
