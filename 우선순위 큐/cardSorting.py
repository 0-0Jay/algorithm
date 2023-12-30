# 백준 1715번 카드 정렬하기 : https://www.acmicpc.net/problem/1715

import sys
input = sys.stdin.readline

def up(k):
    if k // 2 == 0: return
    if arr[k] < arr[k // 2]:
        tmp = arr[k // 2]
        arr[k // 2] = arr[k]
        arr[k] = tmp
        up(k // 2)
     
def down(k):
    sw = k * 2
    if sw >= len(arr): return
    if sw + 1 < len(arr) and arr[sw] > arr[sw + 1]: sw += 1
    if arr[k] > arr[sw]:
        tmp = arr[k]
        arr[k] = arr[sw]
        arr[sw] = tmp
        down(sw)
        
n = int(input())
arr = [0]
for i in range(n):
    num = int(input())
    arr.append(num)
    up(len(arr) - 1)
    
sum = 0
while len(arr) > 2:
    a = arr[1]
    arr[1] = arr[-1]
    arr.pop(-1)
    down(1)
    b = arr[1]
    arr[1] = arr[-1]
    arr.pop(-1)
    down(1)
    arr.append(a + b)
    sum += a + b
    up(len(arr) - 1)
   
print(sum)

# 알고리즘 : 우선순위 큐
'''
풀이 : 이전에 직접 구현한 최소 힙을 이용해 카드를 정렬한다.
가장 작은 카드뭉치 2개를 뽑아 합친 후, 다시 힙에 넣어준다.
'''
