# 백준 21939번 문제 추천 시스템 Version1 : https://www.acmicpc.net/problem/21939

from collections import defaultdict, deque
import heapq as hq
import sys
input = sys.stdin.readline

n = int(input())
easy = []
hard = []
lst = {}  # 실제 문제 리스트
for _ in range(n):
    p, l = map(int, input().split())
    lst[str(p)] = str(l)
    hq.heappush(easy, [l, p])
    hq.heappush(hard, [-l, -p])
    
m = int(input())
chk = {} # 푼 문제 리스트
for _ in range(m):
    com = list(input().split())
    if com[0] == 'add':  # 추가면 각 힙에 맞게 추가하고 리스트에도 추가
        hq.heappush(easy, [int(com[2]), int(com[1])])
        hq.heappush(hard, [-int(com[2]), -int(com[1])])
        lst[com[1]] = com[2]
    elif com[0] == 'recommend':  # 추천이면 1이면 hard에서 아니면 easy에서 0번 인덱스 추천.
        if com[1] == '1':
            while str(-hard[0][1]) in chk and chk[str(-hard[0][1])] == str(-hard[0][0]):  # 만약 chk에 푼 이력이 있으면서 난이도도 같으면
                hq.heappop(hard)
            print(-hard[0][1])
        else:
            while str(easy[0][1]) in chk and chk[str(easy[0][1])] == str(easy[0][0]):
                hq.heappop(easy)
            print(easy[0][1])
    else:  # 풀었으면 chk에 푼 이력 기록
        chk[com[1]] = lst[com[1]]
        del lst[com[1]]

# 알고리즘 : 구현 + 우선순위 큐
'''
풀이 : 난이도와 번호를 묶어서 문제를 컨트롤 한다.
add 명령어일 경우 lst에도 해당 문제 번호와 난이도를 기록하여 나중에 solved 명령어에서 사용한다.
-> chk에 푼 문제를 기록할 때 lst에 있는 난이도를 불러와 저장한다.
chk를 비교하여 난이도까지 포함해 푼 문제 체크를 할 수 있다.
recommend는 리스트에 들어있는 문제만 추천하기 때문에 이미 푼문제를 chk 딕셔너리에서 확인한다.
풀었던 문제가 다시 들어오는 경우가 있기 때문에 난이도 체크까지 함께 수행해야 한다.
chk에 만약 문제 번호가 같으면서 문제 난이도까지 같다면 해당 문제를 pop으로 빼낸다.
이 과정을 푼 문제가 없을 때까지 반복한다.
만약 del 함수를 용해 heap에서 바로 제거하려 한다면, heap이 커질수록 문제 탐색시간이 매우 늘어날 것이라고 생각해 이 방법을 사용했다.
'''
