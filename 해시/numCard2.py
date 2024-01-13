# 백준 10816번 숫자 카드2 : https://www.acmicpc.net/problem/10816

from collections import defaultdict, deque
import sys
input = sys.stdin.readline

n = int(input())
m = 100000000
div = 50009
arr = list(map(int, input().split()))
hash = [[] for _ in range(div)]
for i in range(n):
    index = (arr[i] + m) % div
    if len(hash[index]) == 0: hash[index].append([arr[i], 1])
    else:
        flag = 0
        for j in range(len(hash[index])):
            if hash[index][j][0] == arr[i]:
                hash[index][j][1] += 1
                flag = 1
        if flag == 0:
            hash[index].append([arr[i], 1])
            
               
k = int(input())
tmp = list(map(int,input().split()))
for i in range(k):
    index = (tmp[i] + m) % div
    cnt = 0
    for val in hash[index]:
        if val[0] == tmp[i]:
            cnt = val[1]
    print(cnt, end=" ")

# 알고리즘 : 해싱
'''
풀이 : 해싱테이블을 직접 구현한다.
div 값으로 나눈 나머지의 인덱스에 [숫자, 갯수]의 형태로 넣는다.
만약 같은 숫자가 이미 해당 인덱스에 존재한다면 그 숫자의 갯수를 +1해준다.
'''
