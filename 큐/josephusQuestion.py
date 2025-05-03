# 백준 11866번 - 요세푸스 문제 0 : https://www.acmicpc.net/problem/11866

from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n, k = map(int, input().split())
que = deque([str(i) for i in range(1, n + 1)])
ans = "<"
while que:
    for i in range(k - 1): que.append(que.popleft())
    ans += que.popleft()
    if que: ans += ", "
ans += ">"
print(ans)

# 알고리즘 : 큐
'''
풀이 : 큐에 숫자를 넣고 k - 1번 pop과 push를 반복한 후, answer에 다음 pop한 글자를 추가한다.
출력 형식에 맞게 ans에 <로 시작하고, >로 끝낸다.
k번째 숫자를 넣어야하기 때문에 k - 1번 pop한 숫자를 다시 큐의 맨 뒤에 push한다.
다음 pop한 숫자를 ans에 추가하고 ,를 추가한다. 이를 que가 모두 빌 때까지 반복한다.
'''
