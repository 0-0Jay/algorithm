# 백준 1208번 부분수열의 합 2 : https://www.acmicpc.net/problem/1208

from collections import deque
import heapq as hq
import sys
input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))
tmp1 = { 0 : 1 }
tmp2 = { 0 : 1 }
cnt = 0

def DFS(d, tsum, a, lim):
    for i in range(d + 1, lim):
        t = tsum + arr[i]
        if t not in a:
            a[t] = 1
        else:
            a[t] += 1
        DFS(i, t, a, lim)
       
DFS(-1, 0, tmp1, n // 2)   
DFS(n // 2 - 1, 0, tmp2, n)

for k,v in tmp1.items():
    if s - k in tmp2:
        cnt += v * tmp2[s - k]
        if k == 0 and s == 0: cnt -= 1
        
print(cnt)

# 알고리즘 : DFS + 딕셔너리
'''
풀이 : DFS로 가능한 모든 부분수열의 합을 구하고, 딕셔너리를 활용해 탐색한다.
DFS로 처음부터 마지막까지 모든 부분수열의 합을 구하게 되면, O(n^2)의 탐색을 수행해야 한다.
그러나 임의로 arr를 반으로 나누어 부분수열 합을 구하면, O(2 * (n/2)^2)로 탐색시간을 줄일 수 있다.
ex) n이 8인경우 전자는 64, 후자는 32가 소요

위 과정을 통해 0~n/2까지의 부분수열을 담은 딕셔너리 tmp1과 나머지의 부분수열을 담은 딕셔너리 tmp2를 서로 비교하며 탐색한다.
이 때, tmp1이나 tmp2에서 값을 뽑았을때 그 값이 이미 s인 경우 반대편에서는 뽑지 않아야한다.
따라서 이 경우를 계산하기위에 tmp1과 tmp2에 임의로 key 0을 주고 value를 1로 둔다.
단, 모든 원소가 0인 arr이 주어졌을 경우 임의로 넣어둔 tmp1[0]의 1과 tmp2[0]의 1이 계산에 포함되는 반례가 발생한다.
즉, 양쪽에서 모두 아무 키도 뽑지 않은 경우 1회가 cnt에 포함된다.
이를 처리해주기 위해 만약 뽑은 키도 0이고 s도 0이면 카운트에서 1을 빼준다.
'''
