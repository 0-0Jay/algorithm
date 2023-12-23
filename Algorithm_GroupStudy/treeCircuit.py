# 백준 2263번 트리의 순회 : https://www.acmicpc.net/problem/2263

from collections import defaultdict, deque
import heapq as hq
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n = int(input())
in_order = {value : id for id, value in enumerate(list(map(int,input().split())))}
post_order = list(map(int, input().split()))

def find(in_left, in_right, post_left, post_right):
    if in_left > in_right or post_left > post_right: return
    p = post_order[post_right]
    print(p, end=" ")

    left_end = post_left + (in_order[p] - in_left) - 1
    right_end = left_end + 1
            
    find(in_left, in_order[p] - 1, post_left, left_end)
    find(in_order[p] + 1, in_right, right_end, post_right - 1)
    
find(0, n - 1, 0, n - 1)

# 알고리즘 : 분할 정복
'''
풀이 : 후위 탐색 결과를 이용해 해당 서브트리의 부모 노드를 찾고, 중위 탐색 결과를 이용해 왼쪽 서브트리와 오른쪽 서브트리의 경계점을 찾는다.

현재 탐색범위의 서브트리에서 루트 노드는 후위탐색의 범위내에서 가장 오른쪽에 있는 노드다.
이 노드가 중위탐색에서 어느 인덱스에 위치하는지를 딕셔너리(in_order)를 이용해 찾아낸다.
이 후, 중위 탐색에서 루트 노드 인덱스를 기준으로 현재 서브트리의 왼쪽 끝~루트 노드 까지의 길이만큼 후위 탐색 범위에서 잘라낸다.(left_end)
이 범위가 곧, 현재 루트 노드의 하위 서브트리 중 왼쪽 서브트리가 된다.
자연스럽게 남은 범위는 오른쪽 서브트리가 된다.(right_end)
이 과정을 범위가 사라질 때 까지 반복하며 매 탐색마다 루트 노드를 출력한다.
(단, 반드시 출력 후에 왼쪽 서브트리부터 탐색해야 한다. 전위 탐색이기 때문이다.)
* 해당 서브트리의 인덱스 범위만을 이용해 재귀를 수행해야 메모리 초과가 발생하지 않는다.
'''
