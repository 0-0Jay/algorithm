# 백준 2295번 세 수의 합 : https://www.acmicpc.net/problem/2295

from collections import defaultdict, deque
import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort()

tmp = set()
for i in arr:
    for j in arr:
        tmp.add(i + j)

for i in range(n - 1, -1, -1):
    for j in range(i+1):
        if arr[i] - arr[j] in tmp:
            print(arr[i])
            exit(0)

# 알고리즘 : 집합 + 그리디
'''
풀이 : x + y + z = k를 x + y와 k - z로 계산하여 두 값이 같은 최대값을 찾는다.
arr을 정렬해두고, tmp에 arr에서 두개를 뽑아 더한 값을 넣어둔다.
arr의 오른쪽 끝에서부터 하나씩 줄여가며 k - z를 구하고, 이 값이 tmp에 있는 지 확인한다.
tmp에 있으면 즉시 arr[i]를 출력하고 exit로 종료시킨다.
우측부터 탐색했으므로 반드시 최대값이기 때문이다.
'''
