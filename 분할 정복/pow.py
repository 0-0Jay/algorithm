# 백준 1629번 곱셈 : https://www.acmicpc.net/status?user_id=youngjin2712&problem_id=1629&from_mine=1

import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())
def mult(a, n):
    if n == 1:
        return a
    half = mult(a, n // 2)
    if n % 2 == 0: 
        return half ** 2 % c
    else: return half ** 2 % c * a % c
    
print(mult(a, b) % c)

# 알고리즘 : 분할정복
'''
풀이 : 분할정복을 이용해 제곱을 계산한다.
일반적인 제곱은 O(n^2)이다.
제곱 시간복잡도가 (n)이고, 이 곱셈을 제곱수 만큼 반복(n)하기 때문이다.
ex) a * a = a^2 -> a^2 * a = a^3 -> ..... -> a^9 * a = a^10
         1회                 2회                              10회

a의 b제곱을 분할정복으로 접근하면 다음과 같다.
1. b가 짝수인 경우 : a의 (b // 2)제곱을 제곱한 값 ex) a^10 = a^5 * a^5
2. b가 홀수인 경우 : a의 (b // 2)제곱을 제곱한 값에 a를 한번 더 곱한값 ex) a^11 = a^5 * a^5 * a
ex) a^10 = a^5 * a^5 -> a^5 = a^2 * a^2 * a => a^2 = a * a
               1회                      2회                         3회

즉, 두 수의 곱셈에 대한 시간 복잡도(n)에 log2(제곱수)만큼만 반복하면(logn) O(nlogn)만에 제곱을 계산할 수 있다.
'''
