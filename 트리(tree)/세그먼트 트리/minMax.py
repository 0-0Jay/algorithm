# 백준 2357번 최솟값과 최댓값 : https://www.acmicpc.net/problem/2357

import math
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [0]
tree = [[]] * (((2 ** (math.ceil(math.log2(n)))) << 1) + 1)

def seg(st, ed, node):
    if st == ed:
        tree[node] = [arr[st], arr[st]]
        return tree[node]
    mid = (st + ed) // 2
    l = seg(st, mid, node * 2)
    r = seg(mid + 1, ed, node * 2 + 1)
    tree[node] = [min(l[0], r[0]), max(l[1], r[1])]
    return tree[node]
    
def min_max(st, ed, node, left, right):
    if left > ed or right < st: return [1e12, 0]
    if left <= st and right >= ed: return tree[node]
    mid = (st + ed) // 2
    l = min_max(st, mid, node * 2, left, right)
    r = min_max(mid + 1, ed, node * 2 + 1, left, right)
    return [min(l[0], r[0]), max(l[1], r[1])]
        
for i in range(n):
    arr.append(int(input()))
seg(1, n, 1)
    
for i in range(m):
    a, b = map(int, input().split())
    print(*min_max(1, n, 1, a, b))

# 알고리즘 : 세그먼트 트리
'''
풀이 : 세그먼트 트리를 응용해 자식 노드로 부터 반환된 값들을 최소값, 최대값 비교한다.
세그먼트 트리를 위한 배열(tree)를 만들어 둔다.
seg 함수를 통해 각 구간별 최소값과 최대값을 구한다.
현재 노드의 최소값은 왼쪽 자식 노드의 최소값과 오른쪽 자식노드의 최소값 중 더 작은 값이다.
최대값 또한 두 자식 노드의 최대값 중 더 큰 값이다.
부모 노드로 반환할 때는 [최소값, 최대값] 형태의 배열로 반환하게 했다.

min_max 함수를 통해 원하는 구간의 최소값과 최대값을 구한다.
현재 node의 범위(st ~ ed)가 원하는 구간(left ~ right) 내에 포함되어 있다면 현재 노드의 값들을 반환한다.
만약 구간에 겹치지 않으면 부모 노드에서 반드시 탈락하게 하기 위해 임의로 설정한 최악 값(1e12, 0)을 반환한다.
만약 node의 범위가 원하는 구간에 포함되진 않지만 겹쳐져 있다면 범위를 절반으로 나누어 자식 노드를 탐색한다.
'''
