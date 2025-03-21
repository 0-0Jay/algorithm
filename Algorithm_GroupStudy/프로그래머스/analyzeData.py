# 프로그래머스 - 데이터 분석 : https://school.programmers.co.kr/learn/courses/30/lessons/250121

def solution(data, ext, val_ext, sort_by):
    cmd = {'code' : 0, 'date' : 1, 'maximum' : 2, 'remain' : 3}
    answer = sorted([i for i in data if i[cmd[ext]] < val_ext], key=lambda x : x[cmd[sort_by]])
    return answer

# 알고리즘 : 구현
'''
풀이 : 딕셔너리를 활용해 if문 없이 명령어를 인덱스로 변환한다.
딕셔너리를 만들고 데이터 각 명칭을 key, 인덱스를 value로 저장한다(cmd).
이렇게 하면 if문 없이 단순 반복문으로 answer를 채울 수 있다.
정렬은 sort_by열을 기준으로 정렬하기때문에 key에 lambda식을 활용해 정렬 조건을 넣어준다.
이 때, 위에서 만들었던 cmd에 sort_by를 찾아 value를 가져오면 된다.
배열에서 ext열의 값이 val_ext 미만인 데이터를 찾을 때도 같은 방법으로 찾아올 수 있다.
'''
