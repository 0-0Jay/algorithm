백준 2878번 캔디캔디 : https://www.acmicpc.net/problem/2878

from collections import deque
import heapq as hq
import sys
input = sys.stdin.readline

m, n = map(int, input().split())
m = -m  # 부족한 사탕 개수
want = 0  # 사탕을 원하는 인원 수
candy = []  # 각 인원이 원하는 사탕 개수

for i in range(n):
    tmp = int(input())
    if tmp != 0: 
        want += 1
        candy.append(tmp)
        m += tmp
    
candy.sort()
ans = 0
div = 2 ** 64

for i in range(n):
    fear = m // want
    if candy[i] > fear: 
        ans += (fear ** 2) % div
        m -= fear
    else: 
        ans += (candy[i] ** 2) % div
        m -= candy[i]
    want -= 1
        
print(ans % div)

# 알고리즘 : 그리디
'''
풀이 : 부족한 사탕을 최대한 분산시킨다.
처음 입력을 받을 때 0이면 원하는 사탕이 없으므로 계산에 포함되지 않게 배제한다.
숫자면, candy배열에 append 하고 원하는 사람 수에 카운팅한다.
부족한 사탕을 구하기 위해 처음 주어지는 사탕을 음수로 저장하고, 요구하는 사탕 수를 더해주는 방식을 사용했다.

부족한 사탕수와, 사탕을 원하는 인원 정보를 모두 입력받고, 요구하는 사탕 수를 오름차순 정렬한다.
정렬을 하는 이유는 적은 사탕을 원하는 인원을 앞쪽에 두어, 인원 수에 따라 분배될 사탕의 개수가 점점 늘어나는 것을 고려하기 위해서다.

예를 들면 다음과 같다.
4명의 친구가 12개의 사탕을 요구하지만 사탕이 하나도 없는 경우를 생각해보자.
분노 수치를 최소화하려면 각각 3^2의 분노 수치를 가지면 된다.
만약 1번 친구가 요구하는 사탕의 수가 2개 뿐일 경우, 남은 1개의 부족한 사탕은 다른 사람이 메꿔야 한다.
이 경우 3명의 친구에게 10개(12 - 2)의 사탕이 부족한 경우이므로 3, 3, 4로 분배가 된다.
그러나 오름차순 정렬을 하지 않아, 4명의 친구가 각각 6, 3, 2, 1 개의 사탕을 요구하는 경우를 생각해보자.
사탕이 하나도 없어 아무에게도 사탕을 주지 못했기 때문에 각각 부족한 사탕만큼 분노해야한다.
그러나 단순히 분배하게 되면 1번 친구는 사탕이 6개 부족한데 3개 만큼의 분노만 하고, 4번 친구는 사탕이 1개만 부족한데 3개를 못받은 분노를 하는 오류가 발생한다.

따라서 오름차순 정렬 후, 부족한 사탕을 현재 남은 인원만큼 분배한 개수와 각 인원이 요구하는 사탕 개수를 비교해가며 계산한다.
요구하는 사탕이 분배 개수보다 작으면 요구하는 사탕 만큼만 분노하고, 반대의 경우는 분배 개수만큼만 분노하게끔 하면 가장 적은 분노 수치를 얻을 수 있다.
'''
