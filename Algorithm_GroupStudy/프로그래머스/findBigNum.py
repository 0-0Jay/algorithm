# 프로그래머스 - 뒤에 있는 큰 수 찾기 : https://school.programmers.co.kr/learn/courses/30/lessons/154539

def solution(numbers):
    answer = [-1] * len(numbers)
    stk = []
    for i in range(len(numbers) - 1, -1, -1):
        while stk and numbers[i] >= stk[-1]:
            stk.pop()
        if stk: answer[i] = stk[-1]
        stk.append(numbers[i])
    return answer

# 알고리즘 : 스택
'''
풀이 : 뒤에서 부터 스택을 활용해 숫자를 쌓고, 현재 수와 비교한다.
우선 answer를 -1로 채운다. 
스택을 활용한 풀이에서 현재 수보다 뒤에있는 수가 모두 작을 경우, 스택의 숫자들이 전부 빠져나올 것이기 때문에 해당 인덱스에 -1이 채워져야 하기 때문이다.
그렇지 않은 경우는 스택의 top에 있는 숫자로 갱신해 주면 된다.
먼저, 스택이 비어있지 않고, 현재 숫자가 스택의 top보다 작아질 때까지 스택의 수를 뻬낸다.
answer의 현재 인덱스에 스택의 top에 있는 숫자로 교체하고, 스택에 현재 숫자를 쌓는다.
이렇게 하면, 스택은 내림차순으로 숫자가 차게 된다.
이 후, 현재 숫자가 스택의 top보다 큰수가 나오면, 위의 과정을 반복하기 때문에, 자연스럽에 뒤에있는 큰 수를 찾을 수 있다.
'''
