# 프로그래머스 - 소수찾기 : https://school.programmers.co.kr/learn/courses/30/lessons/42839

from itertools import permutations
from math import sqrt
        
def solution(numbers):
    chk = set()
    for i in range(1, len(numbers) + 1):
        tmp = set(map("".join, permutations(list(numbers), i)))
        tmp = set(map(int, tmp))
        for num in tmp:
            flag = True
            if num < 2: continue
            for j in range(2, int(sqrt(num)) + 1):
                if num % j == 0:
                    flag = False
                    break
            if flag : chk.add(num)
    return len(chk)

# 알고리즘 : 순열 + 소수 판별 알고리즘
'''
풀이 : permutations를 이용해 만들 수 있는 모든 순열을 찾고, 그 순열이 소수인지 판별한다.
itertools의 permutations 함수로 어떤 숫자 그룹에서 n개의 숫자를 뽑아 만들 수 있는 모든 숫자의 경우의 수를 구할 수 있다.
다음 과정으로 숫자를 1개 뽑는 경우부터 numbers의 모든 수를 뽑는 경우까지 탐색한다.
1. 우선 i개의 숫자를 뽑아 tmp에 집합으로 저장한다. 이 과정에서 똑같은 순서와 조합의 숫자들이 뽑히는 경우가 1차적으로 걸러진다.
2. tmp에 뽑은 조합들을 나열해 정수값으로 만들어준다. 이 과정에서 앞 자릿수에 0이 들어가는 경우가 걸러진다. (ex : 11, 011, 0011)
3. tmp의 각 숫자들을 소수 판별 알고리즘을 활용해 소수인지 검사하고, 소수라면 chk에 옮겨준다.

소수 판별 알고리즘은 단순히 가장 작은 소수인 2부터 판별할 숫자(num)의 제곱근까지만 탐색하면 된다.
만약, num이 2보다 작다면 소수가 아니기때문에 continue문으로 걸러준다.
모든 탐색이 끝났다면, chk의 길이를 return 한다.
'''
