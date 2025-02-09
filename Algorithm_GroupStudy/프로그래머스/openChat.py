# 프로그래머스 - 오픈채팅방 : https://school.programmers.co.kr/learn/courses/30/lessons/42888

def solution(record):
    chat = {}
    uid = {}
    cnt = 0
    for i in range(len(record)):
        tmp = record[i].split(" ")
        if tmp[0] == "Enter":
            uid[tmp[1]] = tmp[2]
            if tmp[1] not in chat : chat[tmp[1]] = []
            chat[tmp[1]].append((cnt, 1))
            cnt += 1
        elif tmp[0] == "Leave":
            chat[tmp[1]].append((cnt, 0))
            cnt += 1
        else:
            uid[tmp[1]] = tmp[2]
            
    answer = ["" for i in range(cnt)]        
    for k, lst in chat.items():
        for id, io in lst:
            res = "들어왔습니다." if io == 1 else "나갔습니다."
            answer[id] = uid[k] + "님이 " + res
            
    return answer

# 알고리즘 : 해시
'''
풀이 : 해시 자료구조인 딕셔너리를 활용해 uid를 키값으로 닉네임값과 출입순서를 기록한다.
문제에서 주어진 record가 10만 길이까지 주어지기 때문에, 이 record대로 answer를 계속 수정하면 반드시 시간초과가 발생할 것이다.

우선 두개의 딕셔너리를 만들고, 인덱스로 활용할 변수(cnt)를 선언한다.
- uid : uid의 현재 닉네임을 기록할 딕셔너리
- chat : uid의 출입 인덱스(cnt)와 출입 여부(1 : 입장, 0 : 퇴장)를 기록할 딕셔너리

record를 처음부터 순서대로 탐색한다.
문자열의 첫 단어가 Enter라면, 일단 uid에 닉네임을 기록한다.
chat에 해당 uid가 없다면, uid키를 추가하고, 값으로 리스트를 둔 뒤, (cnt, 1)을 추가한다.
문자열의 첫 단어가 Leave라면, chat[uid]에 (cnt, 0)을 추가한다.
chat에 값이 추가될 때마다 cnt를 +1해준다.
문자열의 첫단어가 Change라면, uid에서 해당 유저 id의 닉네임을 바꿔준다.
이렇게 하면, 닉네임을 바꿀때마다 모든 채팅의 문자열을 변경할 필요 없이 닉네임만 따로 변경할 수 있다.

answer를 cnt만큼의 길이로 배열을 선언한다.
chat에서 유저 id(k) 별로 기록된 출입여부 리스트(lst)를 꺼내 answer를 채운다.
lst의 각 원소는 (인덱스, 출입여부)로 저장되어 있기 때문에, answer[id]에 출입여부에 따른 문자열을 저장하면된다.
- answer[id] = uid[k] + (io가 1이면 "들어왔습니다.", 0이면 "나갔습니다."
'''
