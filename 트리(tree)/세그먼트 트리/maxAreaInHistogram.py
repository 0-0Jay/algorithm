# 백준 6549번 히스토그램에서 가장 큰 직사각형 : https://www.acmicpc.net/problem/6549

import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

hlist = []
tree = []

def divide(st, ed):
    if st == ed: return hlist[st]
    elif ed < st: return 0
    h, id = minVal(1, hlist[0], 1, st, ed)

    return max(divide(st, id - 1), divide(id + 1, ed), h * (ed - st + 1))

def seg(st, ed, node):
    if st == ed: 
        tree[node] = (hlist[st], st)
        return tree[node]
    mid = (st + ed) // 2
    a = seg(st, mid, node << 1)
    b = seg(mid + 1, ed, (node << 1) + 1)
    tree[node] = a if a[0] < b[0] else b
    return tree[node]

def minVal(st, ed, node, left, right):
    if left > ed or right < st: return (1e12, 0)
    if left <= st and right >= ed: return tree[node]
    mid = (st + ed) // 2
    a = minVal(st, mid, node << 1, left, right)
    b = minVal(mid + 1, ed, (node << 1) + 1, left, right)
    return a if a[0] < b[0] else b
        
while True:
    hlist = list(map(int, input().split()))
    if hlist[0] == 0: break
    tree = [0] * (((2 ** (math.ceil(math.log2(hlist[0])))) << 1) + 1)
    seg(1, hlist[0], 1)
    print(divide(1, hlist[0]))

# 알고리즘 : 분할정복 + 세그먼트 트리
'''
풀이 : 세그먼트 트리로 최소 높이를 가진 인덱스를 찾고, 해당 높이를 기준으로 좌우로 분할하는 과정을 반복한다.
각 테스트 케이스마다 입력값을 최소값 세그먼트 트리에 입력한다.
먼저 st ~ ed까지의 범위 내에서 가장 작은 값을 세그먼트 트리를 통해 찾는다.
이 때, 가장 작은 값이 위치한 인덱스를 기준으로 분할할 것이기 때문에 (값, 인덱스)의 튜플로 트리를 컨트롤한다.
최소값을 찾았다면, 그 값과 st ~ ed의 너비를 곱해 직사각형의 넒이를 구한다.
이 후, 최소값의 인덱스를 기준으로 범위를 좌우로 나누어 위 과정을 반복한다.

매 재귀호출 마다 현재 범위의 너비와 왼쪽 범위의 너비, 오른쪽 범위의 너비를 비교하여 최대값 구한다.
'''
    
 
