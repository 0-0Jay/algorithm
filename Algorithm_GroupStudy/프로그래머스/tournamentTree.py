# 프로그래머스 예상 대진표 : https://school.programmers.co.kr/learn/courses/30/lessons/12985

import math

def solution(n,a,b):
    logn = 2 ** math.ceil(math.log2(n))
    A = logn + a - 1
    B = logn + b - 1
    cnt = 0
    while A != B:
        A //= 2
        B //= 2
        cnt += 1        
    return cnt

# 알고리즘 : 이진 트리
'''
풀이 : 이진 트리의 부모 탐색 방식을 응용한다.
주어진 N에 대해 대진표를 그릴 때, 가장 아래 라운드의 최대 인원수(logn)를 구한다.
예를 들어 5명이 참가하는 대진표를 그릴 경우, 이진 트리에서 가장 아래 라운드의 최대 인원수는 8명이다.
이 때, 이진 트리의 특징상 logn번째 인덱스부터 가장 아래 라운드에 사람을 채워넣기 때문에, A와 B를 이 인덱스로 치환한다.
A와 B가 같아질 때까지 2로 나누면서 라운드를 카운팅한다.
'''
