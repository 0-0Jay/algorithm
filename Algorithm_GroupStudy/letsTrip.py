# 백준 1976번 여행 가자 : https://www.acmicpc.net/problem/1976

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
route = []
for i in range(1, n + 1):
    tmp = [0] + list(map(int, input().split()))
    for j in range(1, n + 1):
        if tmp[j] == 1:
            route.append([i, j])
plan = list(map(int, input().split()))

parent = [i for i in range(n + 1)]
def union(parent, a, b):
    rootA = find(parent, a)
    rootB = find(parent, b)
    
    if rootA < rootB:
        parent[rootB] = rootA
    else:
        parent[rootA] = rootB

def find(parent, x):
    if parent[x] == x:
        return x
    parent[x] = find(parent, parent[x])
    return parent[x]

for a, b in route:
    if find(parent, a) != find(parent, b):
        union(parent, a, b)

ans = "YES"
p = find(parent, plan[0])
for i in range(1, m):
    if p != find(parent, plan[i]):
        ans = "NO"
        break
print(ans)

# 알고리즘 : union/find
'''
풀이 : 입력받을 때, 값이 1이면 두 노드 쌍을 route에 저장하고, route를 탐색하며 union함수로 연결한다.
모든 연결이 끝난 후에, plan의 첫번째 도시의 부모 노드를 find를 통해 구한다.

이 때, parent에서 직접 값을 가져오면 안되고 반드시 find를 통해 값을 가져와야 한다.
그 이유는 예를 들면 다음과 같다.
2과 4가 union하게 되면 4의 parent는 2로 기록된다.
그러나 1이 2와 union 할 경우, 2의 parent는 1로 갱신되지만 4의 parent는 1로 갱신되지 않는다.
따라서 모든 연결이 끝난 후에 find 함수를 통해 최종 루트 노드를 찾아야 한다.

한 번이라도 루트노드가 하위 노드가 있다면 NO를 출력하고, 아니면 YES를 출력한다.
'''
