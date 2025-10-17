# 백준 1700번 멀티탭 스케줄링 : https://www.acmicpc.net/problem/1700

from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))
chk = [deque() for _ in range(k + 1)]  # 남은 사용 스케줄
nx = [0] * (k + 1)  # 다음 사용 스케줄
mult = set()  # 멀티탭 현황
cnt = 0
fid = 0

for i in range(k):
    chk[arr[i]].append(i)
    
for i in arr:
    chk[i].popleft()
    if len(mult) == n:
        if i not in mult:
            cnt += 1
            mult.remove(fid)
            nx[fid] = 0
    mult.add(i)
    nx[i] = chk[i][0] if chk[i] else 110
    fid = nx.index(max(nx))
         
print(cnt)

# 알고리즘 : 그리디
'''
풀이 : 멀티탭에 빈 칸이 없는 경우, 가장 나중에 스케줄이 잡혀있는 전기용품의 플러그를 교체한다.
mult(멀티탭)를 set로 두어, 이번에 사용하는 전기용품이 이미 멀티탭에 꽂혀있다면 add가 발생하지 않게했다.
처음 arr을 입력 받을 때, chk배열의 원소를 deque로 만들어, 스케줄을 popleft하는 방식으로 꺼내오게 했다.
즉, 이번에 사용하는 전기용품이 2라면 chk[2]에서 popleft한다.
이러면 2번 전기용품의 다음 스케줄은 자연스럽게 chk[2]의 0번 인덱스가 된다.
단, popleft한 스케줄이 마지막일 경우 deque가 비게 되는데, 이 때는 nx에 110(범위 밖 최대값)을 주어 다음 교체 시 반드시 교체되게 한다.

만약 멀티탭의 모든 칸이 사용중이며 현재 사용할 전기용품이 멀티탭에 꽂혀있지 않다면 교체작업을 수행한다.
교체 횟수(cnt)를 +1 해주고, mult에서 fid를 제거하면서 nx[fid]를 0으로 초기화 한다.

이 때, fid는 다음 사용 스케줄을 저장하는 nx에서 가장 나중에 수행하는 전기용품의 id다.
이를위해 max(nx)와 index 함수를 사용해 계산한다.
'''
