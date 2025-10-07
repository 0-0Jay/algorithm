# 백준 10868번 최솟값 : https://www.acmicpc.net/problem/10868

import math
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [0]
tree = [0] * (((2 ** (math.ceil(math.log2(n)))) << 1) + 1)

def seg(st, ed, node):
    if st == ed:
        tree[node] = arr[st]
        return tree[node]
    mid = (st + ed) // 2
    tree[node] = min(seg(st, mid, node * 2), seg(mid + 1, ed, node * 2 + 1))
    return tree[node]
    
def minVal(st, ed, node, left, right):
    if left > ed or right < st: return 1e12
    if left <= st and right >= ed: return tree[node]
    mid = (st + ed) // 2
    return min(minVal(st, mid, node * 2, left, right), minVal(mid + 1, ed, node * 2 + 1, left, right))
        
for i in range(n):
    arr.append(int(input()))
seg(1, n, 1)
    
for i in range(m):
    a, b = map(int, input().split())
    print(minVal(1, n, 1, a, b))

# 알고리즘 : 세그먼트 트리
'''
풀이 : 세그먼트 트리를 응용해 각 구간의 최솟값을 구한다.
최솟값과 최댓값 문제와 완전히 동일한 하위 호환 문제다.
자세한 설명은 해당 문제를 보고 참고
'''
