# 백준 11689번 GCD(n, k) = 1 : https://www.acmicpc.net/problem/11689

import math
import sys
input = sys.stdin.readline

n = int(input())
k = int(math.ceil(math.sqrt(n))) + 1
sieve = [1] * k
sieve[0] = 0
if n > 1: sieve[1] = 0
for i in range(2, k):
    if sieve[i] == 0: continue
    for j in range(i + i, k, i):
        sieve[j] = 0

cnt = 1
for i in range(2, k):
    if sieve[i] == 0: continue
    tmp = 0
    while n % i == 0:
        tmp += 1
        n //= i
    if tmp == 1: cnt *= i - 1
    else: cnt *= int(math.pow(i, tmp)) - int(math.pow(i, tmp - 1))
if n != 1: cnt *= n - 1
    
print(cnt)

# 알고리즘 : 오일러 피 함수 + 에라토스테네스의 체
'''
풀이 : 숫자를 소인수 분해 하며 오일러 피 함수의 법칙에 따라 최대공약수가 1인 수의 개수를 계산한다.
오일러 피 함수는 1부터 N까지의 범위에서 N과 서로소인 자연수의 개수를 구하는 함수다.
각 수가 소수인지 아닌지를 매번 탐색해도 되지만, 더 빠르게 판단하기 위해 에라토스테네스의 체를 활용한다.

오일러 피 함수를 설명하면 다음과 같다.
예를 들어, n을 나누어 떨어지게 만들 수 있는 수 i가 있다면, n을 i로 몇번 나눌 수 있는지 카운팅(tmp)한다.
이 때, tmp에 따라 두가지 방향으로 cnt에 곱해준다.
1. tmp가 1이라면, 단순히 카운트(cnt)에 i - 1을 곱한다.
2. tmp가 1보다 크다면, cnt에 i를 tmp만큼 제곱한 값에서 cnt에 i를 tmp-1만큼 제곱한 값을 뺀 값을 곱한다.

모든 계산이 끝났을 때 남은 n이 1이 아니라면, 이 남은 n은 소수다.
소수는 자기 자신으로 1회 나누면 1이 되므로 1번의 계산이 적용될 수 있다.
따라서 마지막으로 n - 1을 cnt에 곱해준다.
'''
