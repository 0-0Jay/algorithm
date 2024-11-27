# 프로그래머스 - 주식가격 : https://school.programmers.co.kr/learn/courses/30/lessons/42584?language=python3

def solution(prices):
    answer = [len(prices) - i - 1 for i in range(len(prices))]
    stk = []
    for i in range(0, len(prices)):
        if not stk or prices[stk[-1]] <= prices[i]: 
            stk.append(i)
        else:
            while stk and prices[stk[-1]] > prices[i]:
                tmp = stk.pop()
                answer[tmp] = i - tmp
            stk.append(i)
    return answer

# 알고리즘 : 스택
'''
풀이 : 스택에 인덱스를 저장하며 값을 비교하고, 가격이 떨어지는 구간이 발생하면 answer의 값을 갱신한다.
answer에 우선 가격이 한 번도 떨어지지 않았다고 가정하고 인덱스 역순으로 초기화한다.
prices의 0번 인덱스부터 탐색한다.
만약 스택이 비어있거나, prices에서 현재 탐색중인 인덱스(i)의 값이 스택의 top에 저장된 인덱스(tmp)의 값 이상이면, 스택에 현재 인덱스를 쌓는다.

그러나 prices[i]가 prices[tmp] 미만이면, i - tmp를 answer에 갱신하며 스택에 저장된 인덱스를 빼낸다.
위 과정을 prices[i]가 prices[tmp] 이상이 될때까지 반복한 후, i를 스택에 추가한다.
'''
