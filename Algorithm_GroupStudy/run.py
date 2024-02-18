# 백준 2517번 달리기 : https://www.acmicpc.net/problem/2517

from collections import defaultdict, deque
import heapq as hq
import math
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n = int(input())
logn = 2 ** math.ceil(math.log2(n))
tree = [0] * ((logn * 2) + 1)
arr = [[0, 0]] + [[int(input()), i] for i in range(1, n + 1)]

arr.sort(key = lambda x : x[0])
for i in range(n + 1):
    arr[i][0] = i
arr.sort(key = lambda x : x[1])

def update(st, ed, node, id):
    if id < st or id > ed: return
    tree[node] += 1
    if st == ed: return
    mid = (st + ed) // 2
    update(st, mid, node << 1, id)
    update(mid + 1, ed, (node << 1) + 1, id)
    
def query(st, ed, node, left, right):
    if left > ed or right < st: return 0
    if left <= st and right >= ed: return tree[node]
    mid = (st + ed) // 2
    return query(st, mid, node << 1, left, right) + query(mid + 1, ed, (node << 1) + 1, left, right)
    
for i in range(1, n + 1):
    val = arr[i][0]
    print(query(1, n, 1, val, n) + 1)
    update(1, n, 1, val)

# 알고리즘 : 세그먼트 트리 + 좌표 압축
'''
풀이 : 세그먼트 트리로 자신보다 실력이 좋은 선수들의 수를 구한다.
입력 단계에서 선수들의 실력이 1000000000까지 인데 이를 배열에 직접 사용하면 반드시 메모리 초과가 발생한다.
따라서 모든 선수들의 실력을 오름차순 했을 때의 순번으로 치환해준다.
계산 상 필요한 정보는 앞 선수와 뒤 선수의 실력의 우열이므로 A와 B가 1000000만큼 차이 나는 경우와 1만큼 차이 나는 경우의 결과는 동일하기 때문이다.

이 후, 입력 순서대로 세그먼트 트리를 계산한다.
어떤 선수의 실력이 val이라면, 세그먼트 트리에서 val보다 크고 n보다 작은 모든 선수의 수를 구한다.
모든 선수의 수를 구해서 출력한 후에 현재 선수를 트리에 추가해준다.
이때, 현재 선수가 누적합에 영향을 주지 않도록 반드시 출력 후에 현재 선수를 추가해야 한다.
입력이 되면 1부터 n까지의 범위 중 val에 1로 수정되고, 매 계산마다 val부터 n까지의 1 개수를 세기 때문에 세그먼트 트리의 누적합으로 계산할 수 있다.
'''
