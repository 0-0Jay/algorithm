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
