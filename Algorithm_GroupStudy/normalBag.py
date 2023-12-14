# 백준 12865번 평범한 배낭 : https://www.acmicpc.net/problem/12865

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
arr.sort(key=lambda x: x[0])
DP = [[0,set()] for _ in range(m + 1)]
maxv = 0
        
for i in range(n):
    for j in range(n):
        if i - arr[j][0] < 0 : break;
        if j not in DP[i - arr[j][0]][1] and DP[i - arr[j][0]][0] + arr[j][1] > DP[i][0]:
            DP[i][0] = DP[i - arr[j][0]][0] + arr[j][1]
            DP[i][1] = set(DP[i - arr[j][0]][1])
            DP[i][1].add(j)
            maxv = max(maxv, DP[i][0])
            
print(maxv)

# 알고리즘 :  DP
'''
풀이 : 무게 기준으로 오름차순 한 뒤, DP 배열을 활용해 이전 무게를 가져와 계산한다.
처음 짐을 오름차순으로 정렬해두고, 현재 탐색중인 인덱스 - 짐 무게 한 인덱스에서 가치를 가져와 최대값 비교한다.

진행 방식은 예를 들면 다음과 같다.
1. 현재 탐색할 무게가 4이다.
2. 짐을 오름차순으로 정렬해둔 arr 배열을 가장 왼쪽부터 탐색한다. 예를들어 2부터 시작한다.
3. DP[4 - 2]번에 저장된 가치가 10이라면 DP[4]에 저장된 가치와 DP[2] + 현재 짐의 가치의 최대값 비교해 교체한다.

이 때, 같은 무게가 여러개 있을 수 있기 때문에 무게를 기준으로 중복체크를 하지 않고, 해당 짐의 인덱스를 기준으로 체크한다.
'''
