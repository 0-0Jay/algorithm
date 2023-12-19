# 백준 16437번 양 구출작전 : https://www.acmicpc.net/problem/16437

from collections import deque
import heapq as hq
import sys
input = sys.stdin.readline

n = int(input())
arr = [[] for _ in range(n + 1)]
node = [0] * (n + 1)
que = deque()

for i in range(2, n + 1):
    t, a, p = input().split()
    if t == 'S' : arr[i] = [int(p), int(a)]
    else: arr[i] = [int(p), -int(a)]
    node[int(p)] += 1
    
arr[1] = [0, 0]  # 1번 인덱스에 구출한 양 저장
        
for i in range(1, n + 1):
    if node[i] == 0:
        que.append((i, arr[i][1]))

while que:
    now, cnt = que.popleft()
        
    if cnt > 0 and arr[arr[now][0]]:  # 양의 수가 양수일 때만 다음 노드에 합산. 늑대를 올릴 수 없기 때문
        arr[arr[now][0]][1] += cnt

    node[arr[now][0]] -= 1  # 노드 연결 끊기

    if node[arr[now][0]] == 0:  # 하위 노드가 없을 때만 큐에 삽입
        que.append((arr[now][0], arr[arr[now][0]][1]))
        
print(arr[1][1])

# 알고리즘 : 방향 비순환 그래프
'''
풀이 : 각 노드 별로 연결된 하위 노드의 양 마릿수를 총합해 상위 노드로 보낸다.
노드 정보를 입력받을 때 양이면 양수, 늑대면 음수로 값을 저장한다.
연결한 노드 p에 연결된 노드가 있음을 표시하기 위해 +1해준다.
즉, node[p]에는 연결되어 있는 하위 노드의 수가 저장된다.
arr[1]에는 1번 노드로 오는 모든 양의 수를 저장하기 위해 [0, 0]으로 임의로 초기화 한다.

node 배열을 돌면서 연결된 하위 노드의 수가 0인 노드들을 큐에 담는다.
하위 노드의 수가 0이라는 것은 가장 깊은 노드라는 뜻이다.

큐를 돌면서 현재 노드와 노드에 저장된 양의 수를 가져와 연결된 다음 노드와 합한다.
이 때, 현재 노드에 저장된 양의 수가 0또는 음수라면, 현재 노드에 늑대가 있으며 모든 양을 잡아먹었다는 뜻이다.
따라서 양의 수가 양수일때만 다음 노드의 양의 수에 현재 양의 수를 합산해주고, 그 외에는 연결만 끊어준다.
다음 노드에 연결된 하위 노드가 모두 탐색되었다면 큐에 넣는다.

모든 노드를 탐색하면, 1번 노드의 1번 인덱스가 곧 구출한 양의 수다.
'''
