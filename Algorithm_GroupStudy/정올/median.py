# 정올 - 중앙값 : https://jungol.co.kr/problem/1570?cursor=MTAsMiw1

import heapq as hq
import sys
input = sys.stdin.readline

n = int(input())
left, right = [], []

for _ in range(n // 2 + 1):
    tmp = list(map(int, input().split()))
    for i in tmp:
        if not left or i <= -left[0]:
            hq.heappush(left, -i)
        else:
            hq.heappush(right, i)

        if len(left) > len(right) + 1:
            hq.heappush(right, -hq.heappop(left))
        elif len(right) > len(left):
            hq.heappush(left, -hq.heappop(right))
    
    print(-left[0])

# 알고리즘 : 힙
'''
풀이 : 최대힙 큐와 최소힙 큐를 사용해 중앙값을 찾는다.
먼저 최대힙과 최소힙을 하나씩 만든다.(left, right)

문젱에서 첫 숫자는 1개고 그 이후부터는 2개씩 주기 때문에 반복을 (숫자의 수 // 2 + 1)만큼만 실행한다.
숫자를 하나씩 뽑아서 최대힙의 top과 비교한다.
만약 최대힙이 비어있거나 top의 숫자보다 작으면, 최대힙에 넣는다.
그렇지 않으면 최소힙에 넣는다.

매 반복마다 최대힙과 최소힙의 길이를 비슷하게 맞춰준다.
최대힙의 길이가 최소힙의 길이 + 1이 되게끔 해야한다.
매번 숫자가 2개씩 들어오기 때문에 2개가 전부 한쪽 힙에 들어가면 하나를 빼서 반대쪽 힙에 넣는 과정 1회만 실시하면 된다.
최대힙의 top을 꺼내면 항상 중앙값이 된다.

이 때, 파이썬에서 기본제공하는 heapq는 최소힙이기 때문에, 최대힙에 수를 컨트롤할때, 음수처리하여 활용한다.
'''
