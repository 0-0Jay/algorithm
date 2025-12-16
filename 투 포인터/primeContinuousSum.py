# 백준 1644번 소수의 연속합 : https://www.acmicpc.net/problem/1644

import sys
import math
sys.setrecursionlimit(100000)

n = int(input())
prime = [0 for _ in range(n + 1)]
prime[0], prime[1] = 1, 1

# 소수 판별 : 에라토스테네스의 체
for i in range(2, int(math.sqrt(n)) + 1):
    for j in range(i + i, n + 1, i):
        prime[j] = 1

# 소수 -> 누적합 변환        
num = [0]
for i in range(n + 1): 
    if prime[i] == 0: num.append(i + num[-1])

# 연속합 경우의 수 찾기
s, e = 0, 0
cnt = 0
while s <= e:
    now = num[e] - num[s]
    if now <= n: 
        if now == n: cnt += 1
        e += 1
    else:
        s += 1
    if e == len(num): break
    
print(cnt)

# 알고리즘 : 에라토스테네스의 체, 누적합, 투 포인터
'''
풀이 : 소수들의 누적합 배열을 이용해 투포인터로 인덱스를 이동시켜가며 경우의 수를 찾는다.
에라토스테네스의 체 알고리즘을 이용해 n까지의 모든 소수를 찾는다.
소수를 2부터 누적합을 구해서 num배열에 담는다.
s, e로 두개의 포인터를 이용해 num 배열을 탐색한다.
이때 num[e] - sum[s]가 곧 s번째 소수부터 e번째 소수까지의 연속합이 된다.
현재 합이 n보다 작거나 같으면 e를 +1 해서 값을 증가시키고, 크면 s를 +1해서 값을 줄인다.
n과 합이 같을 때도 e+1을 해야 모든 경우의 수를 탐색할 수 있다.
'''
