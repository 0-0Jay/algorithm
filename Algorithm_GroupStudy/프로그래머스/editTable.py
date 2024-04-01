# 프로그래머스 2021 카카오 채용연계형 인턴십 - 표 편집 : https://school.programmers.co.kr/learn/courses/30/lessons/81303

def solution(n, k, cmd):
    answer = ''
    vertex = []
    rollback = []
    for i in range(n):
        bef = i - 1 if i > 0 else None
        aft = i + 1 if i < n - 1 else None
        vertex.append([bef, aft])

    for c in cmd:
        tmp = list(c.split(" "))
        if tmp[0] == 'D':
            for i in range(int(tmp[1])):
                k = vertex[k][1]
        elif tmp[0] == 'U': 
            for i in range(int(tmp[1])):
                k = vertex[k][0]
        elif tmp[0] == 'C':
            rollback.append(k)
            a, b = vertex[k]
            if a != None: vertex[a][1] = b
            if b != None: 
                vertex[b][0] = a
                k = b
            else: k = a
        else:
            id = rollback.pop()
            a, b = vertex[id]
            if b != None: vertex[b][0] = id
            if a != None: vertex[a][1] = id
    chk = set(rollback)                    
    for i in range(n):
        answer += 'O' if i not in chk else 'X'
            
    return answer

# 알고리즘 : 링크드 리스트 구현
'''
풀이 : 링크드 리스트를 구현하여 명령어에 따라 간선을 조정한다.
각 정점 i에 대해 i-1 정점과 i+1 정점으로 간선을 연결하여 초기 링크드 리스트를 구성한다.
위 코드에서는 vertex배열의 0번은 이전, 1번은 다음 정점을 의미한다.

D, U의 경우, 뒤에 함께 오는 숫자 a만큼 아래 또는 위로 이동하는 명령이다.
이 때, 단순히 k를 +a해버리면 중간에 숫자가 삭제된 경우, k가 삭제된 행을 가르키게 된다.
따라서 반복문을 활용해 다음 노드로 이동하는 과정을 a만큼 반복하는 방식으로 구현해야 한다.

C의 경우, 해당 위치의 정점을 제거하는 명령이다.
이 때, 실제로 간선의 삭제를 수행하게 되면 배열 사이즈 변경과 인덱스 조정과정에 의해 어마어마한 시간을 소요하게 된다.
따라서 링크드 리스트의 장점인 데이터 삽입/삭제의 효율성을 이용한다.
링크드 리스트에서 데이터 삭제는 단순히 현재 인덱스와 연결된 두 정점 a, b와의 간선을 끊고, a와 b를 연결해주면 된다.
삭제한 정점은 rollback 배열에 stack으로 쌓는다.
ex) 1 - 2 - 3에서 2를 제거하는 경우
1 2 3            1 2 3
x 1 2   ----->  x 1 1  => 제거하는 2에 대한 간선정보는 이후 롤백과정을 위해 수정하지 않는다.
2 3 x            3 3 x
정점 제거가 끝났다면, 방금 제거한 정점이 전체 리스트에서 마지막 정점인지 확인하여 k를 조건대로 옮겨준다.

Z의 경우, 가장 최근 삭제 데이터에 대한 롤백 명령이므로 C명령을 반대로 수행한다.
rollback에서 가장 위에 위치한 값 id를 뽑아 의 vertex 정보를 보면 삭제되기 전에 연결되어 있던 정점 정보가 존재한다.
저장되어 있는 두 정점의 연결을 끊고 중간에 id로 다시 연결해준다.
ex) 1 - 3  (2)에서 2를 다시 연결하는 경우
1 2 3                                                                                             1 2 3
x 1 1  -----> 2와 연결되어있던 정점 1, 3의 다음/이전 정점을 2로 수정 -----> x 1 2
3 3 x                                                                                             2 3 x

모든 명령어를 수행했다면, rollback 스택에 남아있는 정점들이 곧, 삭제되어 복구되지 않은 행들이다.
0번 정점부터 n-1번 정점까지 rollback 스택에 없으면 'O', 있으면 'X'로 기록한다.
'''
