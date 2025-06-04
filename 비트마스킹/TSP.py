# 백준 2098번 외판원 순회 : https://www.acmicpc.net/problem/2098

import sys
input = sys.stdin.readline

n = int(input())
city = [list(map(int, input().split())) for _ in range(n)]
chk = [[0] * (1 << n) for _ in range(n + 1)]
all_visited = (1 << n) - 1

def DFS(node, bit):
    global chk
    if bit == all_visited:
        if city[node][0] > 0: return city[node][0]
        else: return 1e12
    if chk[node][bit] != 0: return chk[node][bit]
    min_cost = 1e12
    for i in range(n):
        if city[node][i] == 0 or bit & (1 << i) != 0: continue
        min_cost = min(DFS(i, bit | (1 << i)) + city[node][i], min_cost)
    chk[node][bit] = min_cost
    return chk[node][bit]
        
print(DFS(0, 1))

# 알고리즘 : 비트마스킹 + 메모이제이션 (TSP : Traveling Salesman Problem)
'''
풀이 : 방문한 도시를 비트마스킹하며 DFS 순회한다. 비트마스킹한 도시들에 대한 비용을 메모이제이션 한다.
외판원이 모든 도시를 순회해서 시작점으로 돌아온다는 것은 어느 도시에서 출발하던 순회가 가능하다는 뜻이다.
따라서 임의로 0번 도시에서 출발해도 무관한다.

DFS를 돌면서 다음 도시로 이동할 때마다 해당 도시의 번호를 비트마스킹 한다.
같은 도시를 순회했다면 다시 탐색하지 않도록 chk배열에 이 비트 정보를 인덱스로 사용해 비용을 기록한다.
만약 모든 비트가 1이라면, 모든 도시를 순회했다는 뜻이므로 해당 도시에서 0번 도시로 가는 길이 있는지 탐색한다.
길이 있으면 0번 도시로 가는 비용을 없으면 임의 최대값을 리턴한다.
현재 노드까지 오는 길 중 최소 값만 활용하기 때문에, 0번 도시로 돌아왔을 때, 반환되는 값이 최소 비용 경로이다.
이 때, min_cost를 최대값으로 시작하기 때문에 중간에 루트가 끊기면 자연스럽게 최소값 계산에서 배제된다
'''
