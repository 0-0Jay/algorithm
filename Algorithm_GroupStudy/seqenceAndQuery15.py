# 백준 14427번 수열과 쿼리 15 : https://www.acmicpc.net/problem/14427

import math
import sys
input = sys.stdin.readline

n =  int(input())
arr = [1e12] + list(map(int, input().split()))
idx = [0] * (n + 1)
tree = [1e12] + [0] * ((2 ** (math.ceil(math.log2(n)))) << 1)
q = int(input())

def seg(st, ed, node): 
    if st == ed:
        tree[node] = st
        idx[st] = node
        return tree[node]
    mid = (st + ed) // 2
    a = seg(st, mid, node << 1)
    b = seg(mid + 1, ed, (node << 1) + 1)
    tree[node] = a if arr[a] <= arr[b] else b  # 같은 경우도 왼쪽 선택
    return tree[node]

def update(k):
    if k // 2 == 0: return
    if k // 2 == (k - 1) // 2: # 오른쪽 자식인 경우
        if arr[tree[k]] >= arr[tree[k - 1]]: k -= 1 # 왼쪽이 작거나 같으면 k값 교체
    else:  # 왼쪽 자식인 경우
        if arr[tree[k]] > arr[tree[k + 1]]: k += 1 # 오른쪽이 작으면 k값 교체
    
    if arr[tree[k]] < arr[tree[k // 2]]:
        tree[k // 2] = tree[k]
        update(k // 2)
    elif arr[tree[k]] == arr[tree[k // 2]]:
        if tree[k] < tree[k // 2]:
            tree[k // 2] = tree[k]
        update(k // 2)

seg(1, n, 1)
for i in range(q):
    tmp = list(map(int, input().split()))
    if tmp[0] == 1:
        arr[tmp[1]] = tmp[2]
        update(idx[tmp[1]])
    else:
        print(tree[1])

# 알고리즘 : 세그먼트 트리
'''
풀이 : 세그먼트 트리를 생성하고, heap정렬의 push방식을 응용해 update를 수행한다.
가장 작은 값들 중 가장 작은 인덱스를 선택하라는 조건에 따라 모든 대소 비교에서 왼쪽 자식에 같을 때를 포함시켜준다.
즉, 오른쪽 자식이 더 작은 경우를 제외하고 모두 왼쪽 자식의 우선순위를 높여준다.

update를 할때는, heap 구현에서 데이터 삽입의 경우를 응용한다.
그러나 바뀌는 인덱스가 tree에서 어느 인덱스에 있는지 알 수 없다.
따라서 arr의 각 인덱스가 tree에서 어느 인덱스와 매칭되어 있는지 세그먼트 트리를 만들면서 idx에 기록한다.
변경 명령이 들어오면 바뀌는 인덱스를 idx에서 트리에서의 인덱스로 바꾸어 update를 수행한다.
update를 수행할 때도 다른 자식 테이블과 비교해 더 작은 값의 인덱스를 부모로 올린다.

쿼리 명령이 들어오면 update를 heap의 push방식으로 했기때문에 tree[1]을 출력하면 반드시 요구하는 값이 출력된다.
'''
