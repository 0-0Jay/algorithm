# 백준 22866번 탑 보기 : https://www.acmicpc.net/problem/22866

import sys
input = sys.stdin.readline

n = int(input())
tower = [0] + list(map(int, input().split()))
arr = [[0, 0] for _ in range(n + 1)]

stk = []    
for i in range(1, n + 1):
    while stk and stk[-1][0] <= tower[i]:
        stk.pop()
    arr[i][0] += len(stk)
    if stk: arr[i][1] = stk[-1][1]
    stk.append((tower[i], i))
    
stk = []
for i in range(n, 0, -1):
    while stk and stk[-1][0] <= tower[i]:
        stk.pop()
    arr[i][0] += len(stk)
    if stk:
        if arr[i][1] == 0: arr[i][1] = stk[-1][1]
        elif abs(i - arr[i][1]) > abs(i - stk[-1][1]): arr[i][1] = stk[-1][1]
    stk.append((tower[i], i))
        
for i in range(1, n + 1):
    if arr[i][0] > 0:
        print(*arr[i])
    else:
        print(0)

# 알고리즘 : 스택
'''
풀이 : 왼쪽과 오른쪽에서 스택을 한번씩 탐색한다.
가장 가까우면서 현재 건물보다 높은 건물을 선택하되, 같은거리에 높은 건물 2개가 있다면 더 작은 번호의 건물을 선택한다.
위 조건을 위해 좌측에서부터 먼저 탐색하여 처음 발견한 가장 가까운 건물을 왼쪽에 위치한 건물로 저장한다.

tower 배열을 왼쪽 끝에서부터 순차적으로 탐색한다.
만약 스택의 top이 현재 건물보다 작거나 같으면 큰 건물이 나올 때까지 pop해준다.
pop 과정이 끝났을 때 남은 stack의 길이가 곧, 현재 건물에서 좌측을 봤을 때 볼 수 있는 더 높은 건물의 갯수가 된다.
또한 stack의 top이 곧 좌측에서 볼 수있는 더 높은 건물중 가장 가까운 건물이 된다.

우측을 봤을 때 더 높은 건물의 갯수와 가장 가까운 건물을 찾기위해 방금 과정을 tower 배열의 오른쪽 끝부터 한 번 더 수행한다.
이 때, arr에 저장된 좌측에서 가장 가까운 건물과의 거리보다 방금 우측에서 발견한 가장 가까운 건물과의 거리를 비교한다.
거리가 더 먼 경우는 무시하고, 같은 경우라면 더작은 번호는 당연히 왼쪽의 건물일테니 교체하지 않는다.
거리가 더 짧은 경우에만 arr의 가장 가까운 건물 id를 교체해준다.

모든 계산이 끝났다면, 출력 조건에 맞게 출력해준다. 
'''
