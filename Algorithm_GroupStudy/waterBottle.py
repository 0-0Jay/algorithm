# 백준 2251번 물통 : https://www.acmicpc.net/problem/2251

import sys
import math

chk = [[[0 for _ in range(201)] for _ in range(201)] for _ in range(201)]
s = set()

def DFS(a, b, c):
    if chk[a][b][c] == 1: return
    chk[a][b][c] = 1
    if a == 0: s.add(c)
    
    # C -> A
    if A - a <= c: DFS(A, b, c - (A - a)) # A가 꽉차게
    else: DFS(a + c, b, 0) # C가 텅비게 
    # B -> A
    if A - a <= b: DFS(A, b - (A - a), c) # A가 꽉차게
    else: DFS(a + b, 0, c) # B가 텅비게
    # A -> C
    if C - c <= a: DFS(a - (C - c), b, C) # C가 꽉차게
    else: DFS(0, b, c + a) # A가 텅비게
    # B -> C
    if C - c <= b: DFS(A, b - (C - c), C) # C가 꽉차게
    else: DFS(a, 0, c + b) # B가 텅비게
    # A -> B
    if B - b <= a: DFS(a - (B - b), B, c) # B가 꽉차게
    else: DFS(0, b + a, c) # A가 텅비게
    # C -> B
    if B - b <= c: DFS(a, B, c - (B - b)) # B가 꽉차게
    else: DFS(a, b + c, 0) # C가 텅비게

    return

A, B, C = map(int, input().split())

DFS(0, 0, C)
s = sorted(list(s))

for i in s: print(i, end=" ")

# 알고리즘 : 정렬, DFS
'''
풀이 : 12가지의 경우를 DFS로 완전탐색한다.
단, 한번이라도 나온 물통 상태면 return으로 돌아가 불필요한 중복 탐색을 방지한다.
물통 상태 중복 체크는 3차원 체크 배열을 사용했다.
a가 0일때 c의 값을 set에 넣으면, 중복값을 자동으로 제거할 수 있다.
마지막에 s를 리스트로 전환하고 오름차순 정렬하여 출력한다.
'''
