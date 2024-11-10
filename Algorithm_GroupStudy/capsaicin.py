# 백준 15824번 너 봄에는 캡사이신이 맛있단다 : https://www.acmicpc.net/problem/15824

import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n = int(input())
tmp = [0] * (n + 1)
tmp[0], tmp[1] = 1, 2
arr = sorted(map(int, input().split()))

def divconq(num):
    if tmp[num]: return tmp[num] 
    res = divconq(num // 2) ** 2
    if num % 2 != 0: res = res * 2
    tmp[num] = res % 1000000007
    return tmp[num]

scoville = 0
for i in range(1, n):
    scoville += (arr[i] - arr[0]) * (divconq(i) - 1)
    scoville -= (arr[i] - arr[0]) * (divconq(n - i - 1) - 1)
    scoville %= 1000000007

print(scoville)

# 알고리즘 : 분할정복(거듭제곱), 메모이제이션
'''
풀이 : 스코빌지수를 오름차순 정렬하고, 각 스코빌 지수가 최대값인 경우와 최소값이 경우를 계산한다.
모든 스코빌 지수 조합에서 최대값과 최소값의 차만 구하면 되기 때문에 조합을 모두 구하지 않고, 조합의 개수 공식만 사용한다.
예를 들어 1번 예제와 같이 5, 2, 8일 경우 최대값인 8과 최소값인 2의 차이인 6만 알고있으면 된다.
2와 8을 골라놓고, 가능한 모든 경우의 수는 5를 추가로 고르거나, 2와 8만 쓰는 경우 2가지다.
따라서 6 * 2를 scoville에 더해주는 방식이다.

그러나 이렇게 계산할 경우, 시간복잡도가 n*n + nlogn으로 너무 긴 시간이 걸린다.
따라서 이를 개선하기 위해 다음과 같이 계산한다.
먼저 i번 인덱스에 위치한 스코빌지수가 최대값인 경우는 2^i - 1과 같다.
-> 2 5 8 11의 경우 8이 최대려면 8보다 작은 (2, 5)로 가능한 모든 조합의 수 - 1(아무것도 안고르는 경우) 이다.
-> 즉, 2^2 - 1 = 3
이 값에 (i번 스코빌 지수 - 가장 작은 스코빌 지수)를 곱하여 결과값(scoville)에 더한다. 
여기서 이 값을 그대로 계산할 경우, (5, 8)을 고른 경우도 8 - 2한 값이 더해지게 된다.
이를 방지하기 위해 각 스코빌 지수가 최소값인 경우의 그만큼의 값을 빼주어야 한다.
즉, (i번 스코빌 지수 - 가장 작은 스코빌 지수) * 2^(n - i - 1) - 1의 값을 빼준다.
-> 이렇게 하면 스코빌 지수 5에 대한 계산 과정에서 이미 최대값이 8과 11인 경우에 대해 5-2를 한 번 씩 빼주게 된다.
-> 즉, 스코빌지수 8을 계산할 때 (5, 8)을 고른 경우, 6(2 ~ 8) - 3(2 ~ 5)를 해주는 것이다.
이렇게 계산하면 n번만에 모든 경우에 대한 스코빌지수를 계산할 수 있다.

이 때, 2의 거듭제곱에 대한 계산은 분할정복을 활용하여 계산한다.
'''