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
세그먼트 트리를 탐색할 때에 자식 노드 중 왼쪽 노드에 해당하는 값(현재 탐색중인 범위의 왼쪽 절반)과 현재 군번을 비교해서 이 사람이 어느 부대 소속인지 판별한다.
예를 들어, 5번까지의 부대번호가 있고 8번 군인이 몇번째에 부대 소속인지를 찾는다고 하자.
1번부터 3번까지의 모든 부대인원의 합의 5명이라면, 8번 군인은 최소 4번 부대에 존재할 가능성이 생긴다.

이를 위해, 전체 범위를 기준으로 반씩 나누어 가며 왼쪽 자식노드의 값(lnode)과 현재 군인(val)의 번호를 비교한다.
만약 val이 현재 범위의 크기보다 작다면, 현재범위에 소속된 부대 중 한 곳에 val이 소속되어있다는 의미이다.
따라서, 현재 범위를 반으로 나누어서 val과 한번 더 비교한다.
만약 val이 왼쪽 절반 범위보다 작다면 왼쪽 절반 노드로 내려가 위 과정을 한 번 더 수행한다.
크다면, 오른쪽 절반 범위로 이동한다. 단, 부대별로 각각의 값이 누적합 세그먼트 트리에 저장되어있기 때문에 오른쪽으로 이동할때는 lnode의 값을 뺀 값만 내려간다.
위 과정을 st와 ed가 같아질때까지 반복했을때 리턴되는 부대 번호가 곧, 해당 군인의 부대번호이다.
'''
