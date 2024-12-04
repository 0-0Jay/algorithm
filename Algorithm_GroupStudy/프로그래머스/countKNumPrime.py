# 프로그래머스 2022 카카오 블라인드 채용 - k진수에서 소수 개수 구하기 : https://school.programmers.co.kr/learn/courses/30/lessons/92335#

import math

def chkPrime(n):
    if n < 2: return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0 : return False
    return True

def changeNum(n, k):
    if n < k: return str(n)
    return changeNum(n // k, k) + str(n % k)

def solution(n, k):
    answer = 0
    kNum = changeNum(n, k).split("0")
    chk = set()
    for num in kNum:
        if num in chk or num.isalnum() and chkPrime(int(num)): 
            answer += 1
            chk.add(num)
    return answer

# 알고리즘 : 구현
'''
풀이 : 진법변환, 소수판별 알고리즘을 구현한다.
에라토스테네스의 체를 사용할 수도 있지만, 진법 변환의 특성상 불필요한 숫자들 까지 소수판별을 해두기 때문에 더 효율적인 방법이 필요하다.
어떤 수가 소수인지 판별할 때는 2부터 그 수의 제곱근까지의 범위만 확인하면 효율적으로 판별할 수 있다.

일단 주어진 n을 k진법으로 변환한 후, 0을 기준으로 split하여 배열(kNum) 하나를 만든다.
kNum을 전부 순회하되, split()함수의 특징에 따라 빈 문자열이 들어있을 수 있음에 유의한다.
-> 예를 들어, 10000이라는 문자열을 '0'을 기준으로 스플릿하면 ['1', '', '', '', ''] 이 만들어진다.
따라서 분할된 문자열이 숫자인지 isalnum을 통해 확인하고, 숫자가 맞으면 소수판별을 한다.
이 과정에 서 빈 문자열은 숫자가 아니므로 걸러진다.

소수 판별을 할 때도 이미 소수임이 판별된 숫자를 또 판별하는 것은 비효율적이므로 chk 집합을 하나 두고, 소수가 판별될때마다 기록해둔다.
이 후, 어떤 숫자가 chk 집합에 존재한다면, chkPrime 함수로 확인하지 않아도 소수임을 알 수 있다.
이런 방식으로 kNum의 모든 숫자에 대해 소수면 answer에 1씩 추가한다.
'''
