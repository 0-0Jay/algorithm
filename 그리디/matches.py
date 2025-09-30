# 백준 3687번 성냥개비 : https://www.acmicpc.net/problem/3687

from collections import defaultdict, deque
import math
import heapq as hq
import sys
input = sys.stdin.readline

t = int(input())
arr = [-1, -1, 1, 7, 4, 2, 0, 8]
for test in range(t):
    n = int(input())
    tmp = n
    key = 1
    small, big = 0, 0
    while tmp > 13:
        tmp -= 7
        small = small * 10 + 8
        key *= 10
    res = 99
    for i in range(2, 8):
        a = arr[i] if arr[i] != 0 else 6
        b = arr[tmp - i] if 1 < tmp - i < 8 else None
        if tmp - i == 0:
            res = min(res, a)
        elif b != None:
            res = min(res, a * 10 + b)
    if res % 10 == 2 and small > 0:
        small %= key // 10
        res //= 10
        small += res * key * 10
    else: small += res * key
             
    tmp = n
    if tmp % 2 != 0:
        tmp -= 3
        big = 7
    while tmp > 1:
        big = big * 10 + 1
        tmp -= 2
         
    print(small, big)
    
# 알고리즘 : 그리디
'''
풀이 : 각 갯수별 최소숫자를 배열에 맵핑해두고, 숫자를 만든다.
먼저 가장 작은 수에 대해 2가지 규칙이 있고, 그에 따른 대응 방법은 다음과 같다.
1. 자릿수가 작을 수록 작은 수다. -> 최대한 많은 성냥을 사용하는 숫자를 많이 사용한다.
2. 높은 자리가 작을 수록 작은 수다. -> 숫자 두개를 만들었다면, 더 작은 수를 높은 자리에 배치한다.

위 두가지 규칙에 따라 각 성냥 갯수별로 만들 수 있는 가장 작은 숫자를 arr배열에 매핑해둔다.
가장 많은 성냥을 사용하는 숫자는 8이므로 남은 성냥의 개수가 14개 이상인지 확인하며 일의 자리부터 8을 채워나간다. (small)
남은 성냥의 개수가 14개 미만이면, a와 b에 숫자를 하나씩 만들어 두자릿수 ab를 만든 후 res와 최소값 비교 해본다.
만약 a에 숫자를 만들었는데, 남은 성냥이 있으나 2개 미만이라면, b에는 숫자를 만들 수 없기 때문에 계산하지 않는다.
a에 남은 성냥을 모두 사용해 숫자를 만들었다면 1번 규칙에 따라 2자리 수를 만들 필요없이 small의 제일 왼쪽에 붙여준다.

이 때, 예외적인 상황이 하나 발생한다.
숫자 가운데에 28이 발생하는 경우로 b가 2인 경우가 이에 해당한다.
28이라는 수는 5 + 7 으로 성냥 12개를 사용하는데, 똑같은 수의 성냥을 사용하여 00이라는 두자리 수를 만들 수 있다.
00은 첫번째 자리에 올 수 없기 때문에 처음 계산에서는 배제되었지만, 가운데에 위치하게 되면 교체하는 것이 유리하다.
따라서 b가 2인 경우, 뒷 숫자들은 888.... 이기 때문에 b를 0으로, 뒷 숫자들은 맨앞 8을 0으로 교체하여 0과 088...로 사용한다.

큰 수를 만드는 경우는 규칙이 매우 간단하다.
작은수의 반대로 자릿수가 클수록 큰 수이며, 높은자리가 높을 수록 큰 수가 된다.
즉, 사용하는 성냥의 수가 가장 작은 1을 최대한 나열하는 것이 유리하다.
그러나, 주어진 성냥의 수가 홀수일 경우 2로 나누어 떨어지지 않기 때문에 3개를 먼저 빼서 7로 만들어 두고 뒤에 1을 나열한다.
'''
