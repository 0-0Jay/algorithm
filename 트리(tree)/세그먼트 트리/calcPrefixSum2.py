# 백준 10999번 구간 합 구하기2 : https://www.acmicpc.net/problem/10999

import math
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n, m, k = map(int, input().split())
logn = 1 << (math.ceil(math.log2(n)) + 1)
arr = [0] + [int(input()) for _ in range(n)]
tree = [0] * (logn + 1)
lazy = [0] * (logn + 1)

def seg(st, ed, node):
    if st == ed:
        tree[node] = arr[st]
        return tree[node]
    mid = (st + ed) // 2
    tree[node] = seg(st, mid, node << 1) + seg(mid + 1, ed, (node << 1) + 1)
    return tree[node]

def query(st, ed, node, left, right):
    calc_lazy(st, ed, node)
    if left > ed or right < st: return 0
    if left <= st and ed <= right: return tree[node]
    mid = (st + ed) // 2
    return query(st, mid, node << 1, left, right) + query(mid + 1, ed, (node << 1) + 1, left, right)

def update(st, ed, node, left, right, val):
    calc_lazy(st, ed, node)
    if left > ed or right < st: return tree[node]
    if left <= st and ed <= right:
        tree[node] += (ed - st + 1) * val
        if st != ed:
            lazy[node << 1] += val
            lazy[(node << 1) + 1] += val
        return tree[node]
    mid = (st + ed) // 2
    tree[node] = update(st, mid, node << 1, left, right, val) + update(mid + 1, ed, (node << 1) + 1, left, right, val)
    return tree[node]

def calc_lazy(st, ed, node):
    if lazy[node] != 0:
        tree[node] += lazy[node] * (ed - st + 1)
        if st != ed:
            lazy[node << 1] += lazy[node]
            lazy[(node << 1) + 1] += lazy[node]
        lazy[node] = 0
    
seg(1, n, 1)
for _ in range(m + k):
    cmd = tuple(map(int, input().split()))
    if cmd[0] == 1:
        update(1, n, 1, cmd[1], cmd[2], cmd[3])
    else:
        print(query(1, n, 1, cmd[1], cmd[2]))
    
# 알고리즘 : 느리게 갱신되는 세그먼트 트리
'''
풀이 : 각 노드에 갱신 내용을 기록만 해두고, 실질적으로 해당 노드에 접근하면 한 번에 계산한다. 
기본 구현의 틀은 일반적인 세그먼트 트리와 같다.
단, 세그먼트 트리와 같은 크기의 lazy 트리를 하나 더 생성한다.
lazy 트리는 갱신 내용을 모아서 한 번에 처리하기 위해 갱신 값을 누적시켜두는 트리다.

느리게 갱신되는 세그먼트 트리의 기본 원리는 다음과 같다.
1. 구하려는 범위 안에 현재 노드가 가진 범위가 포함된다면, 구간합을 미리 계산해 반환한다.
2. lazy 트리에서 현재 노드의 자식노드에 갱신 값을 기록만 해두고 빠져나온다.(탐색하지 않는다.)
3. 만약 lazy트리에서 현재 노드에 갱신 값이 있다면, 갱신값을 반영 함과 동시에 2번을 한 번 수행한다.

update 또는 query 함수가 실행될때 마다 calc_lazy 함수를 통해 lazy 트리를 검사한다.
만약 lazy 트리에 갱신값이 있다면, 현재 노드의 범위만큼 lazy 값을 곱하여 현재 노드에 추가한다.
 -> 현재 노드가 1~3번의 구간합을 가지고 있다면, 1~3이 3개의 노드를 포함하므로 * 3을 해주는 것이다.
query 함수의 경우 calc_lazy를 적용한 후 현재 노드의 값을 반환하면 된다.
update 함수의 경우 calc_lazy를 적용한 후에, 현재 노드의 값에 갱신 과정을 한 번 더 수행해준다.

매 탐색/갱신 마다 기존 세그먼트 트리처럼 리프 노드까지 이동하지 않고, 최소한의 깊이에서 계산한다.
최악의 경우 일반 세그먼트 트리 O(n* n * logn)이 걸리지만, 이 세그먼트 트리는 O(n * logn)으로 더 효율적이다.
'''
