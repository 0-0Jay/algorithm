# 프로그래머스 2018 카카오 블라인드채용 - [3차] 압축 : https://school.programmers.co.kr/learn/courses/30/lessons/17684

def solution(msg):
    answer = []
    dict = {}
    for i in range(65, 91):
        dict[chr(i)] = i - 64
    id = 27
    key = 0
    while key < len(msg):
        tmp = msg[key]
        while tmp in dict:
            key += 1
            if key == len(msg): 
                answer.append(dict[tmp])
                return answer
            tmp += msg[key]
        answer.append(dict[tmp[:len(tmp) - 1]])
        dict[tmp] = id
        id += 1

# 알고리즘 : 구현
'''
풀이 : 각 글자가 사전에 있는지 없는지 검사하고, 있다면 한글자씩 추가해본다.
먼저 사전역할을 할 딕셔너리를 하나 생성하고, A ~ Z에 해당하는 숫자를 저장한다.
알파벳이 26자이기 때문에 다음에 딕셔너리에 추가되는 단어는 27번 인덱스부터 출발한다.(id)
key 값으로 0번을 지정해두고, key를 한 칸 씩 옮겨가며 msg를 순회한다.

탐색 순서는 다음과 같다.
1. 현재 key값의 글자를 뽑는다.(tmp)
2. tmp가 사전에 있다면, key 값을 한칸 옮기고, 해당 key값에 위치한 글자를 tmp에 추가한다.
3. 2번 과정을 tmp가 사전에 없을 때까지 반복한다.
4. tmp가 사전에 없으면, tmp를 사전에 추가하고 id값을 부여한 후, id를 1 올려준다.
5. tmp에서 마지막 글자를 제외한 단어를 answer에 추가한다.
6. 만약 key가 msg의 마지막 글자까지 이동했다면, 현재 저장된 tmp의 값을 사전에서 뽑아 answer에 추가한 후, answer를 반환한다.
'''
