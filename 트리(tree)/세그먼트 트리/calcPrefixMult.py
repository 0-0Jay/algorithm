# 백준 11505번 구간 곱 구하기 : https://www.acmicpc.net/problem/11505

from collections import defaultdict, deque
from functools import cmp_to_key
import heapq as hq
import math
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
arr = [0]
tree = [0] * (((2 ** math.ceil(math.log2(n)))) * 2 + 1)
div = 1000000007

def seg(st, ed, node):
    if st == ed:
        tree[node] = arr[st]
        return tree[node]
    mid = (st + ed) // 2
    tree[node] = (seg(st, mid, node * 2) * seg(mid + 1, ed, node * 2 + 1)) % div
    return tree[node]

def mult(st, ed, node, left, right):
    if right < st or left > ed: return 1
    if left <= st and right >= ed: return tree[node]
    mid = (st + ed) // 2
    return (mult(st, mid, node * 2, left, right) * mult(mid + 1, ed, node * 2 + 1, left, right)) % div

def update(st, ed, node, id, aft):
    if id < st or id > ed: return
    if st == ed: 
        tree[node] = aft
        return
    mid = (st + ed) // 2
    update(st, mid, node * 2, id, aft)
    update(mid + 1, ed, node * 2 + 1, id, aft)
    tree[node] = (tree[node * 2] * tree[node * 2 + 1]) % div
    
for i in range(n):
    arr.append(int(input()))    
    
seg(1, n, 1)
for i in range(m + k):
    a, b, c = map(int, input().split())
    if a == 1:
        update(1, n, 1, b, c)
        arr[b] = c
    else:
        print(int(mult(1, n, 1, b, c)))

# 알고리즘 : 세그먼트 트리
'''
풀이 : 세그먼트 트리를 생성해 구간 곱을 구한다.
구간 합 구하기와 트리 생성 부분은 동일하다.
그러나 곱을 계산하는 부분과, 값을 수정하는 부분에서 처리해줘야 할 부분이 있다.

먼저 구간곱을 구하는 mult 함수는 범위 밖에 대한 요청이 들어올 때 0이 아닌 1을 반환해야한다.
곱셈이기 때문에 0이 곱해져 버리면 결과값이 0이 되어버리기 때문이다.
또한 오버플로우를 방지하기 위해 매 곱셈마다 % 1000000007를 수행하여 트리에 저장한다.

값을 변경하는 부분은 단순히 이전 값을 나누었다가 새로운 값을 곱해주는 방식으로 계산하면 안된다.
따라서 기존에 구간합 구하기에서 전위 탐색으로 tree의 값을 변경해주는 방식을 사용하지 않는다.
후위 탐색을 통해 하위 노드부터 차례대로 새로 곱해주는 방식으로 변경해야 한다.
이를 위해 만약 범위가 숫자 하나라면 교체된 인덱스이므로 새로운 값으로 바꿔준다.
범위가 여러개라면 해당 범위를 반으로 나누어 하위 계산을 수행한 후 두 하위 결과의 곱을 현재 노드에 저장한다.
'''
