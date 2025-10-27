백준 1806번 부분합 : https://www.acmicpc.net/problem/1806

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))

for i in range(1, n + 1):
    arr[i] += arr[i - 1]

size = n * 2    
l, r = 0, 1

while l < r:
    if r < n and arr[r] - arr[l] < m:
        r += 1
    elif arr[r] - arr[l] >= m:
        if r - l < size:
            size = r - l
        l += 1
    else: l += 1
            
print(size if size <= n else 0)

# 알고리즘 : 누적합 + 투 포인터
'''
풀이: 누적합을 활용한 단순 투 포인터 활용 문제다.
배열을 누적합 배열로 만들어주고, l과 r 두개의 포인터를 이용해 범위를 조절하며 가장 길이가 짧은 수열은 찾는다.
'''
