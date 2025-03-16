# 프로그래머스 - 햄버거 만들기 : https://school.programmers.co.kr/learn/courses/30/lessons/133502

def solution(ingredient):
    answer = 0
    stk = []
    key = 0
    for k in ingredient:
        stk.append(k)
        if len(stk) > 3 and stk[-4:] == [1, 2, 3, 1]:
            for i in range(4): stk.pop()
            answer += 1
            
    return answer

# 알고리즘 : 스택
'''
풀이 : 스택에 재료를 하나씩 쌓고, 햄버거가 완성되면 즉시 빼내고 answer에 +1한다.
재료를 하나씩 꺼내 쌓는다(stk).
stk의 길이가 4이상이고, 가장 위의 재료 4개가 1-2-3-1의 순서라면, 해당 4개를 pop하고 answer에 +1한다.
모든 재료에 대해 수행하고 answer를 반환한다.

이 때, 반드시 pop을 4번하는 방법을 사용한다.
슬라이싱을 통해 배열을 자르는 방식을 사용하면, 배열 복사가 수행되므로 시간초과가 발생할 수 있다.
'''
