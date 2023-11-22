# 백준 2143번 두 배열의 합 : https://www.acmicpc.net/problem/2143

from collections import deque
import sys
input = sys.stdin.readline

t = int(input())
n = int(input())
Aarr = [0] + list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))
Barr = {}
res = 0

for i in range(1, n + 1):
    Aarr[i] += Aarr[i - 1] # A의 누적합
for i in range(m):
    sum = 0
    for j in range(i, m):
        sum += B[j]
        if sum not in Barr:
            Barr[sum] = 1
        else:
            Barr[sum] += 1
Barr = dict(sorted(Barr.items(), key = lambda x: x[0])) # B의 모든 부배열 쌍의 합

for i in range(n):
    for j in range(i + 1, n + 1):
        a_sub = Aarr[j] - Aarr[i];
        goal = t - a_sub
        if goal not in Barr : continue
        else:
            res += Barr[goal]
            
print(res)

# 알고리즘 : 누적합 + 딕셔너리
'''
풀이 : A의 누적합을 구해두고, i와 j 투포인터를 활용해 가능한 모든 부 배열 합을 구해서 Barr과 비교한다.
2중 for문을 통해 A에서 가능한 모든 부배열합을 구할 수 있다.
이를 Barr에서 탐색하기 위해 매 탐색마다 (t - A 부배열 합)을 goal로 둔다.
사전에 Barr에 B에서 나올 수 있는 모든 부 배열합을 key값으로 하는 딕셔너리를 만들고, 해당 값이 얼마나 나오는지를 value값으로 한다.
goal이 Barr에 존재하는 key값이면 그 value를 res에 누적한다.
'''
