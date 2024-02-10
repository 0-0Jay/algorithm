# 백준 1744번 수 묶기 : https://www.acmicpc.net/problem/1744

import sys
input = sys.stdin.readline

n = int(input())
plus = []
minor = []
for i in range(n):
    tmp = int(input())
    if tmp > 0: plus.append(tmp)
    else: minor.append(tmp)
plus.sort()
minor.sort(reverse = True)
sum = 0
while plus:
    a = plus.pop()
    b = -1 if len(plus) == 0 else plus.pop()
    if a > 1 and b > 1: sum += a * b
    elif a == 1 and b != -1 or b == 1: sum += a + b
    else: sum += a
while minor:
    a = minor.pop()
    b = 1 if len(minor) == 0 else minor.pop()
    sum += a * b
print(sum)

# 알고리즘 : 그리디
'''
풀이 : 양수 그룹과 (음수와 0) 그룹으로 나눈 후, 절대값이 큰 값부터 두개씩 묶어서 곱하여 합한다.
단, 예외상황이 2가지 있고, 그 해결 방안은 다음과 같다.

1. 두 수중 하나가 1인 경우
양수 그룹에서 두 수 중 하나가 1인 경우 곱하는 것 보다 더하는 것이 값이 더 크기때문에 이 때는 값을 더해준다.
음수 그룹에서는 고려하지 않아도 된다.

2. 각 그룹의 크기가 홀수인 경우
양수 그룹 같은 경우 곱셈에 영향을 주지 않기 위해 b를 1로 두면 덧셈으로 계산되어 버리므로 -1로 임의 설정 해준다.
만약 b가 -1이라면 뽑힌 수가 a 하나라는 뜻이므로 그냥 sum에 누적해준다.
음수 그룹의 경우는 곱셈에 영향을 주지 않기 위해 b를 1로 두어도 된다. 
만약 b가 1이라면 뽑힌 수가 a 하나고, 1은 음수 곱셈에 영향을 주지 않으므로 a * b를 해도 무관하다.
'''
