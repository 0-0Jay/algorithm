# 프로그래머스 - 시소 짝꿍 : https://school.programmers.co.kr/learn/courses/30/lessons/152996

import math
from collections import Counter

def solution(weights):
    weights = sorted(Counter(weights).items())
    answer = 0
  
    for i in range(len(weights)):
        for j in range(i, len(weights)) :
            if i == j and weights[i][1] > 1:
                answer += math.comb(weights[i][1], 2)
            elif weights[i][0] * 2 < weights[j][0]:
                break
            elif weights[i][0] * 3 == weights[j][0] * 2:
                answer += weights[i][1] * weights[j][1]
            elif weights[i][0] * 4 == weights[j][0] * 3:
                answer += weights[i][1] * weights[j][1]
            elif weights[i][0] * 2 == weights[j][0]:
                answer += weights[i][1] * weights[j][1]
                
    return answer

# 알고리즘 : 조합
'''
풀이 : 가능한 경우의 수를 최대한 압축해, 경우의 수를 센다.
주어진 weights 배열의 최대 크기가 10만이기 때문에 그대로 쓰게 되면 10만의 제곱만큼 경우의 수를 세게 된다.
따라서 Counter 함수를 통해, 같은 숫자의 경우 하나의 key값으로 두고, 그 숫자의 개수를 value로 짝지어 weights를 압축한다.
두 숫자 a, b가 있을 때, 이 두 숫자가 시소 짝꿍이라면, 다음에 또 a와 b가 뽑혀도 같은 계산을 할 것이기 때문이다.
이 방식을 활용하면 a의 개수 * b의 개수를 하면 a중 한개와 b중 한개를 뽑은 경우의 수를 한번에 계산할 수 있어 시간을 단축할 수 있다.
후에 if문에 일관성있게 계산을 적용하기위해 weights를 오름차순 정렬해준다.

weights에서 수를 하나씩 뽑는다.
방금전에 weights를 오름차순 정렬해두었기 때문에, 항상 현재 인덱스 이후의 값만 뽑으면 모든 경우의 수를 중복 탐색 없이 계산할 수 있다.
이 때, 반드시 자기 자신과도 짝을 지어야 하는데, 지금 뽑히는 수는 압축된 경우의 수이기 때문이다. 
즉, 같은 숫자가 여러 개 있을 수 있기 때문에 해당 숫자가 2개 이상이라면, value에 해당하는 개수에서 순서에 상관없이 2개를 뽑는 경우의 수를 answer에 추가한다.
주어진 거리가 2m, 3m, 4m이기 때문에 2:3, 3:4, 2:4(1:2)의 경우만 계산하면된다.
weights[i]가 weights[j]보다 무조건 작거나 같기 때문에(오름차순 정렬했기 때문) 항상 왼쪽에 더 큰 거리를 주면 된다.
조건의 무게 비례식이 성립한다면, weights[i]의 개수와 weights[j]의 개수를 곱해 answer에 추가한다.

이렇게 두번에 걸쳐 계산을 압축하게 되면, 최악의 경우 10만^2 만큼의 계산이 100~1000사이의 모든 경우의 수인 900^2만큼만 계산하기 때문에 시간을 획기적으로 단축할 수 있다.
모든 경우의 수를 계산했다면, answer를 반환한다.
'''
