# 백준 1927번 최소 힙 : https://www.acmicpc.net/problem/1927

import sys
input = sys.stdin.readline

def up(k):
    if k // 2 == 0: return
    if arr[k] < arr[k // 2]:
        arr[k // 2], arr[k] = arr[k], arr[k // 2]
        up(k // 2)
     
def down(k):
    sw = k * 2
    if sw >= len(arr): return
    if sw + 1 < len(arr) and arr[sw] > arr[sw + 1]: sw += 1
    if arr[k] > arr[sw]:
        arr[k], arr[sw] = arr[sw], arr[k]
        down(sw)
        
n = int(input())
arr = [0]
for i in range(n):
    num = int(input())
    if num == 0:
        if len(arr) == 1: 
            print(0)
        else:
            print(arr[1])
            arr[1] = arr[-1]
            arr.pop(-1)
            down(1)
    else:
        arr.append(num)
        up(len(arr) - 1)

# 알고리즘 : 우선순위 큐
''' 
풀이 : 최소 힙을 직접 구현해본다.
'''
