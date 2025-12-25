# 백준 17436번 소수의 배수 : https://www.acmicpc.net/problem/17436

import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n, m = map(int, input().split())
arr = list(map(int, input().split()))
total = 0

def calc(now, bef, d):
    global total
    if d % 2 != 0: total += m // now
    elif now > 1: total -= m // now
    
    for i in range(bef + 1, n):
        calc(now * arr[i], i, d + 1)
        
calc(1, -1, 0)
print(total)

# 알고리즘 : 포함 배제의 원리
'''
풀이 : 홀수 개의 묶음에 대한 갯수는 더하고 짝수 개의 묶음에 대한 갯수는 뺀다.
합집합과 교집합을 활용한 계산을 활용한다.
A집합과 B집합의 합집합의 원소 개수는 n(A) + n(B) - n(A&B)가 된다.
예를 들어 2번 예제의 경우, 100보다 작은 수 중 2의 배수는 50개, 3의 배수는 33개, 6의 배수는 16개이다.
즉, 50 + 33 - 16으로 67개가 된다.
3번 예제의 경우는 2의 배수 50개, 3의 배수 33개, 5의 배수 20개이다.
이 때, 2*3의 배수 중에 5의 배수, 3*5의 배수 중 2의 배수, 2*5의 배수 중 3의 배수의 개수가 빼지면서 2*3*5의 배수가 추가로 빠진다.
이를 위해 2*3*5의 배수의 갯수를 더해주어야 한다.
위 조건들을 살펴 보면 짝수 개의 수면 빼고, 홀수 개면 더한다는 규칙을 찾을 수 있다.
이것이 포함 배제의 원리이다.
'''
