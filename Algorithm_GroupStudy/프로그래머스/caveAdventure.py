# 프로그래머스 2020 카카오 인턴십 동굴 탐험 : https://school.programmers.co.kr/learn/courses/30/lessons/67260

from collections import deque

def solution(n, path, order):
    graph = [set() for _ in range(n)]
    for a, b in path:
        graph[a].add(b)
        graph[b].add(a)
    after = {}
    before = [0] * n
    for a, b in order:
        if a == 0: continue
        if b == 0: return False
        if a not in after: after[a] = []
        after[a].append(b)
        before[b] += 1
        
    que = deque([0])
    chk = set({0})
    while que:
        now = que.popleft()
        for nx in graph[now]:
            if nx not in chk:
                chk.add(nx)
                if before[nx] == 0:
                    chk.add(nx)
                    que.append(nx)
                    if nx in after:
                        for b in after[nx]:
                            before[b] -= 1
                            if before[b] == 0 and b in chk:
                                que.append(b)
                        after.pop(nx)
                        if len(after) == 0: return True
    return False

# 알고리즘 : BFS + 위상 정렬
'''
풀이 : BFS를 수행하다가 벽을 발견하면 방문 기록만 두었다가 순서 조건이 충족 되었을 때 que에 넣는다.
이 문제에서 가장 중요한 고려사항은 다음 두 가지이다.
1. 주어진 순서 조건만 만족한다면 다른 방은 어떤 순서로 방문해도 무관하다. (위상 정렬)
2. 순서 조건 (a, b) 쌍에서 b방이 a방보다 먼저 도착할 수도 있는 경우가 발생한다.

위 두 가지를 해결하기 위해 우선 입력받은 order의 (a, b) 쌍을 after와 before에 다음과 같이 가공한다.
1. after : a방에 도착했다면, b방에 갈 수 있다는 정보를 저장하는 딕셔너리(map)
2. before : b방에 방문하기 전에 방문해야할 방의 개수를 기록하는 배열

이 후, 두 정보를 기반으로 chk에 방문기록을 저장하며 BFS를 탐색한다.
이 때, 일반적으로 BFS를 돌려면 order의 (a, b)쌍 중 a방을 방문했을 때, 이를 추가로 체크해주는 과정이 필요한데, 이를 위해 비트마스킹, 플래그 등을 활용하게 되면 반드시 시간 초과가 발생한다.
따라서 0번 정점에서 마지막 정점까지 모든 정점을 딱 1회씩만 방문하기 위해 위상정렬 알고리즘을 응용한다.
어떤 정점을 방문했을 때, order의 (a, b)쌍 중 a방일 경우, after[a]에 저장된 b들의 before를 1씩 내려준다.
모두 내려주고 나서 a방을 after에서 제거하여 after의 크기를 줄여준다.

만약 다음에 방문할 b의 before가 0이라면 이제 방문할 수 있는 방이라는 뜻이다.
그러나 2번 고려사항에 의해 b방에 before가 0이 되기 전에 방문했던 기록이 chk에 남아 있다면, 큐에 b방을 그냥 넣어준다.
chk에 방문 기록이 남겨져 있다는 뜻은 어떤 경로로든 a방 이후 b방을 들릴 수 있다는 의미이기 때문이다.
BFS 순회 방식에 의해 자연스럽게 b방 하위의 방도 탐색하게 되며 모든 정점을 1회만 방문하고도 모든 순서를 확인할 수 있다.
'''
