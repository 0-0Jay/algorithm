# 백준 1525번 퍼즐 : https://www.acmicpc.net/problem/1525

from collections import defaultdict, deque
import heapq as hq
import math
import sys
input = sys.stdin.readline

sz = 500009  # 임의의 적당한 크기의 소수
z = 0  # 0의 위치(1의 위치)
arr = []
for i in range(3):
    tmp = list(map(int, input().split()))
    for j in range(3):
        arr.append(tmp[j] + 1)  # 0의 처리를 간편화하기위해 모든 값에 +1해주고, 0을 1로 처리
        if tmp[j] == 0:
            z = i * 3 + j
            
def makeKey(arr):  # 키 값으로 쓰기위해 배열을 9자리 숫자로 변환하는 함수
    key = 0
    for i in range(9):
        key = key * 10 + arr[i]
    return key

que = deque()
chk = [[] for _ in range(sz)]
key = makeKey(arr)
chk[key % sz].append(key)
que.append((key, z, 0))
dt = [-1, 1, -3, 3]
res = -1
while que:
    now, zr, cnt = que.popleft()
    
    if now == 234567891:
        res = cnt
        break
    
    lst = list(map(int, list(str(now))))
    for i in range(4):
        if zr % 3 == 0 and i == 0: continue  # 줄이 바뀌는 경우 배제
        if zr % 3 == 2 and i == 1: continue
        nx = zr + dt[i]
        if 0 <= nx < 9:
            lst[nx], lst[zr] = lst[zr], lst[nx]
            key = makeKey(lst)  # 배열이 아닌 숫자로 컨트롤
            if key not in chk[key % sz]:
                que.append((key, nx, cnt + 1))
                chk[key % sz].append(key)
            lst[nx], lst[zr] = lst[zr], lst[nx]

print(res)

# 알고리즘 : 해싱 + BFS
'''
풀이 : 3 x 3의 숫자 배치 정보를 1차원 배열로 바꾸고, 이를 숫자로 치환하면서 컨트롤한다.
3 x 3의 입력을 arr에 1차원으로 바꾸어 저장한다.
상하좌우와 교체하는 작업은 1차원에서 -1, 1, -3, 3의 인덱스와 교체하는 것과 같다.
단, 이떄 좌우의 교체과정에서 줄바꿈이 일어나는 경우는 배제해야 한다.

이 문제는 메모리가 32mb 밖에 주어지지 않으므로 9자리의 체크배열을 사용할 수 없다.
따라서 해싱을 이용한 중복체크 방식을 사용한다.
BFS를 수행할 때도 배열이 아닌, 9자리 숫자로 치환하여 메모리를 절약한다.
초기에 모든 자리에 +1한 값으로 시작하기 때문에 now가 234567891이면 BFS를 중단한다.
'''
