# 백준 1725번 히스토그램 : https://www.acmicpc.net/problem/1725

import math
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
MAX = 1e12
n = int(input())
logn = 2 ** math.ceil(math.log2(n))
tree = [(MAX, 0) for _ in range(logn * 2 + 1)]

def query(tree, st, ed, node, left, right):  # 범위의 최소값 찾는 쿼리
    if ed < left or right < st: return (MAX, 0)
    if left <= st and ed <= right: return tree[node]
    mid = (st + ed) // 2
    l_val, l_id = query(tree, st, mid, node << 1, left, right)
    r_val, r_id = query(tree, mid + 1, ed, (node << 1) + 1, left, right)
    return (l_val, l_id) if l_val < r_val else (r_val, r_id)

def update(tree, id, val, left, right):  # 사용한 인덱스를 임의 최대값으로 업데이트
    tree[id] = (val, id - logn + 1)
    while id > 1:
        id //= 2
        l_val, l_id = tree[id * 2]
        l_val, l_id = (MAX, 0) if l_id < left else (l_val, l_id)
        r_val, r_id = tree[id * 2 + 1]
        r_val, r_id = (MAX, 0) if r_id > right else (r_val, r_id)
        tree[id] = (l_val, l_id) if l_val < r_val else (r_val, r_id)

max_area = 0
def divide(tree, st, ed):  # 최소값을 기준으로 좌우로 쪼개는 분할정복 함수
    global max_area
    if st > ed: return
    min_val, min_id = query(tree, 1, logn, 1, st, ed)
    area = min_val * (ed - st + 1)
    max_area = max(max_area, area)
    update(tree, logn + min_id - 1, MAX, st, ed)
    divide(tree, st, min_id - 1)
    divide(tree, min_id + 1, ed)

for i in range(n):
    tmp = int(input())
    update(tree, logn + i, tmp, 1, i + 1)

divide(tree, 1, n)
print(max_area)

# 알고리즘 : 세그먼트 트리 + 분할정복
'''
풀이 : 전체 범위를 최소 높이를 기준으로 양옆으로 분할 해가면서 최대 크기를 찾는다.
세그먼트 트리를 이용해 범위의 최소값과 그 인덱스를 찾는다.
최소값 * 범위를 한 값과 max_area를 비교해 더 큰값으로 max_area를 교체한다.
해당 범위에서 넓이를 구했다면, 방금 발견한 인덱스의 최소값을 임의의 최대값으로 교체하고, update 한다.
이 후, 해당 인덱스를 기준으로 왼쪽 범위와 오른쪽 범위로 분할하여 위 과정을 반복한다.
'''
