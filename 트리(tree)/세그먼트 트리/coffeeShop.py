# 백준 1275번 커피숍2 : https://www.acmicpc.net/problem/1275

from collections import defaultdict, deque
import heapq as hq
import math
import sys
input = sys.stdin.readline

n, q = map(int, input().split())
arr = [0] + list(map(int, input().split()))
tree = [0] * (((2 ** (math.ceil(math.log2(n)))) << 1) + 1)

def segTree(st, ed, node):
    if st == ed:
        tree[node] = arr[st]
        return tree[node]
    mid = (st + ed) // 2
    tree[node] = segTree(st, mid, node << 1) + segTree(mid + 1, ed, (node << 1) + 1)
    return tree[node]

def update(st, ed, node, id, diff):
    if id < st or id > ed: return
    tree[node] += diff
    if st == ed: return
    mid = (st + ed) // 2
    update(st, mid, node << 1, id, diff)
    update(mid + 1, ed, (node << 1) + 1, id, diff)
    
def output(st, ed, node, l, r):
    if l > ed or r < st: return 0
    if l <= st and ed <= r: return tree[node]
    mid = (st + ed) // 2
    return output(st, mid, node << 1, l, r) + output(mid + 1, ed, (node << 1) + 1, l, r)
    
segTree(1, n, 1)
for i in range(q):
    x, y, a, b = map(int, input().split())
    if x > y: x, y = y, x
    print(output(1, n, 1, x, y))
    update(1, n, 1, a, b - arr[a])
    arr[a] = b

# 알고리즘 : 세그먼트 트리
'''
풀이 : 세그먼트 트리를 이용해 구간합을 구하고, 자료를 업데이트 한다.
이전에 풀어본 구간합 구하기 문제와 완전히 동일하다.
-> 자세한 설명은 구간합 구하기 : Algorithm_GroupStudy/calcPrefixSum.py 참고
'''
