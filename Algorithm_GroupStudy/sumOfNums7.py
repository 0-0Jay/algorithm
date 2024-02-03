# 백준 2268번 수들의 합 7 : https://www.acmicpc.net/problem/2268

from collections import defaultdict, deque
import heapq as hq
import math
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [0] * (n + 1)
tree = [0] * (((2 **math.ceil(math.log2(n))) << 1) + 1)
idx = [0] * (n + 1)

def seg(st, ed, node):
    if st == ed:
        idx[st] = node
        return
    mid = (st + ed) // 2
    seg(st, mid, node << 1)
    seg(mid + 1, ed, (node << 1) + 1)
    return

def sum(st, ed, node, left, right):
    if left > ed or right < st: return 0
    if left <= st and ed <= right: return tree[node]
    mid = (st + ed) // 2
    return sum(st, mid, node << 1, left, right) + sum(mid + 1, ed, (node << 1) + 1, left, right)
    
def modify(k, diff):
    tree[k] += diff
    if k // 2 == 0 : return
    modify(k // 2, diff)
    
seg(1, n, 1)
for i in range(m):
    a, b, c = map(int, input().split())
    if a == 0:
        if b > c: b, c = c, b
        print(sum(1, n, 1, b, c))
    else:
        modify(idx[b], c - arr[b])
        arr[b] = c

# 알고리즘 : 세그먼트 트리
'''
풀이 : arr의 각 인덱스가 트리에서 어디에 위치하는지 seg 함수를 통해 기록하고, modify로 수정한다.
다른 구간합 문제와 다르게 이 문제는 초기 숫자를 모두 0으로 주기때문에 seg 함수에 합산 과정은 생략한다.
이 후 각 입력에서 a가 0이면 sum, 1이면 modify 함수를 수행한다.
modify함수는 초기 idx에 저장한 인덱스를 활용해 heap 방식으로 수정한다.
'''
