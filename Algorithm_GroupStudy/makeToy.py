# 백준 2637번 장난감 조립 : https://www.acmicpc.net/problem/2637

from collections import defaultdict, deque
import heapq as hq
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]  # 부품 간선 정보
chk = [0] * (n + 1)  # 하위 노드 갯수 체크
base = [{} for _ in range(n + 1)]  # 기본 부품 갯수 체크
que = deque()

for i in range(m):  # 부품 간선 정보 및 각 노드별 하위 노드 갯수 체크
    x, y, k = map(int, input().split())
    graph[y].append((x, k))
    chk[x] += 1
    
for i in range(1, n + 1):  # 하위 노드가 없는 노드 큐에 삽입
    if chk[i] == 0:
        que.append(i)
        base[i][i] = 1  # 하위 노드가 없으면 기본 부품이므로 base에 초기값 지정
        
while que:
    now = que.popleft()
    
    for nx, k in graph[now]:
        chk[nx] -= 1
        if now not in base[nx]:
            for key, val in base[now].items():  # 현재 부품에 들어가는 기본 부품의 k배수를 상위 부품에 누적
                if key not in base[nx]:
                    base[nx][key] = val * k
                else:
                    base[nx][key] += val * k
        if chk[nx] == 0:
            que.append(nx)
            
for k, v in sorted(base[n].items()):
    print(k, v)

# 알고리즘 : 위상 정렬
'''
풀이 : 위상 정렬을 통해 각 부품별 상하관계를 정리해두고, 하위부품에 들어가는 기본 부품을 상위부품에 누적시킨다.
기본 부품을 계산에 활용하기 위해 base에 기본 부품하나를 만드는데 해당 부품 하나를 쓴다라는 의미로 1을 저장한다.
하위 노드가 없는 부품들을 큐에 넣고, 하나씩 빼면서 해당 부품을 필요로하는 상위 부품을 계산한다.
상위 부품이 원하는 하위 부품의 갯수만큼 하위 부품이 가진 기본 부품의 개수의 배수를 누적시킨다.

예를 들면 다음과 같다.
ex ) 3을 만드는데 2가 2개가 들고, 2를 만드는데 1이 3개가 들어가는 경우
2 -> '1' * 3  -> 2는 기본 부품 1을 3개 가지고 있음
3 -> 2 * ('1' * 3) -> 3은 2가 가진 기본 부품 1 3개를 2배수 가짐

이를 n이 큐에서 나올 때까지 반복하면, base[n]에는 총 필요한 기본부품의 종류별 개수가 저장된다. 
'''
