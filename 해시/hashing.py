# 백준 15829번 Hashing : https://www.acmicpc.net/problem/15829

import sys
input = sys.stdin.readline

n = int(input())
word = list(input().strip())
m = 1234567891
r = 31

key = 0
for i in range(len(word)):
    now = (ord(word[i]) - 96)
    key += now * (r ** i)
    
print(key % m)

# 알고리즘 : 해싱
'''
풀이 : 문제에서 제시한 그대로 해시 계산을 수행한다.
문자열의 해싱을 구현해보는 문제다.
'''
