# 백준 2632번 피자판매 : https://www.acmicpc.net/problem/2632

import sys

n = int(input())
a, b = map(int, input().split())
cnt = 0
apizza = []
bpizza = []

for i in range(a): apizza.append(int(input()))
for i in range(b): bpizza.append(int(input()))

adict = { 0 : 1, sum(apizza) : 1 }
bdict = { 0 : 1, sum(bpizza) : 1 }

for ast in range(a):
    tmp = apizza[ast]
    if tmp not in adict: adict[tmp] = 1
    else: adict[tmp] += 1
    
    for aed in range(1, a - 1):
        tmp += apizza[(ast + aed) % a]
        if tmp not in adict: adict[tmp] = 1
        else: adict[tmp] += 1
             
for bst in range(b):
    tmp = bpizza[bst]
    if tmp not in bdict: bdict[tmp] = 1
    else: bdict[tmp] += 1
    
    for bed in range(1, b - 1):
        tmp += bpizza[(bst + bed) % b]
        if tmp not in bdict: bdict[tmp] = 1
        else: bdict[tmp] += 1
        
for i in adict:
    if i > n : continue
    if n - i not in bdict: continue
    cnt += adict[i] * bdict[n - i]
        
print(cnt)

# 알고리즘 : 누적합 + 딕셔너리
'''
풀이 : 각 피자에서 나올 수 있는 모든 너비의 경우의 수를 딕셔너리에 저장하고, 합이 n이 되는 두 key의 value값을 곱해 cnt에 누적한다.
본래 1번 피자에서 경우를 하나 선택하고, 2번 피자에서 이분탐색을 통해 저점/고점 탐색으로 n - i의 경우의 수를 구해 cnt에 누적시키는 방식으로 푸는 문제다.
하지만 딕셔너리 자료구조를 통해 같은 너비가 나오는 경우를 하나의 key값에 카운트를 value로 두는 방식으로 저장하고,
두 딕셔너리를 순회하면서 합이 n이 되는 지점의 value값들을 곱해서 카운트하는 방식으로 간단하게 해결했다.
'''
