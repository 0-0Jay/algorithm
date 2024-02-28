# 백준 10165번 버스 노선 : https://www.acmicpc.net/problem/10165

from collections import defaultdict, deque
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
list = []
for i in range(1, m + 1):
    a, b = map(int, input().split())
    if a > b: list.append((a, b + n, i))
    else:
        list.append((a, b, i))
        list.append((a + n, b + n, i))
        
list.sort(key = lambda x: (x[0], -x[1], x[2]))
st, ed = 0, 0
chk = set()
remove = set()
for a, b, num in list:
    if st <= a and b <= ed:
        if num in chk: chk.remove(num)
        remove.add(num)
        continue
    if num in remove: continue
    st, ed = a, b
    chk.add(num)

print(*sorted(chk))

# 알고리즘 : 스위핑
'''
풀이 : 시작점 기준으로 정렬한 뒤, 현재 범위를 벗어나는 노선이 뽑힐때마다 남길 노선에 추가한다.
입력 단계에서 시작 노선이 끝 노선보다 큰 경우, 0번 노선을 넘어가는 경우이기 때문에 +n 하여 저장한다.
위 경우를 계산에서 고려하기 시작 노선이 끝 노선보다 작은 경우는 시작과 끝 모두에 +n한 값을 한번 더 저장한다.
이 때, 두 노선이 같은 노선임을 표시하기 위해 노선 정보에 더해 노선 번호도 함께 저장한다.

이 후, 노선리스트를 시작점을 기준으로 오름차순, 끝점기준 내림차순, 번호 순으로 오름차순 정렬한다.
만약 어떤 노선 안에 포함된 노선이면 remove에 추가하여 제거된 노선 목록에 추가한다.
다음 노선이 만약 remove에서 이미 제거된 노선이면 continue로 넘어간다.
이 과정을 모든 노선에 반복하면, chk에는 남겨진 노선만 남게되므로 오름차순 정렬하여 출력한다.
'''
    
    
