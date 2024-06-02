# 백준 3665번 최종 순위 : https://www.acmicpc.net/problem/3665

from collections import deque
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    before = [0] * (n + 1)
    graph = [set() for _ in range(n + 1)]
    
    t = list(map(int, input().split()))
    for i in range(n - 1):
        for j in range(i + 1, n):
            graph[t[i]].add(t[j])
            before[t[j]] += 1
    
    flag = 0
    m = int(input())
    for _ in range(m):
        a, b = map(int, input().split())
        if a in graph[b]: 
            before[a] -= 1
            before[b] += 1
            graph[b].remove(a)
            graph[a].add(b)
        elif b in graph[a]:
            before[b] -= 1
            before[a] += 1
            graph[a].remove(b)
            graph[b].add(a)
    
    que = deque()
    for i in range(1, n + 1):
        if before[i] == 0: que.append(i)
        if len(que) > 1: 
            flag = 1
            break

    score = []
    while que and not flag:
        now = que.popleft()
        score.append(now)
        
        for nx in graph[now]:
            before[nx] -= 1
            if before[nx] == 0:
                que.append(nx)
                if len(que) > 1: 
                    flag = 1
                    break
        
    if len(score) < n : print('IMPOSSIBLE')
    else : print(*score)


# 알고리즘 : 위상정렬
'''
풀이 : 이전 순위 정보를 graph와 before 배열로 저장해두고, 바뀐 순위에 맞추어 graph와 before를 수정한다.
graph는 현재 팀 다음 순위인 모든 팀에 대한 정보를 집합 형태로 저장한 배열이다.
before는 각 팀 당 자신보다 높은 순위에 위치한 팀 수를 저장한 배열이다.

모든 변동 된 순위를 graph와 before에 반영한 후에, 위상정렬을 수행한다.
먼저 before 배열을 탐색하여 자신보다 높은 순위가 없는 팀을 찾아 큐에 넣어준다.
만약 그런 팀이 2개 이상이라면, 불가능한 경우기 때문에 flag를 1로 수정해주고 break로 추가 탐색을 방지한다.

flag가 0이고 que에 팀이 들어있다면, 탐색을 수행한다.
que에서 팀을 뽑을 때마다 score에 차례대로 추가해준다.
이 후, 위상정렬 알고리즘에 따라 방금 뽑은 팀 now보다 등수가 낮은 팀들의 before 수를 1씩 감소시킨다.
만약 before가 0이 된 팀은 다음에 뽑을 팀이므로 que에 추가한다.
이 경우에도 마찬가지로 다음에 뽑을 수 있는 팀이 2개 이상이 되면, flag를 1로 수정해주고 break로 추가 탐색을 방지한다.

최종적으로 score에 모든 팀이 들어가지 않았다면, 불가능한 경우가 발생했다는 뜻이므로 IMPOSSIBLE을 출력한다.
아니라면 score의 원소를 출력한다.

* 문제의 출력 조건에 확실한 순위를 찾을 수 없다면 ?를 출력하라는 조건이 있다.
그러나 이 경우 반드시 데이터의 일관성이 없어지게 되므로 IMPOSSIBLE을 출력하는 조건과 다르지 않다.
따라서 ?를 출력하는 케이스는 존재하지 않으므로 배제해도 되는 조건이다.
'''
