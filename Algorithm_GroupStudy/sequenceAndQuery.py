# 백준 14428번 수열과 쿼리 16 : https://www.acmicpc.net/problem/14428

import math
import sys
input = sys.stdin.readline

n = int(input())
arr = [1e12] + list(map(int, input().split()))
tree = [0] * (((2 ** (math.ceil(math.log2(n)))) << 1) + 1)
idx = [0] * (n + 1)

def seg(st, ed, node):
    if st == ed:
        tree[node] = st
        idx[st] = node
        return st
    mid = (st + ed) // 2
    a = seg(st, mid, node << 1)
    b = seg(mid + 1, ed, (node << 1) + 1)
    tree[node] = a if arr[a] <= arr[b] else b
    return tree[node]
    
def update(k):
    if k // 2 == 0: return
    if k // 2 == (k - 1) // 2 and arr[tree[k]] >= arr[tree[k - 1]]: k -= 1 # 오른쪽 자식이고 왼쪽 자식이 더 작거나 같으면 k - 1
    elif k // 2 == (k + 1) // 2 and arr[tree[k]] > arr[tree[k + 1]]: k += 1  # 왼쪽 자식이고, 오른쪽 자식이 더 작으면 k + 1
    if arr[tree[k // 2]] > arr[tree[k]]: 
        tree[k // 2] = tree[k]
        update(k // 2)
    elif arr[tree[k // 2]] == arr[tree[k]]:
        if tree[k] < tree[k // 2]: tree[k // 2] = tree[k]
        update(k // 2)
        
def output(st, ed, node, left, right):
    if left > ed or right < st: return 0
    if left <= st and ed <= right: return tree[node]
    mid = (st + ed) // 2
    a = output(st, mid, node << 1, left, right)
    b = output(mid + 1, ed, (node << 1) + 1, left, right)
    return a if arr[a] <= arr[b] else b

seg(1, n, 1)
m = int(input())
for _ in range(m):
    a, b, c = map(int, input().split())
    if a == 2:
        print(output(1, n, 1, b, c))
    else:
        arr[b] = c
        update(idx[b])

# 알고리즘 : 세그먼트 트리
'''
풀이 : '수열과 쿼리 15' 문제와 동일하되, 구간 최소값 인덱스를 출력하게 수정한다.
세그먼트 트리 구성과 인덱스 활용 방식은 '수열과 쿼리 15'를 참고한다.
출력을 위한 output 함수를 정의한다.
일반적인 세그먼트 트리에서의 구간 활용 방식과 같이 범위에 벗어나면 0, 범위 안이면 tree[node]를 반환한다. 
이 때, arr[0]을 사전에 1e12로 설정해두었기 때문에 아래 좌우 중 작은 값 찾는 과정에서 반드시 배제된다.
왼쪽 및 오른쪽 자식이 가진 인덱스를 가져와 arr에서 해당 인덱스의 값을 비교하여 더 작은 쪽의 인덱스를 반환한다.
'''
