# 백준 1572번 - 중앙값 : https://www.acmicpc.net/problem/1572

import math
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n, k = map(int, input().split())
arr = [0]
tree = [0] * (65537 * 4)

def update(st, ed, node, id, val):
    if id < st or id > ed: return
    tree[node] += val
    if st == ed: return
    mid = (st + ed) // 2
    update(st, mid, node << 1, id, val)
    update(mid + 1, ed, (node << 1) + 1, id, val)

def middle(st, ed, node, q):
    if st == ed: return st
    mid = (st + ed) // 2
    if tree[node << 1] >= q: return middle(st, mid, node << 1, q)
    else: return middle(mid + 1, ed, (node << 1) + 1, q - tree[node << 1])

res = 0
for i in range(1, n + 1):
    arr.append(int(input()))
    update(0, 65537, 1, arr[i], 1)
    if i >= k:
        res += middle(0, 65537, 1, (k + 1) // 2)
        update(0, 65537, 1, arr[i - k + 1], - 1)

print(res)

# 알고리즘 : 세그먼트 트리 + 슬라이딩 윈도우
'''
풀이 : 수의 개수를 누적한 세그먼트 트리를 이용해 중앙값을 찾는다.
먼저 실제 수를 저장할 배열(arr)과 해당 수를 인덱스로 활용할 세그먼트 트리(tree)를 만든다.
이 때, 입력되는 수가 65536까지므로 세그먼트 트리의 인덱스는 충분히 크게 65547 * 4만큼 만든다.

이 문제는 기존의 구간합 문제와 다르게 모든값을 세그먼트 트리에 한번에 업데이트하고 값을 찾으면 안된다.
부분수열의 중앙값은 범위에 따라 값이 달라지기 때문에 세그먼트 트리를 배열로 컨트롤해야하기 때문이다.
따라서 중앙 인덱스(q)의 왼쪽에 존재하는 수와 오른쪽에 존재하는 수를 활용해 중앙값을 찾는 것이다.

먼저 arr에 값을 넣는다.
arr에 값을 저장해두는 이유는 후에 최근 k개의 숫자에 포함되지 않는 수의 개수를 -1 해주기 위해서다.
방금 저장한 값을 인덱스로 하여 세그먼트 트리의 위치를 업데이트한다.
이는 해당 숫자가 1개 존재한다는 뜻이다.

i가 k 이상이 되면, 최근 온도 k개가 준비되었다는 뜻이므로 중앙값을 찾는다.
문제에서 중앙값의 인덱스는 (k + 1) // 2의 위치라고 주어져 있으므로 해당 인덱스를 찾는다.
해당 인덱스의 노드를 갔을 떄, 왼쪽 자식 노드와 오른쪽 자식 노드가 가진 숫자의 개수를 비교한다.
만약 왼쪽 노드가 q((k + 1) // 2)보다 크거나 같으면, 작아질 때까지 왼쪽 자식 노드를 재귀 탐색한다.
그렇지 않다면 q에서 왼쪽 자식 노드에 있는 숫자의 개수를 빼고 오른쪽 자식노드를 재귀 탐색한다.
재귀탐색을 수행하다 st와 ed 가 같아지면, st를 반환한다.
아까 값을 트리의 인덱스로 사용했기 때문에 tree[st]가 아닌, st를 반환하면 중앙값을 찾을 수 있다.
이 값을 res에 누적하고, arr에서 i - k + 1번 인덱스에 있는 값(가장 먼저 들어왔던 값)에 -1을 업데이트하여 0으로 초기화 해준다.
이 과정을 마지막 인덱스까지 반복했을 때, res에 누적된 값이 중앙값의 총합이된다.
'''
