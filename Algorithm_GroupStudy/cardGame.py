# 백준 16566번 카드 게임 : https://www.acmicpc.net/problem/16566

from collections import deque
import heapq as hq
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
card = list(map(int, input().split()))
cs = list(map(int, input().split()))
chk = set()
card.sort()

for i in cs:
    l, r = 0, len(card) - 1
    while l <= r:
        mid = (l + r) // 2
        if i >= card[mid]:
            l = mid + 1
        else:
            r = mid - 1
    if card[l] in chk:
        for j in range(l + 1, m):
            if card[j] not in chk:
                print(card[j])
                chk.add(card[j])
                break
    else:
        print(card[l])
        chk.add(card[l])

# 알고리즘 : 이분 탐색
'''
풀이 : 이분 탐색을 응용해 철수의 카드보다 큰 가장 작은 카드를 찾아서 출력한다.
이분탐색을 위해 사전에 민수가 가진 카드는 오름차순 정렬해둔다.

현재 수보다 큰 가장 작은 수를 찾는 이분탐색은 다음과 같이 수정한다.
1. 이분 탐색의 while문을 l < r에서 l <= r로 바꾸어 만약 l과 r이 같아지더라도 한번 더 수행하게 설정한다.
2. mid를 설정할때도 card[mid]가 i와 같을 때 l을 한번 더 올리도록 설정한다.
3. 출력은 l을 출력한다.

카드를 낼 때 이전에 낸 적이 없으면 그 카드를 출력하고, chk에 중복체크를 해준다.
만약 뽑은 카드(l)가 chk에 있으면 이전에 냈던 카드이므로 for문을 통해 바로 다음 카드를 꺼내며 체크해준다.
for문을 돌다가 낸적없는 카드가 나오면 그 카드를 출력하고, chk에 중복체크를 해준다.
'''
