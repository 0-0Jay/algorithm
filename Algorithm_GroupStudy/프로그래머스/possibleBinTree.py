# 프로그래머스 2023 카카오 블라인드 채용 - 표현 가능한 이진트리 : https://school.programmers.co.kr/learn/courses/30/lessons/150367

import math

def solution(numbers):
    def checkTree(tree, left, right, chk):
        mid = (left + right) // 2
        if chk == 0 and tree[mid] == '1': return 0
        if left == right: return 1
        if tree[mid] == '0': chk = 0
        return checkTree(tree, left, mid - 1, chk) & checkTree(tree, mid + 1, right, chk)
    
    answer = []
    for now in numbers:
        if now == 0: answer.append(0); continue
        tmp = str(bin(now))[2:]
        n = len(tmp)
        logn = 2 ** (int(math.log2(n)) + 1) - 1
        tmp = tmp.zfill(logn)
        answer.append(checkTree(tmp, 0, logn - 1, 1))
    return answer

# 알고리즘 : 트리 순회
'''
풀이 : 중위 순회의 특징을 이용해 트리를 구성할 수 있는지 판별한다.
주어지는 숫자를 이진수로 바꾼 결과는 문제 내용상 중위 순회의 결과물이다.
따라서 mid 값을 부모 노드로 잡고 좌우를 각각 이진 트리의 자식 서브 트리로 봐야한다.

우선, 각 숫자를 트리 탐색을 하기 위해 이진 트리를 리스트로 변환 했을 때의 길이 규칙에 따를 필요가 있다.
이진트리는 각 깊이마다 2^(깊이 - 1)만큼의 원소를 가질 수 있기 때문에, 트리의 크기를 2 ** (int(math.log2(n)) + 1)로 잡는다.(logn)
이 후, 트리 탐색을 위해 tmp의 자릿수가 logn이 되게끔 왼쪽을 0으로 채워준다.

tree와 tree의 왼쪽 끝과 오른쪽 끝의 인덱스, 부모의 숫자를 체크할 chk를 파라미터로 트리탐색을 수행한다.
만약 부모가 0인데(chk == 0), 현재 노드(tree[mid])가 1이라면, 부모가 없는 자식 노드가 발생했으므로 0을 리턴한다.
왼쪽 끝의 인덱스와 오른쪽 끝의 인덱스가 같다면, 더 이상 자식이 없는 리프 노드이므로 문제 없다는 뜻의 1을 리턴한다.
만약 현재 노드가 0이면 chk를 0으로 바꿔주고 자식 노드를 재귀로 탐색한다.
이 때, 왼쪽 자식의 결과와 오른쪽 자식 결과 중에 하나라도 0이 있다면 트리로 만들 수 없다.
리턴 값이 0과 1만 있으므로 두 자식 결과를 비트 and 연산한 결과 값을 최종 반환한다.
'''
