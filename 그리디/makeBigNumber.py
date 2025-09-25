# 백준 16496번 - 큰 수 만들기 : https://www.acmicpc.net/problem/16496

from functools import cmp_to_key
import sys
input = sys.stdin.readline

n = int(input())
arr = list(input().split())

def tmp(x : str, y : str):
    a = x + y
    b = y + x
    if int(a) < int(b):
        return 1
    else: return -1

arr.sort(key = cmp_to_key(tmp))
res = ''
for i in range(n):
    res += arr[i]
    
print(int(res))

# 알고리즘 : 그리디
'''
풀이 : 두 수 a, b를 ab로 붙였을 때와 ba로 붙였을 때를 비교해서 더 큰 수가 되는 값을 기준으로 내림차순 정렬한다.
만약 ab가 더 크다면 a가 b보다 우선, ba가 더 크다면 b가 a보다 우선 배치되도록 정렬한다.
정렬후 배열의 수를 차례대로 나열하면 그 수가 만들 수 있는 가장 큰 수이다.
단, 이 수를 바로 출력하지 않고 res에 하나의 문자열로 합친 후, 정수로 변환해서 출력한다.
0으로만 이루어진 배열일 경우 000000 과 같은 문자열이 만들어지는데 이는 0과 같기 때문이다.
'''
