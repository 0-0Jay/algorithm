# 백준 1517번 버블 소트 : https://www.acmicpc.net/problem/1517

import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n = int(input())
arr = list(map(int, input().split()))
cnt = 0

def bubble(arr, l):
    global cnt
    if l <= 1: return arr
    listA = bubble(arr[:l // 2], l // 2)
    listB = bubble(arr[l//2:], len(arr[l//2:]))
    keyA, keyB = 0, 0
    res = []
    while keyA < len(listA) or keyB < len(listB):
        if keyB == len(listB):
            res.append(listA[keyA])
            keyA+= 1
        elif keyA == len(listA):
            res.append(listB[keyB])
            keyB += 1
        elif listA[keyA] < listB[keyB]:
            res.append(listA[keyA])
            keyA += 1
        elif listB[keyB] < listA[keyA]:
            res.append(listB[keyB])
            keyB += 1
            cnt += len(listA) - keyA
        else:
            res.append(listA[keyA])
            res.append(listB[keyB])
            keyA += 1
            keyB += 1
    return res
       
bubble(arr, n)
print(cnt)

# 알고리즘 : 분할정복
'''
풀이 : 합병정렬(분할정복)을 응용하여 교체 횟수를 누적한다.
배열을 반씩 나누어 작은 배열로 만든 뒤에, 나눈 두 배열의 원소를 비교하며 res 배열에 하나씩 채워넣는다.
왼쪽(listA) 배열과 오른쪽(listB) 배열에 각각 key값을 두고, 각 배열의 key번에 있는 원소를 서로 비교한다.

listA의 값이 더 작은 경우, 교체가 발생하지 않는다. 작은 값이 왼쪽에 그대로 있기 때문이다.
그러나 listB의 값이 더 작은 경우, 교체가 발생한다.
이 때, 교체 횟수는 listA에 남은 숫자만큼 발생한다.
합병 정렬 알고리즘에 따라 항상 각 배열은 오름차순 정렬되어있기 때문이다.
-> listA의 0번 인덱스에 위치한 숫자보다 작다면 오름차순 정렬된 listA의 모든 숫자보다 작을 수 밖에 없다.
따라서 이 교체횟수를 전역변수 cnt에 누적시켜준다.
만약, 두 수가 같거나 어느 한쪽 리스트에 남은 숫자가 없다면, 단순히 key값을 이동시켜준다.

모든 정렬이 완료되면 cnt를 출력한다.
'''
