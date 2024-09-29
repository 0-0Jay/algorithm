# 프로그래머스 2018 카카오 블라인드 채용 - [1차] 뉴스 클러스터링 : https://school.programmers.co.kr/learn/courses/30/lessons/17677?language=python3

def multiset(s):
    res = []
    s = s.lower()
    for i in range(len(s) - 1):
        tmp = s[i] if 97 <= ord(s[i]) <= 122 else ''
        tmp += s[i + 1] if 97 <= ord(s[i + 1]) <= 122 else ''
        if len(tmp) == 2: res.append(tmp)
    return res

def solution(str1, str2):
    sub_str1 = multiset(str1)
    sub_str2 = multiset(str2)
    inter = []
    union = len(sub_str1) + len(sub_str2) 
    chk = set()
    for i in sub_str1:
        for j in range(len(sub_str2)):
            if i == sub_str2[j] and j not in chk:
                chk.add(j)
                inter.append(i)
                union -= 1
                break
    answer = 65536 if len(sub_str1) == 0 and len(sub_str2) == 0 else int((len(inter) / union) * 65536) 
    return answer

# 알고리즘 : 구현
'''
풀이 : 모든 문자를 소문자로 변환후, 다중집합으로 가공하고, 교집합을 구한다.
문제에서 대소문자 구분이 없기 때문에 모든 문자를 소문자로 변환시킨다.
문자를 두 개씩 끊고, 두 문자가 모두 알파벳 소문자 범위에 들어가는지 확인 한 후, tmp에 저장한다.
만약 tmp의 길이가 2가 아니라면, 두 문자 중에 알파벳이 아닌 문자가 있다는 뜻이므로 다중집합에 포함시키지 않는다.

만들어진 다중집합(sub_str1, sub_str2)을 2중 반복문으로 완전탐색한다.
중복이 없는 집합이라면 집합연산자를 사용하겠지만, 중복이 허용되는 집합이기 때문에 배열 상태로 해결해야 한다.
합집합의 원소의 개수는 (두 집합의 원소의 개수 합)에서 (두 집합의 교집합의 원소의 개수)를 뺀 값이다.
따라서 두 집합의 원소의 개수 합을 union 변수에 초기값으로 저장하고, 교집합을 저장할 inter 배열을 선언한다.

두 다중 집합을 탐색하면서 같은 원소가 발견되면 해당 원소의 인덱스에 중복체크를 해두고 inter에 삽입한다.
인덱스로 중복 체크했기 때문에 같은 문자열이 다른 인덱스에 있다면, 중복 체크되지 않는다.
교집합의 원소의 개수를 빼주는 과정을 생략하기 위해 발견될 때마다 union에서 1씩 차감시킨다.

모든 탐색이 끝나면 union에는 합집합의 원소의 개수, inter에는 교집합이 저장되어 있다.
len(inter) / union한 값에 65536를 곱하고 정수로 변환시켜 소숫점을 날린다.
이 때, sub_str1과 sub_str2가 모두 공집합이라면 그냥 65536을 반환한다.
'''
