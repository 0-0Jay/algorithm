# 백준 7578번 공장 : https://www.acmicpc.net/problem/7578

from collections import defaultdict, deque
import heapq as hq
import math
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n = int(input())
logn = 2 ** math.ceil(math.log2(n))
tree = [0 for _ in range(logn * 2 + 1)]
A = list(map(int, input().split()))
B = list(map(int, input().split()))
Bmap = {}
for i in range(n):
    Bmap[B[i]] = i + 1

def update(tree, id):
    tree[id] += 1
    while id > 1:
        id //= 2
        tree[id] = tree[id * 2] + tree[id * 2 + 1]
    
def query(tree, st, ed, node, left, right):
    if ed < left or right < st: return 0
    if left <= st and ed <= right: return tree[node]
    mid = (st + ed) // 2
    return query(tree, st, mid, node << 1, left, right) + query(tree, mid + 1, ed, (node << 1) + 1, left, right)

cnt = 0
for i in range(n):
    now = Bmap[A[i]]
    cnt += query(tree, 1, logn, 1, now, logn)
    update(tree, now + logn - 1)
print(cnt)

# 알고리즘 : 세그먼트 트리 + 맵핑
'''
풀이 : B열의 기계를 식별번호와 인덱스로 맵핑해두고, 세그먼트 트리로 해당 인덱스 이후의 기계 수를 센다.
A열을 맵핑하던, B열을 맵핑하던 상관없다.
열 하나에서 식별번호를 key로, 인덱스를 value로 맵핑해둔다.
이러면 A열에서의 기계와 연결되는 반대편 기계가 B열에서 어느 인덱스에 위치하는지 알 수 있다.

교차 계산은 세그먼트 트리로 하는데, 그 과정은 다음과 같다.
A열에서 가장 왼쪽부터 기계를 하나씩 뽑는다.
뽑은 기계의 B열에서의 인덱스를 가져와, 해당 인덱스부터 가장 오른쪽 인덱스까지 연결된 기계 수를 센다.
기계 수를 cnt에 누적시킨다.
위 과정을 A열 마지막 기계까지 반복한다.

예제를 예로 들자면, 132를 뽑으면 B열의 3번에 연결된다.
이후 392를 뽑았을 때, 1부터 5번까지 연결된 기계 수를 세보면, 이전에 뽑은 132가 있으니 1개다.
즉, A의 2번인 392가 B의 1번에 연결되면 A의 2번 이전의 기계가 B의 1번 이후에 연결되었다면 교차가 발생한 것이다.
'''
