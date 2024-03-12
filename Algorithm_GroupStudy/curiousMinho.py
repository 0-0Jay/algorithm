백준 1507번 궁금한 민호 : https://www.acmicpc.net/problem/1507

import sys
input = sys.stdin.readline

n = int(input())
city = [list(map(int, input().split())) for _ in range(n)]
use = [[1] * n for _ in range(n)]
roads = 0
    
for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == k or k == j or i == j: continue
            if city[i][j] > city[i][k] + city[k][j]:
                print(-1)
                exit(0)
            if city[i][j] == city[i][k] + city[k][j]:
                use[i][j] = 0

for i in range(n):
    for j in range(n):
        if use[i][j] == 1:
            roads += city[i][j]
            use[i][j] = 0
            use[j][i] = 0
                
print(roads)

# 알고리즘 : 플로이드-워셜
'''
풀이 : 이미 최소값으로만 간선이 연결되어 있기 때문에, 같은 비용의 간선을 찾는다.
i도시에서 j도시로 이동하는 시간과 i도시에서 k도시를 경유하여 j도시로 이동하는 시간이 같다면, i-j도로는 제거해도 무관하다.
따라서 use 배열을 따로 두고, 이 도로를 0으로 체크하여 제거해준다.

단, 도로를 제거할 때 i-j쌍이 자기자신을 가르키는 경우는 계산 시에 오류를 발생시킨다.
예를 들어 1 -> 2의 비용은 플로이드-워셜의 계산과정 상에서 1 -> 1 -> 2 의 비용과 같기 때문에 1 -> 2를 제거해버린다.
따라서 모든 경로가 다른 경우로 예외처리를 해주어야한다.

모든 탐색이 끝났다면, 전체 city 배열을 탐색하여 사용하고 있는 도로의 시간을 roads에 누적해준다.
이 때, 중복 계산되지 않도록 한번 사용한 i-j쌍은 양방향에서 0으로 체크해준다.
'''
