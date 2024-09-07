# 백준 16637번 괄호 추가하기 : https://www.acmicpc.net/problem/16637

from collections import deque
import math
import sys
input = sys.stdin.readline

n = int(input())
s = list(input().strip())
max_val = -1e12
que = deque([(s[0], 0)])
while que:
    now, id = que.popleft()
    if id >= n:
        max_val = max(max_val, int(now))
        continue
    if id + 5 <= n: 
        # 다음수와 다다음수를 괄호로 묶음
        que.append((str(eval(now + s[id + 1] + str(eval(''.join(s[id + 2 : id + 5]))))), id + 4))
    que.append((str(eval(now + ''.join(s[id + 1:id + 3]))), id + 2))
print(max_val)

# 알고리즘 : BFS, 브루트포스
'''
풀이 : 현재 수에 다음 수를 그냥 계산하는 경우와 다음 수와 그 다음 수를 괄호로 묶어 계산하는 경우로 나누어 탐색한다.
BFS를 이용해 두 경우를 탐색한다.
만약 다음에 2개의 수와 2개의 연산자가 존재한다면, 괄호로 묶을 수가 남아있으므로 묶어서 계산한 결과를 큐에 담는다.
매 탐색마다 항상 다음 수를 그냥 계산하는 경우도 큐에 담는다.
모든 경우를 탐색하여 가장 큰 결과값이 나오는 경우를 출력한다.
'''
