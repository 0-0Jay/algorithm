# 백준 1321번 군인 : https://www.acmicpc.net/problem/1321

import math
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n = int(input())
army = [0] + list(map(int, input().split()))
m = int(input())
logn = (((2 ** (math.ceil(math.log2(n)))) << 1) + 1)
tree = [[0, 0] for i in range(logn)]

def seg(st, ed, node):
    if st == ed:
        tree[node] = [army[st], ed]
        return tree[node]
    mid = (st + ed) // 2
    lnode = seg(st, mid, node << 1)
    rnode = seg(mid + 1, ed, (node << 1) + 1)
    tree[node] = [lnode[0] + rnode[0], rnode[1]]
    return tree[node]
    
def update(st, ed, node, id, val):
    if id < st or id > ed: return
    tree[node][0] += val
    if st == ed: return
    mid = (st + ed) // 2
    update(st, mid, node << 1, id, val)
    update(mid + 1, ed, (node << 1) + 1, id, val)
    
def query(st, ed, node, val):
    if st == ed: return tree[node][1]
    mid = (st + ed) // 2
    lnode = tree[node << 1]
    if val < tree[node][0]:
        if val <= lnode[0]:
            return query(st, mid, node << 1, val)
        else:
            return query(mid + 1, ed, (node << 1) + 1, val - lnode[0])
    return tree[node][1]
 
seg(1, n, 1)
for _ in range(m):
    tmp = list(map(int, input().split()))
    if tmp[0] == 1:
        update(1, n, 1, tmp[1], tmp[2])
    else:
        res = query(1, n, 1, tmp[1])
        print(res)

# 알고리즘 : 세그먼트 트리
'''
풀이 : 누적합과 부대 번호를 함께 세그먼트 트리에 저장해 탐색한다.
'''
