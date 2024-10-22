# 백준 14725번 개미굴 : https://www.acmicpc.net/problem/14725

import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n = int(input())
graph = {}
for _ in range(n):
    k = list(input().strip().split(' '))
    k[0] = 'root'
    parent = (0, k[0], '') # 층, 자신, 부모
    for i in range(1, len(k)):
        if parent not in graph: graph[parent] = set()
        graph[parent].add((i, k[i], parent))
        parent = (i, k[i], parent)

def DFS(node):
    if node not in graph: return
    now = sorted(graph[node], key = lambda x: x[1])
    for i in now:
        print("--" * (i[0] - 1) + i[1])
        DFS(i)
        
DFS((0, k[0], ''))

# 알고리즘 : 트라이(Trie)
'''
풀이 : 각 먹이 정보 트라이로 저장한다.
트라이 자료구조는 여러 문자열을 효율적으로 저장하고 탐색하는 자료구조다.
이 문제의 예제 입력 1번을 보면, A B C D 와 A C가 있다.
이 문자열은 A라는 부모 아래에 "B C D"라는 자식과 "C"라는 자식이 있는 트리로 표현할 수 있는데, 이것이 트라이 구조다.

각 행을 입력받아서(k) 첫번째 칸은 임의로 root로 지정한 뒤, 반복문을 통해 한칸씩 이동하며 트라이 구조를 만들어 준다.
이 때, 각 노드는 (층, 자신, 부모의 정보)를 저장해야 한다.
부모의 정보는 단순히 자신의 바로 윗층이 무슨 정보인지만 포함하는 것이 아니다.
root부터 시작되어 어떤 경로로 온 부모인지가 모두 저장되어야 한다.
따라서 parent라는 변수를 두고, 계속 정보를 누적시키며 자식으로 이동시킨다.

트라이를 완성했으면, 일반 트리 탐색하듯 DFS로 전위순회하며 양식에 맞게 출력한다.
이 때, 각 층을 사전순으로 정렬해야 하기 때문에 set로 저장된 정보를 sorted로 사전순 정렬된 리스트로 변환해준다.
'''
