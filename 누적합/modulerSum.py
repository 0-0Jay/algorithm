# 백준 10986번 나머지 합 : https://www.acmicpc.net/problem/10986

from collections import defaultdict
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [0]
cnt = 0
res = defaultdict(int)
for i in tuple(map(int, input().split())):
    tmp = (arr[-1] + i) % m
    arr.append(tmp)
    res[tmp] += 1
    
cnt = res[0]
for i in res.values():
    cnt += i * (i - 1) // 2
        
print(cnt)

# 알고리즘 : 구간합 + 나머지 연산
'''
풀이 : 누적합을 구하되, 나머지 연산한 결과값을 저장하여 활용한다.
일반적으로 누적합을 이용한 구간합을 구하는 방식을 사용하면, 시간복잡도가 N^2으로 시간초과가 발생한다.
이를 해결하기위해 누적합을 구할때 m으로 나눈 나머지 값을 저장한다.
이렇게 하면, 같은 나머지 값을 가지는 지점의 개수를 구할 수 있다.

예제 1번을 예로 들면 다음과 같다.
입력값 : [1 2 3 1 2]
누적합 나머지 : [1 0 0 1 0]
같은 나머지 값 1을 가지는 0번 인덱스와 3번 인덱스 사이 구간의 구간합은 반드시 나머지 연산 법칙에 따라 나머지가 0이 된다.
-> (1 + 2 + 3 + 1) - (1) = 6  -> 6 % 3 == 0
즉, 같은 나머지 값을 가지는 지점들 중 2개를 고른 조합의 수가 나머지가 0인 구간의 수가 된다.

누적합을 구하면서 일단 나머지 값이 0인 지점의 수를 cnt에 저장한다.
res에 저장해둔 나머지 값들의 개수들별로 2개를 고른 조합의 수를 구해 cnt에 누적한다.
'''
