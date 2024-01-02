# 백준 2042번 구간 합 구하기 : https://www.acmicpc.net/problem/2042

import math
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
arr = [0]
tree = [0] * (((2 ** (math.ceil(math.log2(n)))) << 1) + 1)

def seg(st, ed, node):
    if st == ed:  # 만약 st와 ed가 같으면 해당 노드는 자식 노드가 없다.
        tree[node] = arr[st]  # 자식 노드가 없다는 것은 숫자 하나 즉, 구간합이 아니라는 뜻이다.
        return tree[node]
    mid = (st + ed) // 2  # 만약 자식노드가 있다면, st ~ ed의 구간을 절반으로 나눈다.
    # 자식 노드의 인덱스는 현재 노드의 인덱스에 *2한 값과 *2 + 1한 값이 된다.
    tree[node] = seg(st, mid, node << 1) + seg(mid + 1, ed, (node << 1) + 1)
    return tree[node]  # 현재 노드의 값을 부모 노드로 올려준다.

def prefix(st, ed, node, left, right):  # left와 right는 구간합을 구할 범위
    if left > ed or right < st: return 0  # 만약 st와 ed가 범위 밖이면 계산할 필요 없으므로 0을 반환한다.
    if left <= st and right >= ed: return tree[node]  # 모두 범위 안이면 현재 노드의 값을 반환한다.
    mid = (st + ed) // 2
    # 만약 st와 ed가 구간합을 구할 범위에 겹쳐있다면, 구간을 절반으로 나누어 한번 더 탐색한다.
    return prefix(st, mid, node << 1, left, right) + prefix(mid + 1, ed, (node << 1) + 1, left, right)

def update(st, ed, node, id, diff):
    if id < st or id > ed: return
    tree[node] += diff  # 수정된 값과 이전 값의 차이를 해당 숫자가 포함된 범위에 모두 반영한다.
    if st == ed: return
    mid = (st + ed) // 2
    update(st, mid, node << 1, id, diff)
    update(mid + 1, ed, (node << 1) + 1, id, diff)
    
for i in range(n):
    arr.append(int(input()))
seg(1, n, 1)
    
for i in range(m + k):
    a, b, c = map(int, input().split())
    if a == 1:
        update(1, n, 1, b, c - arr[b])
        arr[b] = c
    else:
        print(prefix(1, n, 1, b, c))

# 알고리즘 : 세그먼트 트리
'''
풀이 : 세그먼트 트리를 이용해 logN으로 구간합을 구한다.
먼저 세그먼트 트리를 위한 배열(tree)을 만든다.
이 때, 배열의 크기는 n보다 큰 2의 제곱수들 중, 가장 작은 수에 * 2 + 1로 설정한다.
예를 들어 n이 5라면, 2의 3제곱인 8이 가장 작으므로 배열의 크기는 17이된다.
배열의 인덱스를 0부터 시작하는 것이 아닌, 1부터 시작하게 끔 설정하는 이유는 이진 트리의 노드를 컨트롤 할 때 자식노드의 인덱스를 단순히 부모노드 인덱스 * 2로 계산할 수 있기 때문이다.

배열을 만들었다면 구간합 계산을 위한 함수를 세가지 만든다.
1. 세그먼트 트리 배열을 채워넣는 seg 함수
2. 값이 수정되는 경우 세그먼트 트리를 수정할 update 함수
3. 요구하는 구간의 합을 구해주는 prefix 함수
모든 함수는 기존 배열의 구간을 절반으로 나누어 탐색하는 이진 트리 탐색 방식으로 수행한다.
'''
