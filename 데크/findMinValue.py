# 백준 11003번 최솟값 찾기 : https://www.acmicpc.net/problem/11003

from collections import deque
import sys
input = sys.stdin.readline

n, l = map(int, input().split())
arr = [0] + list(map(int, input().split()))
que = deque()

for i in range(1, len(arr)):
    if que and que[0][1] < i - l + 1: que.popleft()
    while que and que[-1][0] > arr[i]:
        que.pop()
    que.append((arr[i], i))
    print(que[0][0], end=' ')

# 알고리즘 : 데크 백준 11003번 최솟값 찾기 : https://www.acmicpc.net/problem/11003

from collections import deque
import sys
input = sys.stdin.readline

n, l = map(int, input().split())
arr = [0] + list(map(int, input().split()))
que = deque()

for i in range(1, len(arr)):
    if que and que[0][1] < i - l + 1: que.popleft()
    while que and que[-1][0] > arr[i]:
        que.pop()
    que.append((arr[i], i))
    print(que[0][0], end=' ')

# 알고리즘 : 데크
'''
풀이 : 범위 별 최소값과, 다음 최소값 후보 값 두개를 데크를 활용해 관리한다.
만약 이 문제를 슬라이딩 윈도우를 사용해서 접근하게 되면, l길이의 서브배열별로 최소값 계산을 하게 된다.
이 경우, 시간 복잡도는 n * l로 시간제한 2.4초를 훨씬 넘게 된다.

이를 해결하기 위해 데크 자료구조를 사용한다.
덱의 0번 인덱스는 현재 범위에서의 최소값, 나머지 인덱스는 현재 범위에서 다음 최소값 후보를 둔다.
최소값 후보를 두는 이유는, 0번 인덱스의 최소값이 범위를 벗어났을 때, 바로 다음 최소값이 될 수 있기 때문이다.

매 숫자마다 다음 과정을 반복한다.
1. 데크에 숫자가 있을 경우, 데크의 0번 인덱스가 범위 안에 속해 있는지 확인하고, 아니라면 덱에서 제거한다.
2. 데크의 숫자들이 현재 숫자보다 작으면, 범위 안의 최소값이 갱신되어야 하므로 교체한다.
-> 데크에 포함된 숫자는 1번 과정에 의해 반드시 범위 안의 값만 존재한다.
-> 예를 들어, 데크에 [3, 5]가 있고 새로 2가 들어오는 경우 3, 5의 유효 범위에 관계 없이 모두 제거된다.
3. 현재 값 arr[i]를 덱에 추가한다.
4. 데크의 왼쪽 끝을 출력한다.
-> 2번 과정에 의해 데크의 왼쪽 끝 즉, 0번 인덱스는 반드시 범위 내 최소값이 된다.
'''
