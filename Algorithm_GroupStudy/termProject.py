# 백준 9466번 텀 프로젝트 : https://www.acmicpc.net/problem/9466

from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def DFS(n):
    global cnt

    cycle.append(n)
    
    if chk[n] == 1:
        cnt -= len(cycle) - (cycle.index(n) + 1)
        return
    
    chk[n] = 1
    
    DFS(arr[n])
    return

t = int(input())
for i in range(t):
    n = int(input())
    arr = [0] + list(map(int, input().split()))
    chk = [0] * (n + 1)
    cnt = n
    for j in range(1, len(arr)):
        if chk[j] == 0:
            cycle = []
            DFS(j)
    print(cnt)

# 알고리즘 : DFS
'''
풀이 : 각 학생을 시작점으로 DFS를 돌다가 이미 cycle에 소속된 팀원을 마주치면 해당 팀원의 인덱스까지 잘라낸다.
예를들어 1 -> 2 -> 3 -> 4 -> 5 -> 3으로 DFS를 탐색했다면, 3-4-5가 하나의 팀이 된다.
그러면 3이 가장 먼저 발견된 인덱스인 2번 인덱스까지 잘라내면 남은 인원 수가 팀이 결성된 인원수다.
만약, 1 -> 2 -> 3 -> 4 -> 5 -> 3 탐색 이후에 6번 학생이 3번학생을 지목했다면,
3번은 이미 chk배열에서 1로 체크되어 있으니 인덱스 자르기 과정이 수행된다.
그러면 3의 인덱스 까지 잘라내므로 남은 인원 수가 0이고, 이는 팀 결성에 실패했으므로 cnt에서 빼지 못한다.
'''
