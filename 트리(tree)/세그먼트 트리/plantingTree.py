# 백준 1280번 나무 심기 : https://www.acmicpc.net/problem/1280

import math
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
div = 1000000007

n = int(input())
logn = 2 ** math.ceil(math.log2(200000))
sumTree = [0] * ((logn * 2) + 1)
cntTree = [0] * ((logn * 2) + 1)
    
def update(tree, id, val):
    tree[id] += val
    while id > 0:
        id = id // 2
        tree[id] = tree[id * 2] + tree[id * 2 + 1]
    
def query(tree, st, ed, node, left, right):
    if left > ed or right < st: return 0
    if left <= st and ed <= right: return tree[node]
    mid = (st + ed) // 2
    return query(tree, st, mid, node << 1, left, right) + query(tree, mid + 1, ed, (node << 1) + 1, left, right)

sum = 1
for i in range(n):
    tmp = int(input()) + 1
    if i > 0:
        l_cnt = query(cntTree, 1, logn, 1, 1, tmp - 1)
        r_cnt = query(cntTree, 1, logn, 1, tmp + 1, logn)
        l_val = query(sumTree, 1, logn, 1, 1, tmp - 1) % div
        r_val = query(sumTree, 1, logn, 1, tmp + 1, logn) % div
        res = (tmp * l_cnt - l_val - tmp * r_cnt + r_val) % div
        sum = (sum * res) % div
    update(cntTree, tmp + logn - 1, 1)
    update(sumTree, tmp + logn - 1, tmp)
print(sum % div)

# 알고리즘 : 세그먼트 트리
'''
풀이 : 각 나무의 좌표를 정점으로 하여 세그먼트 트리를 생성한다.
나무가 순서대로 심겨지기 때문에 미리 모든 입력을 트리에 대입하면 안된다.
계산의 편의를 위해 세그먼트 트리를 나무의 갯수 트리와 나무의 좌표 트리로 2개 생성한다.
입력마다 트리를 업데이트하고, 방금 입력된 좌표의 왼쪽과 오른쪽의 나무 수와 나무 좌표합을 구한다.

좌표합을 구하는 이유는 다음과 같다.
이번에 좌표 5에 나무가 심겨지고, 좌표 1, 2에 나무가 있다고 하자.
5번 나무를 심는 비용은 (5 - 1) + (5 - 2)이다.
이는 덧셈 법칙에 의해 5 + 5 - (1 + 2)가 된다.
즉, (해당 방향의 나무 수 * 현재 나무 좌표)와 (해당 방향의 모든 좌표 합)의 차이가 비용이 된다.
따라서 세그먼트 트리로 1번부터 현재 좌표 - 1까지의 누적합과 현재좌표 + 1부터 logn까지의 누적합을 구해 더한다.
매 연산마다 1000000007로 나누어 불필요하게 큰 수의 연산을 방지한다.
'''
