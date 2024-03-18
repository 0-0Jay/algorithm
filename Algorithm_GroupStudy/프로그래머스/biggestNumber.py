# 프로그래머스 가장 큰 수 : https://school.programmers.co.kr/learn/courses/30/lessons/42746

from functools import cmp_to_key

def solution(numbers):
    def cmp(x, y):
        if int(x + y) > int(y + x): return -1
        return 1
    
    return str(int(''.join(sorted([str(i) for i in numbers], key=cmp_to_key(cmp)))))

# 알고리즘 : 정렬
'''
풀이 : 정렬기준을 직접 구현한다.
일반적인 문자열 정렬을 사용하면 맨 앞 문자가 사전순으로 정렬되고, 문자열 길이가 짧을수록 먼저 정렬된다.
대부분의 상황이라면 이 방법으로 정렬 후 뒤집었을 때 가장 큰 문자열을 만들 수 있지만, 반례가 존재한다.
문제의 예제 케이스중 일부인 3과 30이 이에 해당한다.
정렬 후 뒤집었을때 일반 문자열 정렬의 결과는 303이 된다. 
왜냐하면 맨 앞 문자가 같은데 3의 길이가 작기 때문이다.
그러나 실제로 303보다 330이 더 큰숫자이므로 이 경우 반대로 정렬되어야 한다.
이를 위해 두 개의 숫자가 들어오면 두숫자를 정순으로 합친 값과 역순으로 합친 값을 놓고 더 큰 숫자를 만드는 순서로 정렬한다.
'''
