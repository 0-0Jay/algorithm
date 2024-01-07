프로그래머스 2개 이하로 다른 비트 : https://school.programmers.co.kr/learn/courses/30/lessons/77885?language=python3

def solution(numbers):
    answer = []
    for i in numbers:
        if i % 2 == 0:
            answer.append(i + 1)
        else:
            tmp = bin(i)
            for j in range(len(tmp) - 1, -1, -1):
                if tmp[j] == '0':
                    tmp = tmp[:j] + '10' + tmp[j + 2:]
                    break
                elif tmp[j] == 'b':
                    tmp = tmp[:2] + '10' + tmp[3:]
                    break
            answer.append(int(tmp, 2))
    return answer

# 알고리즘 : 그리디
'''
풀이 : 숫자가 짝수면 +1 해주고, 홀수면 가장 작은 자릿수의 0을 바로 오른쪽 1과 교체한다.
숫자가 짝수일 경우 이진수로 변환하면 반드시 1의 자리 숫자가 0이므로 +1만 해주면 된다.
홀수일 경우, 이진수의 1의 자리부터 순차적으로 이동하다가 가장 먼저 만나는 0을 바로 오른쪽의 1과 교체하면된다.
ex) 1011 -> 1101
단, 홀수면서 모든 자리가 1인경우 가장 큰 자릿수의 1을 10으로 교체한다
ex) 111 -> 1011
'''
