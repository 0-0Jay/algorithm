# 백준 22981번 휴먼 파이프라인 : https://www.acmicpc.net/problem/22981

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [0] + sorted(list(map(int, input().split())))
max_num = 0

for i in range(1, n):
    now = i * arr[1] + (n - i) * arr[i + 1]
    if now > max_num: max_num = now

print(m // max_num if m % max_num == 0 else m // max_num + 1)

# 알고리즘 : 그리디
'''
풀이 : 각 사람의 분당 작업 속도를 오름차순 정렬한 뒤, 1명씩 팀을 옮겨가며 가장 큰 팀 작업 속도를 내는 지점을 찾는다.
1번 사람부터 i번 사람까지 a팀, i + 1번 사람부터 n번 사람까지 b팀으로 나눈다면, 각 팀의 작업속도는 다음과 같다.
a = i * arr[1]
b = (n - i) * arr[i + 1]
두 팀의 작업속도의 합이 클 수록 상자를 가장 빨리 옮길 수 있다.
따라서 m / max_num한 값을 1의 자리까지 올림한 값이 정답이 된다.

# python에서 그냥 ceil을 쓰면 오답처리되는 이유
math.ceil 함수는 주로 float 자료형을 처리하도록 설계되어 있다.
그러나 float 자료형은 수식 계산에 있어서 정확한 계산 결과가 아닌 오차가 존재한다.
다음 코드를 실행해보면 알 수 있다.

num = 0
for i in range(100):
    num += 0.1
print(num)

num에 0.1을 100번 더했다면 출력값은 당연히 10.0이어야 한다.
그러나 실제 출력값은 9.99999999999998이 출력된다.
만약 m / max_num의 계산 값이 2지만, 코드의 실행 결과가 2.00000000000001이라면, ceil 함수를 썼을때 3이 출력된다.
이 때문에 ceil을 사용할 때 decimal 모듈의 Decimal을 사용하는 것이 정확도를 더 높일 수 있다.
(위 코드에서는 직접 계산하는 방식으로 AC를 받았으나, 이도 정확한 부동소수 계산이라고 할 수 없다.)
'''
