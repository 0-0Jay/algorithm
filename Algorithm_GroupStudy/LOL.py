# 백준 23059번 리그 오브 레게노 : https://www.acmicpc.net/problem/23059

from collections import defaultdict, deque, OrderedDict
import heapq as hq
import sys
input = sys.stdin.readline

n = int(input())
graph = defaultdict(list)
bef = {}
for _ in range(n):
    a, b = input().strip().split(" ")
    graph[a].append(b)
    if b not in bef: bef[b] = 0
    if a not in bef: bef[a] = 0
    bef[b] += 1
 
que = []
items = list(bef.items())
for k, v in items:
    if v == 0:
        hq.heappush(que, (0, k))
        del bef[k]
        
result = []
while que:
    cnt, now = hq.heappop(que)
    result.append((cnt, now))
    for nx in graph[now]:
        bef[nx] -= 1
        if bef[nx] == 0:
            hq.heappush(que, (cnt + 1, nx))
            del bef[nx]
            
if len(bef) == 0:
    result.sort(key = lambda x: (x[0], x[1]))
    for i in result:
        print(i[1])
else:
    print(-1)
    
# 알고리즘 : 위상 정렬 + 해시
'''
풀이 : 해시 자료구조(딕셔너리)를 이용해 그래프 구조를 만들고, 아이템 별로 선행 구매 아이템 개수를 저장한다.
이 문제는 단순히 위상정렬을 그대로 사용하면 안되는 문제다.
문제에서 주어진 아이템 구매 순서에 따라 아이템 구매를 회차 별로 따로 생각해야 한다.
이를 위해 que에 값을 삽입할 때, (회차, 아이템)의 튜플 쌍으로 삽입한다.
bef를 탐색하면서 value가 0이면 que에 넣고, bef에서 key값을 제거해준다.

일반적인 위상정렬과 같이 que가 빌 때까지 진행한다.
que에서 뽑으면 result에 뽑힌 아이템을 저장한다.
뽑은 아이템을 구매한 후에 구매할 수 있는 아이템을 bef에서 찾아 value에 -1해준다.
만약 value가 0이되면, 처음 단계와 같이 que에 삽입하고 bef에서 삭제한다.

위상 정렬을 위한 que 탐색이 끝났을 때, bef에 값이 남아 있다면, 구매할 수 없는 아이템이 존재한다는 의미다.
따라서 bef의 크기가 0일 때만 result를 회차 순으로 오름차순, 같은 회차라면 아이템 이름을 사전순으로 오름차순 정렬한다.
정렬된 result에서 순차적으로 아이템 이름만 출력한다.
'''
