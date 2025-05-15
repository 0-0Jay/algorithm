# 프로그래머스 - 괄호 회전하기 : https://school.programmers.co.kr/learn/courses/30/lessons/76502

def solution(s):
    cnt = 0
    for i in range(len(s)):
        s = s[1:] + s[:1]
        stk = []
        left = set(['(', '[', '{'])
        flag = 0
        for p in s:
            if p in left:
                stk.append(p)
            elif stk:
                if p == ')' and stk[-1] == '(':
                    stk.pop()
                elif p == '}' and stk[-1] == '{':
                    stk.pop()
                elif p == ']' and stk[-1] == '[':
                    stk.pop()
                else:
                    flag = 1
                    break
            else:
                flag = 1
                break
        if flag == 0 and not stk:
            cnt += 1
    return cnt

# 알고리즘 : 스택
'''
풀이 : 괄호 문자열의 첫 글자를 마지막 글자로 하나씩 옮겨가며 스택으로 올바른 괄호 문자열인지 확인한다.
다음과정을 반복한다.
1. 주어진 문자열의 0번 인덱스를 마지막 인덱스로 옮긴다.
2. 변환한 문자열의 0번 인덱스부터 왼쪽 괄호면 스택에 넣고, 오른쪽 괄호면 스택의 top과 비교한다.
3. 짝이 맞는 괄호면 스택의 top을 pop하고, 한 번이라도 짝이 안맞으면 flag를 동작한다.
4. 만약 flag가 0이고 stk에 남은 괄호가 없으면 카운트를 1 증가시킨다.
주어진 괄호 문자열의 길이만큼 반복한 후 cnt를 출력한다.
'''
