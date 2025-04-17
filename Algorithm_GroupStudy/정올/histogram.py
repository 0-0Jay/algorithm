# 정올 - 히스토그램 : https://jungol.co.kr/problem/1214?page=1&sid=10705483&cursor=OCwxLDQ%3D

import math
import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

hist = list(map(int, input().split()))
segtree = [0] * (((2 ** (math.ceil(math.log2(hist[0])))) << 1) + 1)

def seg(st, ed, node):
    if st == ed:
        segtree[node] = [hist[st], st]
        return segtree[node]
    mid = (st + ed) // 2
    left = seg(st, mid, node << 1)
    right = seg(mid + 1, ed, (node << 1) + 1)
    segtree[node] = left if left[0] <= right[0] else right
    return segtree[node]

def min_val(st, ed, node, l, r):
    if st > r or ed < l: return [1e12, 0]
    if l <= st and r >= ed: return segtree[node]
    mid = (st + ed) // 2
    left = min_val(st, mid, node << 1, l, r)
    right = min_val(mid + 1, ed, (node << 1) + 1, l, r)
    return left if left[0] <= right[0] else right

def histogram(st, ed):
    global hist
    if ed == st: return hist[st]
    if ed < st: return 0
    val, id = min_val(1, hist[0], 1, st, ed)
    now_width = val * (ed - st + 1)
    return max(now_width, histogram(st, id - 1), histogram(id + 1, ed))

seg(1, hist[0], 1)
print(histogram(1, hist[0]))

# 알고리즘 : 세그먼트 트리 + 분할정복
'''
풀이 : 세그먼트 트리로 구간내 최소값을 logN으로 탐색하고, 분할정복을 통해 최대 넓이를 찾아낸다.
가장 큰 직사각형을 찾기 위해 다음 방식으로 진행한다.
1. 현재 범위에서 가장 낮은 높이와 그 위치를 찾는다.
2. (현재 범위 길이 * 가장 낮은 높이)로 직사각형의 넓이를 구하고, 이 값과 다음 값을 비교한다.
  2-1. 가장 낮은 높이 왼쪽 범위에서 구해진 직사각형의 넓이
  2-2. 가장 낮은 높이 오른쪽 범위에서 구해진 직사각형의 넓이
3. 왼쪽과 오른쪽 넓이는 마찬가지로 1-2의 과정을 반복한다.

위 방식대로 진행하려면 가장 중요한 것이 가장 낮은 높이를 찾는 것이다.
가장 낮은 높이를 찾기위해 단순 반복문을 통해 n의 시간을 사용하게 되면, 최악의 경우 O(n^2)만큼 탐색하게 된다.
따라서 특정 범위 내에 특정 값을 구하는데 O(logn)을 사용하는 세그먼트 트리를 활용한다.
세그먼트 트리는 구간 최소값 트리로 구현하고, [높이, 인덱스] 쌍으로 트리에 저장한다.

먼저 1번 인덱스부터 n번 인덱스 까지 전체범위로 시작한다.
이 범위에서 가장 낮은 높이를 찾고, 그 높이로 만들 수 있는 직사각형의 너비를 구한다.
이 후, 방금 사용한 인덱스를 제외하고 좌우의 범위로 이 과정을 한번 더 수행한다.
매 구간에서 최대값을 반환하면 histogram(1, n)의 값이 곧, 만들 수 있는 최대 직사각형의 넓이가 된다.
'''
