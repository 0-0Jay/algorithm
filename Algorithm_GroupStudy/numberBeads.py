# 백준 2613번 숫자구슬 : https://www.acmicpc.net/problem/2613

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))
l = 0
for i in range(1, n + 1):
    l = max(l, arr[i])
    arr[i] += arr[i - 1]
r = arr[-1]
    
dp = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(0, i):
        dp[i][j] = arr[i] - arr[j]

tmp = []
while l <= r:
    mid = (l + r) // 2
    
    res = [0]
    st, ed = 0, 1
    while ed <= n:
        if dp[ed][st] > mid:
            res.append(ed - 1)
            st = ed - 1
        ed += 1
    if res[-1] != n: res.append(n)
        
    if len(res) - 1 <= m: 
        r = mid - 1
        tmp = list(res)
    else: l = mid + 1
    
print(l)
ans = []
for i in range(1, len(tmp)):
    ans.append(tmp[i] - tmp[i - 1])
k = len(ans) - 1 
while len(ans) < m:
    if ans[k] > 1:
        ans[k] -= 1
        ans.append(1)
    else: k -= 1
print(*ans)

# 알고리즘 : 누적합 + DP + 이분 탐색
'''
풀이 : DP배열에 모든 구간합을 구해두고, 이분탐색을 통해 구간을 나누어 구간 갯수를 m과 비교한다.
DP 배열에 누적합을 이용해 모든 구간합을 구해둔다.
예를 들어, DP[0][3]이면 (0 + 1)번 인덱스부터 3번 인덱스까지 더한 값이다.

이 후, 이분 탐색을 통해 구슬을 나눈다.
구슬의 구간합이 mid보다 커지면 해당 인덱스 - 1을 res에 추가한다.
나눈 구간의 갯수가 m보다 작으면 구간합이 너무 크다는 의미이므로 mid를 낮추고, 아니면 올린다.

최소 최대값은 l을 통해 출력한다.
만약 구간이 m개라고 할지라도 한번 더 mid를 줄여서 더 작은 최대값이 있는지 확인하도록 구현했기 때문이다.

결과 배열인 tmp는 다음 이유로 ans에 한번 더 옮겨준다.
1. tmp에는 구간의 끝 인덱스가 저장되어 있으므로 구간 크기를 위해 이전 인덱스를 뺀 값으로 바꿔주어야한다.
2. 모든 케이스에서 최소 최대값은 정상적으로 구해지나, 배열을 구하는 방식에 있어서 요구하는 배열 길이(m)만큼의 배열이 ans에 전달되지 않는 경우가 생긴다.
  2-1) 이 경우, 1보다 큰 값들을 오른쪽부터 순차적으로 1씩 빼서 새로운 그룹으로 만들어 주었다.
     -> 아직 이 경우가 왜 통과를 받는지 모르겠다. 굉장히 그리디적인 생각으로 넣은 코드인데 통과되었다.
'''
