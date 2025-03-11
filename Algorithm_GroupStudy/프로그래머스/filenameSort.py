# 프로그래머스 2018 카카오 블라인드 채용 - [3차]파일명 정렬 : https://school.programmers.co.kr/learn/courses/30/lessons/17686#

import re

def solution(files):
    answer = []
    save = []
    for i in range(len(files)):
        name = files[i].lower()
        tmp = [j for j in re.split('([^0-9])', name) if j != '']
        tmp2 = ['', 0]
        for j in range(len(tmp)):
            if tmp[j].isdigit(): 
                tmp2[1] = int(tmp[j])
                tmp = tmp2
                break
            else:
                tmp2[0] += tmp[j]
        save.append((tmp, i))
    save.sort()
    for v, id in save:
        answer.append(files[id])
    return answer

# 알고리즘 : 정규표현식, 완전탐색
'''
풀이 : 파일명에서 tail에 해당하는부분을 잘라내고, 문자열과 숫자를 분리해 전처리 한다.
문제의 조건에 맞추어 모든 파일명을 정렬하기 위한 전처리를 수행한다.
먼저 대소문자 구분이 없기 때문에 소문자로 변환한다.
re의 split을 활용하는데, 문자열은 1개씩 분리하고, 여러자리 숫자는 합쳐서 하나의 숫자로 둔다.

1차적인 문자, 숫자 분리가 완료되었다면, head와 number로 정리하는 배열을 하나 만든다(tmp2)
문자열이면 tmp2[0]에 이어붙이고, 숫자면 tmp2[1]에 정수로 변환하여 저장한 후 save 배열에 저장한다.
모든 전처리 과정이 끝난 save 배열을 정렬한다.
이 때, save에 저장할때 (전처리 한 문자열, 원래 인덱스)의 방식으로 저장한다.
그래야 후에, 같은 순위를 가진 두 파일명에 대해 순서 그대로 정렬할 수 있다.
정렬이 끝난 save의 인덱스부분(id)을 순서대로 꺼내 files[id]의 문자열을 answer에 추가하여 반환한다.
'''
