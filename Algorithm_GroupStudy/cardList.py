# 백준 2534번 카드 배열 : https://www.acmicpc.net/problem/2534

from collections import defaultdict, deque
import heapq as hq
import math
import sys
input = sys.stdin.readline

div = 1000000007
n, k, p = map(int, input().split())
max_graph = [[] for _ in range(n)]
min_graph = [[] for _ in range(n)]
max_bef = [0] * n
min_bef = [0] * n

for i in range(p):
    a, b = map(int, input().split())
    max_graph[a].append(b)  # 최대값을 위한 정방향 그래프
    max_bef[b] += 1
    min_graph[b].append(a)  # 최소값을 위한 역방향 그래프
    min_bef[a] += 1
    
que = []
for i in range(k):
    if max_bef[i] == 0:
        hq.heappush(que, i)

tmp = n - k  # n - k부터 n까지 넣어야 최소
res = [0] * n
while que:  # 정방향으로 돌며 각 자리에 숫자(tmp) 배치
    now = hq.heappop(que)  # 위상 정렬로 숫자를 배치할 자리를 제약조건 순서에 맞게 정렬해서 뽑음
    res[now] = tmp  # res의 now 자리에 숫자 tmp 삽입
    tmp += 1  # tmp는 1씩 증가시켜 정방향으로 배치
    for nx in max_graph[now]:
        max_bef[nx] -= 1
        if max_bef[nx] == 0:
            hq.heappush(que, nx)

for i in range(k):
    if min_bef[i] == 0:
        hq.heappush(que, i)
        
tmp = k - 1  # k-1부터 0까지 넣어야 최소
while que:  # 역방향으로 돌며 각 자리에 숫자(tmp) 배치
    now = hq.heappop(que)
    res[now] -= tmp  # res에 저장된 값에 바로 빼주어 중복 연산 최소화
    tmp -= 1  #tmp는 1씩 감소시켜 역방향으로 배치
    for nx in min_graph[now]:
        min_bef[nx] -= 1
        if min_bef[nx] == 0:
            hq.heappush(que, nx)

ans = 0          
r = 1
for i in range(k):
    ans += res[i] * r
    r = (r * n) % div  # 제곱연산은 시간복잡도가 n^2이므로 변수를 통해 이전 값을 계속 재활용
print(ans % div)

# 알고리즘 : 위상정렬 + 그리디
'''
풀이 : 위상정렬을 정방향/역방향으로 두번 수행하여 각 자리에 숫자를 배치한다.
기본적으로 최대값을 만드려면 모든 자리에 n부터 n - k까지, 최소값을 만드려면 0부터 k - 1까지의 숫자를 써야한다.
ex) 3개의 카드로 10진수 만들기 -> 987이 최대, 210이 최소

먼저 정방향으로 위상정렬을 수행하며 res 배열(자릿수 배열)을 채운다.
우선순위 큐를 통해 현재 큐에서 가장 작은 자리이면서, 가장 작은 값을 가진 자릿수를 뽑는다.
이 때, 우선순위 큐를 쓰는 이유는 이전에 모든 제약조건을 해결해 자릿수가 들어왔더라도,
다음에 들어오는 숫자가 더 작은 자릿수일 경우 이 자릿수를 작은수로 채우는 것이 더 유리하기 때문이다.
ex) 3진법이고, 1번 자리가 2번자리보다 크다는 제약조건이 있는 경우
-> 제약조건을 만족하는 숫자는 012, 021, 120 3가지가 가능.
-> 그러나 더 작은 자릿수인 0번자리에 0을 채우는 것이 가장 큰 값을 만들 수 있음

다음으로 역방향으로 위상정렬을 수행하며 res 배열에 이미 채워져 있는 값들에 현재 나온 값을 빼준다.
우선순위 큐를 통해 현재 큐에서 가장 작은 자리이면서, 가장 작은 값을 가진 자릿수를 뽑는 것은 동일하다.
제약조건은 가장 큰 수와 가장 작은 수가 동일하기 때문이다.
단, 가장 작은 수를 만들 때는 역으로 가장 작은 자리에 가장 큰 값을 넣어야 한다.
ex) 3진법이고, 1번 자리가 2번자리보다 크다는 제약조건이 있는 경우
-> 위와 같이 012, 021, 120일 때, 더 작은 자릿수인 0번 자리에 2를 채우는 것이 가장 작은 값을 만들 수 있음

최종적으로 res에 저장된 수는 만들 수의 역순으로 저장되어 있다.
ex) 실제 수가 1234라면 res 배열은 [4, 3, 2, 1]로 저장되어 있다.
따라서 for문을 통해 ans에 현재 자리의 값 * (n ^ 자릿수)를 곱한 값을 누적한다.
이 때,  ** 연산은 시간복잡도가 n^2이므로 반드시 시간초과가 발생하기 때문에 변수(r)를 하나 사용해 이전 값을 활용해 제곱수를 계산한다.
모든 계산이 끝난 값이 최대값 - 최소값의 결과값이 된다.
'''
