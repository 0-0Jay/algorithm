# 백준 17435번 합성함수와 쿼리 : https://www.acmicpc.net/problem/17435

import math
import sys
input = sys.stdin.readline

m = int(input())
arr = [0] + list(map(int, input().split()))
q = int(input())
query = []
maxn = 0
for _ in range(q):
    n, x = map(int, input().split())
    maxn = max(maxn, n)
    query.append((n, x))
    
logn = math.ceil(math.log2(maxn)) + 1
parent = [[0] * (m + 1) for _ in range(logn)]
for i in range(1, m + 1):
    parent[0][i] = arr[i]

for i in range(logn - 1):
    for j in range(1, m + 1):
        parent[i + 1][j] = parent[i][parent[i][j]]
        
for n, x in query:       
    for i in range(logn):
        if 1 << i > n: break
        if n & (1 << i):
            x = parent[i][x]
    print(x)

# 알고리즘 : 희소 배열 (sparse table)
'''
풀이 : 쿼리에서 가장 큰 n을 찾고, 해당 n에 log2를 취한 값까지 희소배열을 만든다.
희소 배열의 특성상 2의 제곱수 만큼 연결된 노드로 이동하기 때문에 log2(n)만큼의 범위로도 찾을 수 있다.
1을 i씩 왼쪽 시프트 해주면서 n과 값을 비교하고, 값이 같을 때마다 x를 parent[i][x] 값으로 갱신시킨다.
예를 들어, n이 10이라면, x가 i가 1일 때와 3일 때 한 번 씩 갱신된다.
만약 1 << i가 n보다 커지면, 당연히 & 연산의 값이 0일 것이기 때문에 break를 통해 불필요한 탐색을 방지한다.
'''
