# 백준 1016번 제곱ㄴㄴ수 : https://www.acmicpc.net/problem/1016

from collections import deque
import heapq as hq
import math
import sys
input = sys.stdin.readline

min, max = map(int,input().split())
chk = set()
for i in range(2, int(math.sqrt(max)) + 1):
    n = i * i
    for j in range((min // n) * n, max + 1, n):
        if j >= min: chk.add(j)
        
print(max - min - len(chk) + 1)

# 알고리즘 : 에라토스테네스의 체
'''
풀이 : 에라토스테네스의 체 알고리즘을 응용하되, min과 max 사이에만 체크한다.
평소 풀던 에라토스테네스의 체 응용 문제처럼 1부터 지우기 시작하면 반드시 TLE가 발생하는 문제다.
min보다 작으면서 현재 제곱수(n)에게 나누어 떨어지는 가장 큰 수를 찾아 그 수부터 탐색을 시작한다.
제곱ㄴㄴ수를 체크하는 것 또한 집합 자료(set)를 이용해서 불필요한 메모리 사용도 최소화한다.
결과값은 숫자 개수(max - min - 1) - 제곱수로 나누어 떨어지는 숫자 개수(chk의 길이)다.
'''
