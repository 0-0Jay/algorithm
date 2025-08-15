# 백준 1253번 좋다 : https://www.acmicpc.net/problem/1253

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
cnt = 0
for i in range(n):
    l, r = 0, n - 1
    while l < r:
        if arr[l] + arr[r] < arr[i] or l == i: l += 1
        elif arr[l] + arr[r] > arr[i] or r == i: r -= 1
        else: 
            cnt += 1
            break
    
print(cnt)

# 알고리즘 : 투 포인터
'''
풀이 : 수 배열을 정렬하고, 왼쪽 끝과 오른쪽 끝에 두 개의 포인터를 두고 간격을 좁혀가며 탐색한다.
매 탐색마다 arr의 0번 인덱스와 n-1번 인덱스에 두 개의 포인터(l, r)를 놓고 탐색한다.
두 수를 더한 값이 작으면 l을 +1 이동시키고, 크면 r을 -1 이동시킨다.
단, l이나 r이 가르키는 인덱스가 현재 찾아야 하는 수의 인덱스 일 수 있다.
이 경우, 찾아야 하는 수의 인덱스를 가르키는 포인터를 한칸 더 이동시켜서 겹치지 않게 한다.
모든 경우를 찾는 게 아니므로 한 번이라도 두 수의 합이 찾아지면 카운팅하고 break로 다음 수로 넘어간다
'''
