# 프로그래머스 2019 KAKAO BLIND RECRUITMENT : 길 찾기 게임

import sys
sys.setrecursionlimit(1000000)

def solution(nodeinfo):
    # nodeinfo 에 각 노드 번호 삽입 후 1번 인덱스 기준으로 정렬
    sz = len(nodeinfo)
    for i in range(sz):
        nodeinfo[i].append(i + 1)
    nodeinfo.sort(key = lambda x : (-x[1], x[0] ))    
    
    answer = [[],[]]

    def tree(arr):
        if len(arr) == 0: return
        node = arr[0]  # 배열이 정렬되어 있으므로 0번 인덱스는 항상 부모
        left = []
        right = []
        for i in range(1, len(arr)):
            if node[0] > arr[i][0]:  # 부모 노드를 기준으로 왼쪽
                left.append(arr[i])
            else:  # 오른쪽
                right.append(arr[i])
        answer[0].append(node[2]) # 전위 탐색을 위해 재귀 호출 전에 나열
        tree(a)
        tree(b)
        answer[1].append(node[2]) # 후위 탐색을 위해 재귀 호출 후에 나열
        return;
        
    tree(nodeinfo)               
    return answer

# 알고리즘 : 이진 트리 탐색
'''
풀이 : 주어진 노드 정보를 정렬 후, 좌측에 위치한 노드와 우측에 위치한 노드들로 나누어가면서 탐색한다.

노드 정보를 1번 인덱스를 기준으로 내림차순, 1번 인덱스가 같다면 0번 인덱스를 기준으로 오름차순 정렬한다.
이 후, 정렬된 노드 정보를 재귀함수로 탐색하는데, 절차는 다음과 같다.
1. 배열의 0번을 현재 노드로 둔다.
  1-1. 이전에 노드정보를 정렬했기 때문에 매 탐색에서 0번 인덱스는 항상 부모 노드가 된다.
2. 배열의 1번 인덱스부터 탐색하며 현재 노드의 x좌표보다 작은 것은 left에, 큰것은 right에 append한다.
  2-1. append 함수로 배열에 추가하기 때문에 left 배열과 right 배열 또한 정렬상태다.
  2-2. 문제에서 이진트리라고 명시해두었기 때문에 left와 right만 있으면 된다.
3. 1-2를 최대깊이까지 반복한다.

이 때, 전위탐색의 결과와 후위탐색의 결과는 재귀함수에서 함수의 호출지점과 answer에 append하는 지점을 조절하는 것으로 구현할 수 있다.
전위 탐색은 다음 재귀(노드)가 호출되기 전에 현재 노드를 탐색하고, 왼쪽부터 탐색을 수행한다.
따라서 현재 노드를 answer에 넣는 과정을 재귀 호출 전에 작성한다.
후위 탐색은 다음 재귀를 호출한 후에 현재 노드를 탐색하기 때문에 재귀 호출 후에 작성한다.
'''
