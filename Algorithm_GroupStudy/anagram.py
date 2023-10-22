# 백준 6443번 애너그램 : https://www.acmicpc.net/problem/6443

import sys
import math
import heapq as hq
from collections import deque

n = int(input())
di = {}

def DFS(s, d):
    if d == 0:
        print(s)
        return
    for k,v in di.items():
        if v > 0:
            di[k] -= 1
            DFS(s + k, d - 1)
            di[k] += 1
            
for i in range(n):
    word = input()
    di.clear()
    for ch in word:
        if ch in di: di[ch] += 1
        else: di[ch] = 1
    di = dict(sorted(di.items()))
    DFS("", len(word))

# 알고리즘 : 백트래킹
'''
풀이 : 딕셔너리에 각단어에 포함된 알파벳의 종류와 갯수를 저장하고, 남은 알파벳 갯수만큼만 탐색한다.
딕셔너리에 저장된 알파벳의 1개 이상이면, 해당 알파벳을 현재 단어 뒤에 이어붙인다.
d는 남은 자리의 갯수로, d가 0이면 모든 자리가 찼으니 완성된 단어를 출력하고 return한다.
이전 탐색에 사용된 딕셔너리가 현재 탐색에 영향을 끼치지 않도록 새로 단어를 받으면 딕셔너리를 clear해준다.
알파벳 순서로 출력해야 하므로 딕셔너리를 정렬해서 알파벳 순으로 탐색하도록 한다.
'''
