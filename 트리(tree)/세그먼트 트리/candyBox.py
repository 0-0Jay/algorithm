# 백준 2243번 - 사탕상자 : https://www.acmicpc.net/problem/2243

import sys
input = sys.stdin.readline

m = 1000000
tree = [0] * (4 * m + 1)

def update(st, ed, node, id, val):
    if id < st or id > ed: return
    tree[node] += val
    if st == ed: return
    mid = (st + ed) // 2
    update(st, mid, node << 1, id, val)
    update(mid + 1, ed, (node << 1) + 1, id, val)

def query(st, ed, node, cnt):
    if st == ed: return st
    mid = (st + ed) // 2
    if tree[node << 1] >= cnt: return query(st, mid, node << 1, cnt)
    return query(mid + 1, ed, (node << 1) + 1, cnt - tree[node << 1])

for _ in range(int(input())):
    cmd = tuple(map(int, input().split()))
    if cmd[0] == 1:
        now = query(1, m, 1, cmd[1])
        print(now)
        update(1, m, 1, now, -1)
    else:
        update(1, m, 1, cmd[1], cmd[2])

# 알고리즘 : 세그먼트 트리
'''
풀이 : 세그먼트 트리를 응용하여 사탕 맛의 개수를 파악한다.
세그먼트 트리를 구성할 때, 각 노드는 맛으로, 해당 노드에 저장된 값은 그 맛의 개수로 둔다.
이렇게 구성하면 특정 사탕보다 더 맛있는 사탕의 수와 더 맛없는 사탕의 수를 파악할 수 있다.

입력값에 따라 1이면 세그먼트 트리에 저장된 값을 갱신하고, 2면 꺼낼사탕의 순위를 이용해 탐색한다.
만약 주어진 순위가 트리의 왼쪽 노드에 저장된 개수 이하라면, 해당 순위의 사탕은 왼쪽에 있으므로 왼쪽 자식 노드를 탐색한다.
그렇지 않다면 오른쪽 자식 노드를 탐색한다.
예를 들어, 왼쪽 자식 노드에 4 오른쪽 자식 노드에 5개가 저장되어있다고 가정하자.
3번째로 맛있는 사탕을 꺼내려면 왼쪽 노드를 탐색해야 한다.
반대로 7번째로 맛있는 사탕을 꺼내려면 오른쪽 노드를 탐색해야 한다.
해당하는 방향으로 리프 노드까지 탐색 했다면, 해당 노드의 인덱스를 return한다.
'''
