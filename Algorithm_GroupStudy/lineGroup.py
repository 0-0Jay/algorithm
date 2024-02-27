# 백준 2162번 선분 그룹 : https://www.acmicpc.net/problem/2162

from collections import defaultdict, deque
import sys
input = sys.stdin.readline

n = int(input())
line = [tuple(map(int, input().split())) for _ in range(n)]
parent = [i for i in range(n)]
cnt = {}
max_cnt = 0

def find(parent, x):
    if parent[x] == x:
        return x
    parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    rootA = find(parent, a)
    rootB = find(parent, b)
    
    if rootA != rootB:
        parent[rootB] = rootA

def CCW(a1, a2, b1, b2, c1, c2):
    return (a1 * b2 + b1 * c2 + c1 * a2) - (a2 * b1 + b2 * c1 + c2 * a1)

def intersect(a1, a2, b1, b2, c1, c2, d1, d2):
    l1 = CCW(a1, a2, b1, b2, c1, c2) * CCW(a1, a2, b1, b2, d1, d2)
    l2 = CCW(c1, c2, d1, d2, a1, a2) * CCW(c1, c2, d1, d2, b1, b2)

    if l1 == 0 and l2 == 0:
        if min(a1, b1) <= max(c1, d1) and min(c1, d1) <= max(a1, b1) and min(a2, b2) <= max(c2, d2) and min(c2, d2) <= max(a2, b2): return True
        else: False
    elif l1 <= 0 and l2 <= 0: return True
    else: return False

for i in range(n):
    for j in range(n):
        if i == j: continue
        a1, a2, b1, b2 = line[i]
        c1, c2, d1, d2 = line[j]
        if intersect(a1, a2, b1, b2, c1, c2, d1, d2):
            union(parent, i, j)

for i in range(n):
    now = find(parent, i)
    if now not in cnt: cnt[now] = 0
    cnt[now] += 1
    max_cnt = max(cnt[now], max_cnt)
    
print(len(cnt))
print(max_cnt)

# 알고리즘 : union/find + CCW
'''
풀이 : 모든 선분에 대한 교차를 검사하고, 교차한다면 union/find로 그룹화한다.
CCW를 활용해 선분 교차를 검사하는 intersect함수를 만든다.
만약 intersect가 True라면 union한다.
이 때, 불필요한 연산을 방지하기 위해 뽑힌 두 선분이 같은 선분이라면 continue로 건너뛴다.
union/find는 처음 입력단계에서 배열에 저장할 때의 인덱스를 활용해 수행한다.

모든 union 과정이 끝나면, 딕셔너리에 그룹과 그룹에 포함된 선분 수를 카운팅한다.
이 때, 현재 선분이 속한 그룹을 알기위해 단순히 parent 배열에서 값을 가져오면 안되고 find로 찾아서 가져와야 한다.
왜냐하면 만약 A 선분이 B 선분의 하위로 들어가면 A의 하위 선분은 여전히 상위로 A를 가리키고 있기 때문이다.
'''
