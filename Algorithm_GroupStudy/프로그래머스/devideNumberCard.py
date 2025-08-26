# 프로그래머스 - 숫자 카드 나누기 : https://school.programmers.co.kr/learn/courses/30/lessons/135807

def GCD(array):
    if len(array) == 1 : return array[0]
    m = len(array) // 2
    a = GCD(array[:m])
    b = GCD(array[m:])
    if a < b: a, b = b, a
    while b > 0:
        a, b = b, a % b
    return a

def solution(arrayA, arrayB):
    answer = [GCD(arrayA), GCD(arrayB)]
    for i in arrayA:
        if i % answer[1] == 0: answer[1] = 0;break
    for i in arrayB:
        if i % answer[0] == 0: answer[0] = 0;break
                    
    return max(answer)

# 알고리즘 : 유클리드호제법(GCD)
'''
풀이 : 각 배열의 최대 공약수를 구해 다른 배열에 대입해본다.
가지고 있는 카드들의 모든 수를 나눌 수 있다는 말은 해당 숫자들의 공약수를 구하라는 말과 같다.
최대 공약수를 구해서 상대 카드들에 하나씩 나누어 보았을 때, 나머지가 0이 한번이라도 나온다면 이 수는 문제의 조건에 맞지 않는다.
또, 최대공약수로 계산했을 때 조건에 맞지 않는다면 당연히 다른 공약수도 조건에 맞지 않는다.
즉 모든 공약수를 계산할 필요없이 최대 공약수 하나만 대입해보면 된다.

배열의 최대 공약수를 구하기 위해 유클리드 호제법을 사용한다.
주어진 배열을 반씩 나누어가며 2개씩 짝지어 최대 공약수를 구한다.
모든 수의 최대 공약수를 구했다면 이를 answer에 저장해둔다.
answer[0]에는 arrayA의 최대공약수를, answer[1]에는 arrayB의 최대공약수를 저장해두고 상대 배열에 대입한다.
한 번이라도 배열의 수가 나누어 떨어진다면 해당 answer의 값을 0으로 바꿔주고 break로 추가 탐색을 막는다.
두 배열에 각각 이를 수행했다면, 문제 조건에 따라 answer에 저장된 수 중 더 큰 값을 반환한다.
'''
